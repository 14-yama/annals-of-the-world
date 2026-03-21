/* ─── Causal Chain Visualization — Annals of the World ─── */
/* Single-column vertical flowchart with non-crossing side-routed edges */
import React, { useEffect, useRef, useState } from 'react'
import * as d3 from 'd3'
import type { CaseStudy, CausalNode, CausalEdge } from '../types'
import { FRAMEWORK_MAP } from '../constants/frameworks'

interface CausalChainProps {
  caseStudy: CaseStudy
}

export default function CausalChain({ caseStudy }: CausalChainProps) {
  const containerRef = useRef<HTMLDivElement>(null)
  const svgRef = useRef<SVGSVGElement>(null)
  const [activeNode, setActiveNode] = useState<string | null>(null)
  const [activeEdge, setActiveEdge] = useState<string | null>(null)

  useEffect(() => {
    if (!svgRef.current || !containerRef.current) return
    const containerW = containerRef.current.clientWidth || 900

    const sorted = [...caseStudy.nodes].sort((a, b) => a.year - b.year)
    const nodeW = Math.min(480, containerW - 120)
    const nodeH = 56
    const gapY = 28
    const padX = Math.max(60, (containerW - nodeW) / 2)
    const padTop = 20

    // All nodes in a single centered column
    const positions = sorted.map((n, i) => {
      const x = padX
      const y = padTop + i * (nodeH + gapY)
      return { ...n, x, y, cx: x + nodeW / 2, cy: y + nodeH / 2, idx: i }
    })

    const posMap = new Map(positions.map(p => [p.id, p]))
    const idxMap = new Map(sorted.map((n, i) => [n.id, i]))

    // Classify edges: sequential (step-to-next-step) vs long-range (skips steps)
    const seqEdges: typeof caseStudy.edges = []
    const longEdges: typeof caseStudy.edges = []
    caseStudy.edges.forEach(e => {
      const si = idxMap.get(e.source)
      const ti = idxMap.get(e.target)
      if (si === undefined || ti === undefined) return
      if (ti === si + 1) seqEdges.push(e)
      else longEdges.push(e)
    })

    const w = containerW
    const h = padTop + sorted.length * (nodeH + gapY) + 20

    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()
    svg.attr('width', w).attr('height', h).attr('viewBox', `0 0 ${w} ${h}`)
      .style('font-family', 'Inter, sans-serif')

    const defs = svg.append('defs')

    // Drop shadow filter
    const shadow = defs.append('filter').attr('id', 'card-shadow')
      .attr('x', '-5%').attr('y', '-5%').attr('width', '110%').attr('height', '120%')
    shadow.append('feDropShadow').attr('dx', 0).attr('dy', 2).attr('stdDeviation', 3)
      .attr('flood-color', '#2D2A24').attr('flood-opacity', 0.08)

    // Arrow markers
    const fwIds = [...new Set(caseStudy.edges.map(e => e.framework))]
    fwIds.forEach(fId => {
      const c = FRAMEWORK_MAP[fId]?.color || '#888'
      defs.append('marker').attr('id', `arr-${fId}`)
        .attr('viewBox', '0 0 10 10').attr('refX', 9).attr('refY', 5)
        .attr('markerWidth', 7).attr('markerHeight', 7).attr('orient', 'auto')
        .append('path').attr('d', 'M0,1 L10,5 L0,9 Z').attr('fill', c)
    })

    // ─── Draw sequential edges (straight down between adjacent nodes) ───
    const edgeGroup = svg.append('g')
    seqEdges.forEach(e => {
      const src = posMap.get(e.source)
      const tgt = posMap.get(e.target)
      if (!src || !tgt) return
      const fw = FRAMEWORK_MAP[e.framework]
      const color = fw?.color || '#888'
      const edgeId = `${e.source}-${e.target}`
      const cx = src.cx
      const sy = src.y + nodeH
      const ty = tgt.y

      // Straight vertical connector
      const path = edgeGroup.append('path')
        .attr('d', `M${cx},${sy} L${cx},${ty}`)
        .attr('fill', 'none').attr('stroke', color)
        .attr('stroke-width', 2).attr('stroke-opacity', 0.4)
        .attr('marker-end', `url(#arr-${e.framework})`)
        .style('cursor', 'pointer')

      // Verb label
      const ly = (sy + ty) / 2
      const verbText = e.verb.length > 14 ? e.verb.slice(0, 12) + '…' : e.verb
      const badgeW = verbText.length * 6.5 + 14
      const labelG = edgeGroup.append('g')
        .attr('transform', `translate(${cx + 12},${ly})`).style('cursor', 'pointer')
      labelG.append('rect').attr('x', 0).attr('y', -8).attr('width', badgeW).attr('height', 16)
        .attr('rx', 8).attr('fill', color).attr('fill-opacity', 0.1)
      labelG.append('text').attr('x', badgeW / 2).attr('y', 0).attr('dy', '0.35em')
        .attr('text-anchor', 'middle').attr('font-size', '8px').attr('font-weight', 700)
        .attr('font-family', 'JetBrains Mono, monospace').attr('fill', color).text(verbText)

      const hoverIn = () => { path.attr('stroke-width', 3).attr('stroke-opacity', 0.8); setActiveEdge(edgeId) }
      const hoverOut = () => { path.attr('stroke-width', 2).attr('stroke-opacity', 0.4); setActiveEdge(null) }
      path.on('mouseenter', hoverIn).on('mouseleave', hoverOut)
      labelG.on('mouseenter', hoverIn).on('mouseleave', hoverOut)
    })

    // ─── Draw long-range edges (routed around the right side to avoid overlap) ───
    longEdges.forEach((e, ei) => {
      const src = posMap.get(e.source)
      const tgt = posMap.get(e.target)
      if (!src || !tgt) return
      const fw = FRAMEWORK_MAP[e.framework]
      const color = fw?.color || '#888'
      const edgeId = `${e.source}-${e.target}`

      // Route to the right of the cards, staggered to not overlap
      const rightX = padX + nodeW + 20 + ei * 14
      const sy = src.cy
      const ty = tgt.cy

      const path = edgeGroup.append('path')
        .attr('d', `M${padX + nodeW},${sy} L${rightX},${sy} L${rightX},${ty} L${padX + nodeW},${ty}`)
        .attr('fill', 'none').attr('stroke', color)
        .attr('stroke-width', 1.5).attr('stroke-opacity', 0.35)
        .attr('stroke-dasharray', '4,3')
        .attr('marker-end', `url(#arr-${e.framework})`)
        .style('cursor', 'pointer')

      // Verb label on the vertical segment
      const ly = (sy + ty) / 2
      const verbText = e.verb.length > 14 ? e.verb.slice(0, 12) + '…' : e.verb
      const labelG = edgeGroup.append('g')
        .attr('transform', `translate(${rightX + 4},${ly}) rotate(90)`).style('cursor', 'pointer')
      const badgeW = verbText.length * 6 + 10
      labelG.append('rect').attr('x', -badgeW / 2).attr('y', -7).attr('width', badgeW).attr('height', 14)
        .attr('rx', 7).attr('fill', '#FDFAF5').attr('stroke', color).attr('stroke-width', 0.5)
      labelG.append('text').attr('x', 0).attr('y', 0).attr('dy', '0.32em')
        .attr('text-anchor', 'middle').attr('font-size', '7px').attr('font-weight', 700)
        .attr('font-family', 'JetBrains Mono, monospace').attr('fill', color).text(verbText)

      const hoverIn = () => { path.attr('stroke-width', 3).attr('stroke-opacity', 0.7); setActiveEdge(edgeId) }
      const hoverOut = () => { path.attr('stroke-width', 1.5).attr('stroke-opacity', 0.35); setActiveEdge(null) }
      path.on('mouseenter', hoverIn).on('mouseleave', hoverOut)
      labelG.on('mouseenter', hoverIn).on('mouseleave', hoverOut)
    })

    // ─── Draw nodes as single-column cards ───
    const nodeGroup = svg.append('g')
    positions.forEach(p => {
      const fw = FRAMEWORK_MAP[p.framework]
      const color = fw?.color || '#888'
      const g = nodeGroup.append('g').attr('transform', `translate(${p.x},${p.y})`).style('cursor', 'pointer')

      // Card
      g.append('rect').attr('width', nodeW).attr('height', nodeH).attr('rx', 8)
        .attr('fill', '#FDFAF5').attr('stroke', color).attr('stroke-width', 1.5)
        .attr('filter', 'url(#card-shadow)')

      // Left accent bar
      g.append('rect').attr('width', 4).attr('height', nodeH).attr('rx', 2).attr('fill', color)

      // Step number
      g.append('circle').attr('cx', 22).attr('cy', nodeH / 2).attr('r', 11)
        .attr('fill', color).attr('fill-opacity', 0.12).attr('stroke', color).attr('stroke-width', 1)
      g.append('text').attr('x', 22).attr('y', nodeH / 2).attr('dy', '0.35em')
        .attr('text-anchor', 'middle').attr('font-size', '10px').attr('font-weight', 700)
        .attr('font-family', 'JetBrains Mono, monospace').attr('fill', color).text(`${p.idx + 1}`)

      // Year
      const yearStr = p.year < 0 ? `${Math.abs(p.year)} BCE` : `${p.year} CE`
      g.append('text').attr('x', 42).attr('y', 18).attr('font-size', '10px').attr('font-weight', 700)
        .attr('font-family', 'JetBrains Mono, monospace').attr('fill', color).text(yearStr)

      // Title
      const maxChars = Math.floor((nodeW - 100) / 7.5)
      const titleText = p.title.length > maxChars ? p.title.slice(0, maxChars - 1) + '…' : p.title
      g.append('text').attr('x', 42).attr('y', 40).attr('font-size', '13px').attr('font-weight', 700)
        .attr('font-family', 'Cormorant Garamond, serif').attr('fill', '#2D2A24').text(titleText)

      // Framework badge (right side)
      if (fw) {
        const fwName = fw.name.length > 12 ? fw.name.slice(0, 10) + '…' : fw.name
        const fwBadgeW = fwName.length * 6 + 12
        g.append('rect').attr('x', nodeW - fwBadgeW - 8).attr('y', 8).attr('width', fwBadgeW).attr('height', 18)
          .attr('rx', 9).attr('fill', color)
        g.append('text').attr('x', nodeW - fwBadgeW / 2 - 8).attr('y', 21)
          .attr('text-anchor', 'middle').attr('font-size', '8px').attr('font-weight', 600)
          .attr('fill', '#fff').text(fwName)
      }

      g.on('mouseenter', () => setActiveNode(p.id)).on('mouseleave', () => setActiveNode(null))
    })

    return () => { svg.selectAll('*').remove() }
  }, [caseStudy])

  const activeNodeData = activeNode ? caseStudy.nodes.find(n => n.id === activeNode) : null
  const activeEdgeData = activeEdge
    ? caseStudy.edges.find(e => `${e.source}-${e.target}` === activeEdge)
    : null

  return (
    <div ref={containerRef} style={{ width: '100%', overflowX: 'auto' }}>
      <svg ref={svgRef} style={{ width: '100%', display: 'block' }} />
      {(activeNodeData || activeEdgeData) && (
        <div style={{
          background: '#FAFAF8', border: '1px solid #E4E2DC', borderRadius: 12,
          padding: '16px 20px', marginTop: 8,
          boxShadow: '0 4px 16px rgba(44,24,16,0.1)',
        }}>
          {activeNodeData && (() => {
            const fw = FRAMEWORK_MAP[activeNodeData.framework]
            return (
              <>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6 }}>
                  <span style={{ display: 'inline-block', width: 10, height: 10, borderRadius: '50%', background: fw?.color || '#888' }} />
                  <span style={{ fontFamily: 'Cormorant Garamond, serif', fontWeight: 700, fontSize: 16, color: '#2D2A24' }}>
                    {activeNodeData.title}
                  </span>
                  <span style={{ fontFamily: 'JetBrains Mono, monospace', fontSize: 11, color: '#9E9A90', background: '#FDF8ED', padding: '2px 8px', borderRadius: 8 }}>
                    {activeNodeData.year < 0 ? `${Math.abs(activeNodeData.year)} BCE` : `${activeNodeData.year} CE`}
                  </span>
                </div>
                <div style={{ fontFamily: 'Inter, sans-serif', fontSize: 13, color: '#524E44', lineHeight: 1.7 }}>
                  {activeNodeData.description}
                </div>
              </>
            )
          })()}
          {activeEdgeData && (() => {
            const fw = FRAMEWORK_MAP[activeEdgeData.framework]
            const srcName = caseStudy.nodes.find(n => n.id === activeEdgeData.source)?.title
            const tgtName = caseStudy.nodes.find(n => n.id === activeEdgeData.target)?.title
            return (
              <>
                <div style={{ display: 'flex', alignItems: 'center', gap: 8, marginBottom: 6, flexWrap: 'wrap' }}>
                  <span style={{ background: fw?.color || '#888', color: '#fff', padding: '2px 10px', borderRadius: 12, fontSize: 11, fontWeight: 700, fontFamily: 'JetBrains Mono, monospace' }}>
                    {activeEdgeData.verb}
                  </span>
                  <span style={{ fontFamily: 'Cormorant Garamond, serif', fontSize: 14, color: '#2D2A24' }}>
                    {srcName} → {tgtName}
                  </span>
                </div>
                <div style={{ fontFamily: 'Inter, sans-serif', fontSize: 13, color: '#524E44', lineHeight: 1.7 }}>
                  {activeEdgeData.description}
                </div>
                <div style={{ fontFamily: 'Inter, sans-serif', fontSize: 11, color: '#9E9A90', marginTop: 6, fontStyle: 'italic' }}>
                  Source: {activeEdgeData.evidence}
                </div>
              </>
            )
          })()}
        </div>
      )}
    </div>
  )
}
