import React, { useRef, useEffect, useState, useCallback } from 'react'
import { Box, Flex, Text, SimpleGrid, Input, Heading } from '@chakra-ui/react'
import {
  Network, Search, X, Users, MapPin, Landmark, Scroll,
  Zap, Lightbulb, Flag, SlidersHorizontal, ChevronDown, ChevronUp,
} from 'lucide-react'
import graphData from '../data/reformations-graph.json'

/* ─── Types ─── */
interface RawNode { s: string; n: string; l: string; c: string; d: string; k: string }
interface RawEdge { s: string; e: string; t: string; c: string; v: number }

interface GNode extends RawNode {
  x: number; y: number; vx: number; vy: number
  edgeCount: number; radius: number; visible: boolean
}

/* ─── Constants ─── */
const LABEL_COLORS: Record<string, string> = {
  Person:      '#4A90D9',
  Place:       '#2F855A',
  Institution: '#D4AF37',
  Text:        '#8B3A3A',
  Event:       '#D44',
  Idea:        '#6B3FA0',
  Movement:    '#DD6B20',
  Unknown:     '#999',
}

const LABEL_ICONS: Record<string, typeof Users> = {
  Person:      Users,
  Place:       MapPin,
  Institution: Landmark,
  Text:        Scroll,
  Event:       Zap,
  Idea:        Lightbulb,
  Movement:    Flag,
}

const CLUSTER_LABELS: Record<string, string> = {
  English_Reformation: 'English',
  German_Reformation: 'German',
  Swiss_Reformation: 'Swiss',
  Catholic_Reformation: 'Catholic',
  Scottish_Reformation: 'Scottish',
  French_Reformation: 'French',
  Scandinavian_Reformations: 'Scandinavian',
  Dutch_Reformation: 'Dutch',
  Radical_Reformation: 'Radical',
  Bohemian_Moravian_Reformation: 'Bohemian-Moravian',
  Polish_Lithuanian_Reformation: 'Polish-Lithuanian',
}

/* ─── Force simulation helpers ─── */

/** Simulation state – alpha decays so the graph settles after ~300 frames. */
const sim = { alpha: 1.0, alphaMin: 0.001, alphaDecay: 0.0228, alphaTarget: 0 }

function resetAlpha(target = 0.3) {
  sim.alpha = target
}

function initNodes(raw: RawNode[], edges: RawEdge[]): GNode[] {
  const edgeCounts: Record<string, number> = {}
  edges.forEach(e => {
    edgeCounts[e.s] = (edgeCounts[e.s] || 0) + 1
    edgeCounts[e.e] = (edgeCounts[e.e] || 0) + 1
  })

  // Use cluster-based initial placement for better starting layout
  const clusterCenters: Record<string, { x: number; y: number }> = {}
  const clusterList = [...new Set(raw.map(n => n.c))]
  const cx = 600, cy = 400
  clusterList.forEach((c, i) => {
    const angle = (i / clusterList.length) * Math.PI * 2
    clusterCenters[c] = {
      x: cx + Math.cos(angle) * 300,
      y: cy + Math.sin(angle) * 300,
    }
  })

  return raw.map((n) => {
    const center = clusterCenters[n.c] || { x: cx, y: cy }
    const count = edgeCounts[n.s] || 0
    return {
      ...n,
      x: center.x + (Math.random() - 0.5) * 200,
      y: center.y + (Math.random() - 0.5) * 200,
      vx: 0, vy: 0,
      edgeCount: count,
      radius: Math.max(4, Math.min(18, 4 + count * 1.5)),
      visible: true,
    }
  })
}

