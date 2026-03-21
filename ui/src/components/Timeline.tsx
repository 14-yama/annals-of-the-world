/* ─── D3-powered Interactive Timeline — Annals of the World ─── */
/* Draggable, zoomable timeline with external detail panel */
import React, { useRef, useEffect, useState, useCallback } from 'react'
import { Box, Flex, Text, Heading } from '@chakra-ui/react'
import * as d3 from 'd3'
import type { TimelineEvent } from '../types'

const SIGNIFICANCE_RADIUS: Record<string, number> = {
  low: 4, medium: 6, high: 9, critical: 13,
}

const CATEGORY_COLORS: Record<string, string> = {
  Event: '#C53030', Person: '#4A90D9', Institution: '#D4AF37',
  Movement: '#6B3FA0', Text: '#8B3A3A', Place: '#2F855A',
  Idea: '#DD6B20', Evidence: '#38B2AC',
}

const ERA_COLORS: Record<string, string> = {
  prehistory: '#645E52', ancient: '#8B3A3A', medieval: '#96770B',
  'early-modern': '#D4AF37', modern: '#4A90D9', contemporary: '#6B3FA0',
}

interface TimelineProps {
  events: TimelineEvent[]
  height?: number
  title?: string
}

export default function Timeline({ events, height = 420, title }: TimelineProps) {
  const svgRef = useRef<SVGSVGElement>(null)
  const containerRef = useRef<HTMLDivElement>(null)
  const [selected, setSelected] = useState<TimelineEvent | null>(null)
  const [containerWidth, setContainerWidth] = useState(800)

  useEffect(() => {
    const obs = new ResizeObserver(entries => {
      for (const entry of entries) setContainerWidth(entry.contentRect.width)
    })
    if (containerRef.current) obs.observe(containerRef.current)
    return () => obs.disconnect()
  }, [])

  useEffect(() => {
    if (!svgRef.current || events.length === 0) return
    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const w = containerWidth
    const h = height
    const margin = { top: 20, right: 30, bottom: 40, left: 30 }
    const innerW = w - margin.left - margin.right
    const innerH = h - margin.top - margin.bottom

    svg.attr('width', w).attr('height', h)

    const years = events.map(e => e.year)
    const minYear = Math.min(...years)
    const maxYear = Math.max(...years)
    const yearPad = Math.max(10, (maxYear - minYear) * 0.05)

    const xScale = d3.scaleLinear()
      .domain([minYear - yearPad, maxYear + yearPad])
      .range([0, innerW])

    // Clip path for the chart area
    const defs = svg.append('defs')
    defs.append('clipPath').attr('id', 'tl-clip')
      .append('rect').attr('width', innerW).attr('height', innerH)

    const chartArea = svg.append('g').attr('transform', `translate(${margin.left},${margin.top})`)

    // Zoomable content group
    const content = chartArea.append('g').attr('clip-path', 'url(#tl-clip)')
    const zoomGroup = content.append('g')

    // Sortable events
    const sortedEvents = [...events].sort((a, b) => a.year - b.year)

    function renderContent(transform: d3.ZoomTransform) {
      const newX = transform.rescaleX(xScale)
      zoomGroup.selectAll('*').remove()

      // Era background bands
      const eras = [...new Set(sortedEvents.map(e => e.era))]
      eras.forEach(era => {
        const eraEvts = sortedEvents.filter(e => e.era === era)
        const eMin = Math.min(...eraEvts.map(e => e.year))
        const eMax = Math.max(...eraEvts.map(e => e.year))
        zoomGroup.append('rect')
          .attr('x', newX(eMin) - 5).attr('y', 0)
          .attr('width', Math.max(10, newX(eMax) - newX(eMin) + 10))
          .attr('height', innerH)
          .attr('fill', ERA_COLORS[era] || '#ccc').attr('opacity', 0.06).attr('rx', 4)
      })

      // Central axis
      zoomGroup.append('line')
        .attr('x1', newX(minYear - yearPad)).attr('x2', newX(maxYear + yearPad))
        .attr('y1', innerH / 2).attr('y2', innerH / 2)
        .attr('stroke', '#E4E2DC').attr('stroke-width', 2)

      // Tick marks
      const ticks = d3.ticks(newX.domain()[0], newX.domain()[1], Math.max(5, Math.floor(innerW / 100)))
      ticks.forEach(y => {
        const x = newX(y)
        if (x < -20 || x > innerW + 20) return
        zoomGroup.append('line')
          .attr('x1', x).attr('x2', x)
          .attr('y1', innerH / 2 - 8).attr('y2', innerH / 2 + 8)
          .attr('stroke', '#D6D3CC').attr('stroke-width', 1)
        zoomGroup.append('text')
          .attr('x', x).attr('y', innerH / 2 + 24)
          .attr('text-anchor', 'middle').attr('fill', '#9E9A90')
          .attr('font-size', '10px').attr('font-family', 'Inter, sans-serif')
          .text(y < 0 ? `${Math.abs(Math.round(y))} BCE` : `${Math.round(y)} CE`)
      })

      // Event dots — stagger to avoid overlap
      sortedEvents.forEach((event, i) => {
        const x = newX(event.year)
        if (x < -30 || x > innerW + 30) return
        const above = i % 2 === 0
        const tier = Math.floor(i % 4 / 2)
        const yPos = above
          ? innerH / 2 - 35 - tier * 50
          : innerH / 2 + 35 + tier * 50
        const r = SIGNIFICANCE_RADIUS[event.significance] || 6
        const color = CATEGORY_COLORS[event.category] || '#999'
        const isSelected = selected?.id === event.id

        // Connector
        zoomGroup.append('line')
          .attr('x1', x).attr('x2', x)
          .attr('y1', innerH / 2).attr('y2', yPos)
          .attr('stroke', color).attr('stroke-width', isSelected ? 2 : 1)
          .attr('opacity', isSelected ? 0.6 : 0.25)

        // Dot
        zoomGroup.append('circle')
          .attr('cx', x).attr('cy', yPos).attr('r', isSelected ? r * 1.4 : r)
          .attr('fill', color).attr('opacity', isSelected ? 1 : 0.85)
          .attr('stroke', isSelected ? '#2D2A24' : '#fff')
          .attr('stroke-width', isSelected ? 2.5 : 1.5)
          .attr('cursor', 'pointer')
          .on('click', (ev) => { ev.stopPropagation(); setSelected(event) })
          .on('mouseenter', function () { d3.select(this).transition().duration(120).attr('r', r * 1.5).attr('opacity', 1) })
          .on('mouseleave', function () {
            const sel = selected?.id === event.id
            d3.select(this).transition().duration(120).attr('r', sel ? r * 1.4 : r).attr('opacity', sel ? 1 : 0.85)
          })

        // Label
        const label = event.title.length > 22 ? event.title.slice(0, 20) + '…' : event.title
        zoomGroup.append('text')
          .attr('x', x).attr('y', above ? yPos - r - 5 : yPos + r + 12)
          .attr('text-anchor', 'middle').attr('fill', isSelected ? '#2D2A24' : '#524E44')
          .attr('font-size', isSelected ? '10px' : '9px')
          .attr('font-family', 'Inter, sans-serif')
          .attr('font-weight', isSelected ? 700 : (event.significance === 'critical' ? 600 : 400))
          .attr('opacity', event.significance === 'low' ? 0.6 : 0.9)
          .text(label)
          .attr('cursor', 'pointer')
          .on('click', (ev) => { ev.stopPropagation(); setSelected(event) })
      })
    }

    // D3 zoom + pan
    const zoom = d3.zoom<SVGSVGElement, unknown>()
      .scaleExtent([0.3, 20])
      .translateExtent([[-innerW, 0], [innerW * 2, innerH]])
      .on('zoom', (event) => renderContent(event.transform))

    svg.call(zoom)
    svg.style('cursor', 'grab')
    svg.on('mousedown.cursor', () => svg.style('cursor', 'grabbing'))
    svg.on('mouseup.cursor', () => svg.style('cursor', 'grab'))

    // Instruction text
    chartArea.append('text')
      .attr('x', innerW - 4).attr('y', innerH - 4)
      .attr('text-anchor', 'end').attr('fill', '#D4AF37').attr('opacity', 0.5)
      .attr('font-size', '10px').attr('font-family', 'Inter, sans-serif')
      .text('Scroll to zoom · Drag to pan')

    renderContent(d3.zoomIdentity)

    return () => { svg.selectAll('*').remove() }
  }, [events, containerWidth, height, selected])

  return (
    <Box ref={containerRef} w="100%">
      {title && (
        <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#2D2A24" mb={3}>
          {title}
        </Heading>
      )}
      <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" overflow="hidden">
        <svg ref={svgRef} style={{ width: '100%', display: 'block' }} />
      </Box>

      {/* External detail panel */}
      {selected && (
        <Box mt={3} bg="#FAFAF8" border="1px solid" borderColor="#E4E2DC" borderRadius="xl" p={5}
          boxShadow="0 2px 12px rgba(44,24,16,0.08)">
          <Flex justify="space-between" align="flex-start" gap={4}>
            <Box flex={1}>
              <Flex align="center" gap={3} mb={2} flexWrap="wrap">
                <Box w="10px" h="10px" borderRadius="full" bg={CATEGORY_COLORS[selected.category] || '#999'} />
                <Text fontFamily='"JetBrains Mono", monospace' fontSize="xs" fontWeight={600}
                  color={CATEGORY_COLORS[selected.category] || '#999'}>
                  {selected.category} · {selected.year < 0 ? `${Math.abs(selected.year)} BCE` : `${selected.year} CE`}
                </Text>
                <Text fontSize="xs" color="#9E9A90" bg="#FDF8ED" px={2} py={0.5} borderRadius="full">
                  {selected.era}
                </Text>
                <Text fontSize="xs" color="#9E9A90" bg="#FDF8ED" px={2} py={0.5} borderRadius="full">
                  {selected.region}
                </Text>
                <Text fontSize="9px" fontFamily='"JetBrains Mono", monospace' color="#D4AF37"
                  bg="#FFF5EB" px={2} py={0.5} borderRadius="full" textTransform="uppercase">
                  {selected.significance}
                </Text>
              </Flex>
              <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#2D2A24" mb={2}>
                {selected.title}
              </Heading>
              <Text fontFamily='"Inter", sans-serif' fontSize="sm" color="#524E44" lineHeight={1.8}>
                {selected.description}
              </Text>
            </Box>
            <Box cursor="pointer" onClick={() => setSelected(null)} color="#9E9A90" flexShrink={0}
              _hover={{ color: '#C53030' }} fontSize="lg" fontWeight={700}>
              ✕
            </Box>
          </Flex>
        </Box>
      )}
    </Box>
  )
}