function stepSimulation(
  nodes: GNode[],
  edges: RawEdge[],
  nodeIndex: Map<string, number>,
  width: number,
  height: number,
) {
  // Alpha decay – once alpha < alphaMin the layout is "frozen"
  if (sim.alpha < sim.alphaMin) return
  sim.alpha += (sim.alphaTarget - sim.alpha) * sim.alphaDecay

  const REPULSION = 600
  const SPRING = 0.005
  const REST_LEN = 80
  const DAMPING = 0.6          // stronger damping → less jitter
  const GRAVITY = 0.008
  const cx = width / 2, cy = height / 2

  // Gravity toward center
  for (const n of nodes) {
    if (!n.visible) continue
    n.vx += (cx - n.x) * GRAVITY * sim.alpha
    n.vy += (cy - n.y) * GRAVITY * sim.alpha
  }

  // Barnes-Hut style culling: skip pairs > 400px apart
  const visible = nodes.filter(n => n.visible)
  for (let i = 0; i < visible.length; i++) {
    const a = visible[i]
    for (let j = i + 1; j < visible.length; j++) {
      const b = visible[j]
      const dx = a.x - b.x
      const dy = a.y - b.y
      const distSq = dx * dx + dy * dy
      if (distSq > 160000) continue // 400^2
      const dist = Math.sqrt(distSq) || 1
      const force = (REPULSION * sim.alpha) / (dist * dist)
      const fx = (dx / dist) * force
      const fy = (dy / dist) * force
      a.vx += fx; a.vy += fy
      b.vx -= fx; b.vy -= fy
    }
  }

  // Spring forces for edges
  for (const e of edges) {
    const si = nodeIndex.get(e.s)
    const ei = nodeIndex.get(e.e)
    if (si === undefined || ei === undefined) continue
    const a = nodes[si], b = nodes[ei]
    if (!a.visible || !b.visible) continue
    const dx = b.x - a.x
    const dy = b.y - a.y
    const dist = Math.sqrt(dx * dx + dy * dy) || 1
    const force = (dist - REST_LEN) * SPRING * sim.alpha
    const fx = (dx / dist) * force
    const fy = (dy / dist) * force
    a.vx += fx; a.vy += fy
    b.vx -= fx; b.vy -= fy
  }

  // Apply velocity + damping
  for (const n of nodes) {
    if (!n.visible) continue
    n.vx *= DAMPING
    n.vy *= DAMPING
    n.x += n.vx
    n.y += n.vy
    // Bounds
    n.x = Math.max(20, Math.min(width - 20, n.x))
    n.y = Math.max(20, Math.min(height - 20, n.y))
  }
}

/* ─── Main Component ─── */
export default function GraphExplorer() {
  const canvasRef = useRef<HTMLCanvasElement>(null)
  const nodesRef = useRef<GNode[]>([])
  const nodeIndexRef = useRef<Map<string, number>>(new Map())
  const edgesRef = useRef<RawEdge[]>(graphData.edges as RawEdge[])
  const animRef = useRef<number>(0)
  const dragRef = useRef<{ idx: number; offsetX: number; offsetY: number } | null>(null)
  const panRef = useRef({ x: 0, y: 0, scale: 1, dragging: false, lastX: 0, lastY: 0 })

  const [selectedNode, setSelectedNode] = useState<GNode | null>(null)
  const [searchQuery, setSearchQuery] = useState('')
  const [activeLabels, setActiveLabels] = useState<Set<string>>(new Set(Object.keys(LABEL_COLORS)))
  const [activeClusters, setActiveClusters] = useState<Set<string>>(new Set(graphData.clusters))
  const [showFilters, setShowFilters] = useState(false)
  const [connectedEdges, setConnectedEdges] = useState<RawEdge[]>([])
  const [hoveredNode, setHoveredNode] = useState<string | null>(null)
  const [stats, setStats] = useState({ nodes: 0, edges: 0, visible: 0 })

  // Initialize
  useEffect(() => {
    const nodes = initNodes(graphData.nodes as RawNode[], graphData.edges as RawEdge[])
    nodesRef.current = nodes
    const idxMap = new Map<string, number>()
    nodes.forEach((n, i) => idxMap.set(n.s, i))
    nodeIndexRef.current = idxMap
    setStats({ nodes: nodes.length, edges: edgesRef.current.length, visible: nodes.length })
  }, [])

  // Apply filters
  useEffect(() => {
    const q = searchQuery.toLowerCase()
    let visCount = 0
    nodesRef.current.forEach(n => {
      const labelOk = activeLabels.has(n.l)
      const clusterOk = activeClusters.has(n.c)
      const searchOk = !q || n.n.toLowerCase().includes(q) || n.s.toLowerCase().includes(q) || n.d.toLowerCase().includes(q)
      n.visible = labelOk && clusterOk && searchOk
      if (n.visible) visCount++
    })
    setStats(prev => ({ ...prev, visible: visCount }))
    resetAlpha(0.5) // reheat so filtered graph re-settles
  }, [searchQuery, activeLabels, activeClusters])

  // Get connected edges for selected node
  useEffect(() => {
    if (!selectedNode) { setConnectedEdges([]); return }
    const slug = selectedNode.s
    const connected = edgesRef.current.filter(e => e.s === slug || e.e === slug)
    setConnectedEdges(connected)
  }, [selectedNode])

  // Canvas rendering + simulation loop
  useEffect(() => {
    const canvas = canvasRef.current
    if (!canvas) return
    const ctx = canvas.getContext('2d')
    if (!ctx) return

    const resize = () => {
      const parent = canvas.parentElement
      if (parent) {
        canvas.width = parent.clientWidth
        canvas.height = parent.clientHeight
      }
    }
    resize()
    window.addEventListener('resize', resize)

    let running = true
    const draw = () => {
      if (!running) return
      const { width, height } = canvas
      const pan = panRef.current

      stepSimulation(nodesRef.current, edgesRef.current, nodeIndexRef.current, width / pan.scale, height / pan.scale)

      ctx.clearRect(0, 0, width, height)
      ctx.save()
      ctx.translate(pan.x, pan.y)
      ctx.scale(pan.scale, pan.scale)

      const nodes = nodesRef.current
      const edges = edgesRef.current
      const idxMap = nodeIndexRef.current

      // Draw edges
      ctx.globalAlpha = 0.12
      ctx.lineWidth = 0.5
      for (const e of edges) {
        const si = idxMap.get(e.s)
        const ei = idxMap.get(e.e)
        if (si === undefined || ei === undefined) continue
        const a = nodes[si], b = nodes[ei]
        if (!a.visible || !b.visible) continue
        // Highlight edges for selected/hovered node
        if (selectedNode && (e.s === selectedNode.s || e.e === selectedNode.s)) {
          ctx.globalAlpha = 0.6
          ctx.lineWidth = 1.5
          ctx.strokeStyle = LABEL_COLORS[a.l] || '#999'
        } else if (hoveredNode && (e.s === hoveredNode || e.e === hoveredNode)) {
          ctx.globalAlpha = 0.4
          ctx.lineWidth = 1
          ctx.strokeStyle = '#D4AF37'
        } else {
          ctx.globalAlpha = 0.12
          ctx.lineWidth = 0.5
          ctx.strokeStyle = '#B8B2A4'
        }
        ctx.beginPath()
        ctx.moveTo(a.x, a.y)
        ctx.lineTo(b.x, b.y)
        ctx.stroke()
      }

      // Draw nodes
      ctx.globalAlpha = 1
      for (const n of nodes) {
        if (!n.visible) continue
        const isSelected = selectedNode?.s === n.s
        const isHovered = hoveredNode === n.s
        const isConnected = selectedNode && connectedEdges.some(e => e.s === n.s || e.e === n.s)

        ctx.beginPath()
        const r = isSelected ? n.radius * 1.5 : isHovered ? n.radius * 1.3 : n.radius
        ctx.arc(n.x, n.y, r, 0, Math.PI * 2)
        ctx.fillStyle = LABEL_COLORS[n.l] || '#999'

        if (selectedNode && !isSelected && !isConnected) {
          ctx.globalAlpha = 0.15
        } else {
          ctx.globalAlpha = 0.9
        }
        ctx.fill()

        if (isSelected || isHovered) {
          ctx.strokeStyle = '#2D2A24'
          ctx.lineWidth = 2
          ctx.stroke()
        }

        // Label for larger or selected nodes
        if ((n.edgeCount >= 5 || isSelected || isHovered) && panRef.current.scale > 0.5) {
          ctx.globalAlpha = isSelected ? 1 : 0.8
          ctx.font = `${isSelected ? 'bold ' : ''}${isSelected ? 11 : 9}px Inter, sans-serif`
          ctx.fillStyle = '#2D2A24'
          ctx.textAlign = 'center'
          ctx.fillText(n.n.length > 25 ? n.n.slice(0, 23) + '…' : n.n, n.x, n.y - r - 4)
        }
        ctx.globalAlpha = 1
      }

      // Edge labels for selected node
      if (selectedNode && panRef.current.scale > 0.7) {
        ctx.font = '8px Inter, sans-serif'
        ctx.globalAlpha = 0.7
        for (const e of connectedEdges) {
          const si = idxMap.get(e.s)
          const ei = idxMap.get(e.e)
          if (si === undefined || ei === undefined) continue
          const a = nodes[si], b = nodes[ei]
          if (!a.visible || !b.visible) continue
          const mx = (a.x + b.x) / 2
          const my = (a.y + b.y) / 2
          ctx.fillStyle = '#8B3A3A'
          ctx.textAlign = 'center'
          const label = e.t.replace(/_/g, ' ')
          ctx.fillText(label.length > 20 ? label.slice(0, 18) + '…' : label, mx, my - 3)
        }
        ctx.globalAlpha = 1
      }

      ctx.restore()
      animRef.current = requestAnimationFrame(draw)
    }

    animRef.current = requestAnimationFrame(draw)

    return () => {
      running = false
      cancelAnimationFrame(animRef.current)
      window.removeEventListener('resize', resize)
    }
  }, [selectedNode, hoveredNode, connectedEdges])

  // Mouse interaction
  const screenToWorld = useCallback((sx: number, sy: number) => {
    const pan = panRef.current
    return { x: (sx - pan.x) / pan.scale, y: (sy - pan.y) / pan.scale }
  }, [])

  const findNodeAt = useCallback((wx: number, wy: number): number => {
    const nodes = nodesRef.current
    for (let i = nodes.length - 1; i >= 0; i--) {
      const n = nodes[i]
      if (!n.visible) continue
      const dx = n.x - wx, dy = n.y - wy
      if (dx * dx + dy * dy <= (n.radius + 4) * (n.radius + 4)) return i
    }
    return -1
  }, [])

  const handleMouseDown = useCallback((e: React.MouseEvent<HTMLCanvasElement>) => {
    const rect = canvasRef.current!.getBoundingClientRect()
    const sx = e.clientX - rect.left, sy = e.clientY - rect.top
    const { x, y } = screenToWorld(sx, sy)
    const idx = findNodeAt(x, y)
    if (idx >= 0) {
      dragRef.current = { idx, offsetX: nodesRef.current[idx].x - x, offsetY: nodesRef.current[idx].y - y }
    } else {
      panRef.current.dragging = true
      panRef.current.lastX = sx
      panRef.current.lastY = sy
    }
  }, [screenToWorld, findNodeAt])

  const handleMouseMove = useCallback((e: React.MouseEvent<HTMLCanvasElement>) => {
    const rect = canvasRef.current!.getBoundingClientRect()
    const sx = e.clientX - rect.left, sy = e.clientY - rect.top
    const { x, y } = screenToWorld(sx, sy)

    if (dragRef.current) {
      const n = nodesRef.current[dragRef.current.idx]
      n.x = x + dragRef.current.offsetX
      n.y = y + dragRef.current.offsetY
      n.vx = 0; n.vy = 0
      resetAlpha(0.1) // gently reheat on drag
    } else if (panRef.current.dragging) {
      panRef.current.x += sx - panRef.current.lastX
      panRef.current.y += sy - panRef.current.lastY
      panRef.current.lastX = sx
      panRef.current.lastY = sy
    } else {
      const idx = findNodeAt(x, y)
      const slug = idx >= 0 ? nodesRef.current[idx].s : null
      setHoveredNode(slug)
    }
  }, [screenToWorld, findNodeAt])

  const handleMouseUp = useCallback((e: React.MouseEvent<HTMLCanvasElement>) => {
    if (dragRef.current) {
      // If barely moved, treat as click
      const rect = canvasRef.current!.getBoundingClientRect()
      const { x, y } = screenToWorld(e.clientX - rect.left, e.clientY - rect.top)
      const idx = findNodeAt(x, y)
      if (idx >= 0) {
        setSelectedNode(prev => prev?.s === nodesRef.current[idx].s ? null : nodesRef.current[idx])
      }
    }
    dragRef.current = null
    panRef.current.dragging = false
  }, [screenToWorld, findNodeAt])

  const handleWheel = useCallback((e: React.WheelEvent<HTMLCanvasElement>) => {
    e.preventDefault()
    const pan = panRef.current
    const rect = canvasRef.current!.getBoundingClientRect()
    const mx = e.clientX - rect.left
    const my = e.clientY - rect.top
    const factor = e.deltaY < 0 ? 1.1 : 0.9
    const newScale = Math.max(0.15, Math.min(4, pan.scale * factor))
    // Zoom toward mouse
    pan.x = mx - (mx - pan.x) * (newScale / pan.scale)
    pan.y = my - (my - pan.y) * (newScale / pan.scale)
    pan.scale = newScale
  }, [])

  const toggleLabel = (label: string) => {
    setActiveLabels(prev => {
      const next = new Set(prev)
      next.has(label) ? next.delete(label) : next.add(label)
      return next
    })
  }

  const toggleCluster = (cluster: string) => {
    setActiveClusters(prev => {
      const next = new Set(prev)
      next.has(cluster) ? next.delete(cluster) : next.add(cluster)
      return next
    })
  }

  // Resolve node name from slug for edge display
  const nodeName = (slug: string): string => {
    const idx = nodeIndexRef.current.get(slug)
    if (idx !== undefined) return nodesRef.current[idx].n
    return slug.replace(/_/g, ' ')
  }

  return (
    <Box h="calc(100vh - 80px)">
      {/* Header */}
      <Flex justify="space-between" align="center" mb={3}>
        <Flex align="center" gap={3}>
          <Network size={24} color="#D4AF37" />
          <Heading
            fontFamily='"Cinzel", serif'
            fontSize="2xl"
            fontWeight={700}
            color="#2D2A24"
          >
            Reformations Graph
          </Heading>
          <Text fontSize="xs" color="#9E9A90" ml={2}>
            {stats.visible} / {stats.nodes} nodes &middot; {stats.edges} edges &middot; 11 clusters
          </Text>
        </Flex>
        <Flex gap={2}>
          <Flex align="center" bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="md" px={2}>
            <Search size={14} color="#9E9A90" />
            <Input
              placeholder="Search nodes..."
              size="sm"
              variant="flushed"
              px={2}
              value={searchQuery}
              onChange={e => setSearchQuery(e.target.value)}
              fontSize="sm"
              border="none"
            />
            {searchQuery && (
              <Box cursor="pointer" onClick={() => setSearchQuery('')}>
                <X size={14} color="#9E9A90" />
              </Box>
            )}
          </Flex>
          <Box
            as="button"
            bg={showFilters ? '#2D2A24' : 'white'}
            color={showFilters ? '#D4AF37' : '#524E44'}
            border="1px solid"
            borderColor={showFilters ? '#2D2A24' : '#E4E2DC'}
            borderRadius="md"
            px={3}
            py={1.5}
            fontSize="sm"
            cursor="pointer"
            display="flex"
            alignItems="center"
            gap={1}
            onClick={() => setShowFilters(!showFilters)}
          >
            <SlidersHorizontal size={14} />
            Filters
            {showFilters ? <ChevronUp size={12} /> : <ChevronDown size={12} />}
          </Box>
        </Flex>
      </Flex>

      {/* Filters Panel */}
      {showFilters && (
        <Box
          bg="white"
          border="1px solid"
          borderColor="#E4E2DC"
          borderRadius="lg"
          p={4}
          mb={3}
        >
          <Flex gap={8} wrap="wrap">
            {/* Label filters */}
            <Box>
              <Text fontSize="xs" fontWeight={600} color="#8B3A3A" mb={2} textTransform="uppercase" letterSpacing="0.05em">
                Node Types
              </Text>
              <Flex gap={2} wrap="wrap">
                {Object.keys(LABEL_COLORS).filter(l => l !== 'Unknown').map(label => {
                  const active = activeLabels.has(label)
                  const Icon = LABEL_ICONS[label] || Network
                  return (
                    <Box
                      key={label}
                      as="button"
                      display="flex"
                      alignItems="center"
                      gap={1}
                      px={2.5}
                      py={1}
                      bg={active ? LABEL_COLORS[label] : '#F5F4F0'}
                      color={active ? 'white' : '#9E9A90'}
                      borderRadius="full"
                      fontSize="xs"
                      fontWeight={500}
                      cursor="pointer"
                      border="1px solid"
                      borderColor={active ? LABEL_COLORS[label] : '#E4E2DC'}
                      transition="all 0.2s"
                      onClick={() => toggleLabel(label)}
                    >
                      <Icon size={12} />
                      {label}
                    </Box>
                  )
                })}
              </Flex>
            </Box>

            {/* Cluster filters */}
            <Box>
              <Text fontSize="xs" fontWeight={600} color="#8B3A3A" mb={2} textTransform="uppercase" letterSpacing="0.05em">
                Clusters
              </Text>
              <Flex gap={2} wrap="wrap">
                {graphData.clusters.map((cluster: string) => {
                  const active = activeClusters.has(cluster)
                  return (
                    <Box
                      key={cluster}
                      as="button"
                      px={2.5}
                      py={1}
                      bg={active ? '#2D2A24' : '#F5F4F0'}
                      color={active ? '#D4AF37' : '#9E9A90'}
                      borderRadius="full"
                      fontSize="xs"
                      fontWeight={500}
                      cursor="pointer"
                      border="1px solid"
                      borderColor={active ? '#2D2A24' : '#E4E2DC'}
                      transition="all 0.2s"
                      onClick={() => toggleCluster(cluster)}
                    >
                      {CLUSTER_LABELS[cluster] || cluster}
                    </Box>
                  )
                })}
              </Flex>
            </Box>
          </Flex>
        </Box>
      )}

      {/* Main area: Canvas + Detail panel */}
      <Flex h="calc(100% - 60px)" gap={0}>
        {/* Canvas */}
        <Box
          flex={1}
          position="relative"
          bg="#FAFAF8"
          border="1px solid"
          borderColor="#E4E2DC"
          borderRadius="lg"
          overflow="hidden"
        >
          <canvas
            ref={canvasRef}
            style={{ width: '100%', height: '100%', cursor: dragRef.current ? 'grabbing' : 'grab' }}
            onMouseDown={handleMouseDown}
            onMouseMove={handleMouseMove}
            onMouseUp={handleMouseUp}
            onMouseLeave={() => { dragRef.current = null; panRef.current.dragging = false; setHoveredNode(null) }}
            onWheel={handleWheel}
          />

          {/* Legend */}
          <Box position="absolute" bottom={3} left={3} bg="rgba(250,243,232,0.95)" borderRadius="md" p={2.5} border="1px solid" borderColor="#E4E2DC" fontSize="xs">
            <Flex gap={3} wrap="wrap">
              {Object.entries(LABEL_COLORS).filter(([k]) => k !== 'Unknown').map(([label, color]) => (
                <Flex key={label} align="center" gap={1}>
                  <Box w="8px" h="8px" borderRadius="full" bg={color} />
                  <Text color="#524E44">{label}</Text>
                </Flex>
              ))}
            </Flex>
          </Box>

          {/* Controls hint */}
          <Box position="absolute" top={3} right={3} bg="rgba(250,243,232,0.9)" borderRadius="md" px={2} py={1} fontSize="xs" color="#9E9A90">
            Scroll = zoom &middot; Drag = pan &middot; Click node = inspect
          </Box>
        </Box>

        {/* Detail Panel */}
        {selectedNode && (
          <Box
            w="340px"
            flexShrink={0}
            bg="white"
            border="1px solid"
            borderColor="#E4E2DC"
            borderRadius="lg"
            ml={3}
            overflowY="auto"
          >
            {/* Node header */}
            <Box bg="#2D2A24" p={4} borderTopRadius="lg">
              <Flex justify="space-between" align="flex-start">
                <Box flex={1}>
                  <Flex align="center" gap={2} mb={1}>
                    <Box
                      bg={LABEL_COLORS[selectedNode.l]}
                      color="white"
                      px={2}
                      py={0.5}
                      borderRadius="full"
                      fontSize="xs"
                      fontWeight={600}
                    >
                      {selectedNode.l}
                    </Box>
                    {selectedNode.k && (
                      <Text fontSize="xs" color="#B8B2A4">
                        {selectedNode.k}
                      </Text>
                    )}
                  </Flex>
                  <Text
                    fontFamily='"Cormorant Garamond", serif'
                    fontSize="lg"
                    fontWeight={700}
                    color="#D4AF37"
                    lineHeight={1.2}
                  >
                    {selectedNode.n}
                  </Text>
                  <Text fontSize="xs" color="#B8B2A4" mt={1} fontFamily="mono">
                    {selectedNode.s}
                  </Text>
                </Box>
                <Box
                  cursor="pointer"
                  onClick={() => setSelectedNode(null)}
                  color="#B8B2A4"
                  _hover={{ color: '#D4AF37' }}
                  p={1}
                >
                  <X size={16} />
                </Box>
              </Flex>
            </Box>

            {/* Description */}
            {selectedNode.d && (
              <Box p={4} borderBottom="1px solid" borderColor="#F5F4F0">
                <Text fontSize="sm" color="#524E44" lineHeight={1.6}>
                  {selectedNode.d}
                </Text>
              </Box>
            )}

            {/* Cluster */}
            <Box px={4} py={2} borderBottom="1px solid" borderColor="#F5F4F0">
              <Text fontSize="xs" color="#96770B" fontWeight={600}>
                Cluster
              </Text>
              <Text fontSize="sm" color="#2D2A24">
                {(CLUSTER_LABELS[selectedNode.c] || selectedNode.c).replace(/_/g, ' ')} Reformation
              </Text>
            </Box>

            {/* Connected edges */}
            <Box p={4}>
              <Text fontSize="xs" color="#96770B" fontWeight={600} mb={2}>
                Relationships ({connectedEdges.length})
              </Text>
              {connectedEdges.length === 0 && (
                <Text fontSize="xs" color="#9E9A90" fontStyle="italic">
                  No documented relationships
                </Text>
              )}
              <Box maxH="400px" overflowY="auto">
                {connectedEdges.map((edge, i) => {
                  const isSource = edge.s === selectedNode.s
                  const otherSlug = isSource ? edge.e : edge.s
                  const otherName = nodeName(otherSlug)
                  const otherIdx = nodeIndexRef.current.get(otherSlug)
                  const otherNode = otherIdx !== undefined ? nodesRef.current[otherIdx] : null
                  const otherColor = otherNode ? LABEL_COLORS[otherNode.l] || '#999' : '#999'

                  return (
                    <Box
                      key={i}
                      p={2}
                      mb={1}
                      bg="#FAFAF8"
                      borderRadius="md"
                      cursor="pointer"
                      _hover={{ bg: '#F5F4F0' }}
                      onClick={() => {
                        if (otherNode) setSelectedNode(otherNode)
                      }}
                    >
                      <Flex align="center" gap={1.5}>
                        {isSource ? (
                          <>
                            <Text fontSize="xs" color="#8B3A3A" fontWeight={600}>
                              {edge.t.replace(/_/g, ' ')}
                            </Text>
                            <Text fontSize="xs" color="#9E9A90">→</Text>
                          </>
                        ) : (
                          <>
                            <Text fontSize="xs" color="#9E9A90">←</Text>
                            <Text fontSize="xs" color="#8B3A3A" fontWeight={600}>
                              {edge.t.replace(/_/g, ' ')}
                            </Text>
                          </>
                        )}
                      </Flex>
                      <Flex align="center" gap={1.5} mt={0.5}>
                        <Box w="6px" h="6px" borderRadius="full" bg={otherColor} flexShrink={0} />
                        <Text fontSize="xs" color="#2D2A24" fontWeight={500}>
                          {otherName}
                        </Text>
                        {otherNode && (
                          <Text fontSize="xs" color="#96770B">
                            ({otherNode.l})
                          </Text>
                        )}
                      </Flex>
                    </Box>
                  )
                })}
              </Box>
            </Box>
          </Box>
        )}
      </Flex>
    </Box>
  )
}
