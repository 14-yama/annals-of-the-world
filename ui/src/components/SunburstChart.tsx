/* ─── D3 Sunburst / Treemap Visualization — Annals of the World ─── */
import React, { useRef, useEffect, useState } from 'react'
import { Box, Text, Flex, Heading } from '@chakra-ui/react'
import * as d3 from 'd3'

interface HierarchyDataNode {
  name: string
  value?: number
  color?: string
  children?: HierarchyDataNode[]
}

interface SunburstChartProps {
  data: HierarchyDataNode
  title?: string
  width?: number
  height?: number
}

export default function SunburstChart({ data, title, width = 500, height = 500 }: SunburstChartProps) {
  const svgRef = useRef<SVGSVGElement>(null)
  const [hoveredNode, setHoveredNode] = useState<{ name: string; value: number; depth: number } | null>(null)

  useEffect(() => {
    if (!svgRef.current) return
    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const radius = Math.min(width, height) / 2

    const partition = d3.partition<HierarchyDataNode>()
      .size([2 * Math.PI, radius])

    const hierarchy = d3.hierarchy(data)
      .sum(d => d.value || 0)
      .sort((a, b) => (b.value || 0) - (a.value || 0))

    const root = partition(hierarchy)

    const color = d3.scaleOrdinal<string>()
      .domain(root.children?.map(d => d.data.name) || [])
      .range(['#D4AF37', '#8B3A3A', '#4A90D9', '#6B3FA0', '#DD6B20', '#2F855A', '#C53030', '#38B2AC', '#D69E2E', '#805AD5'])

    const arc = d3.arc<d3.HierarchyRectangularNode<HierarchyDataNode>>()
      .startAngle(d => d.x0)
      .endAngle(d => d.x1)
      .padAngle(d => Math.min((d.x1 - d.x0) / 2, 0.005))
      .padRadius(radius / 2)
      .innerRadius(d => d.y0)
      .outerRadius(d => d.y1 - 1)

    const g = svg.append('g')
      .attr('transform', `translate(${width / 2},${height / 2})`)

    g.selectAll('path')
      .data(root.descendants().filter(d => d.depth > 0))
      .join('path')
      .attr('fill', d => {
        if (d.data.color) return d.data.color
        let node: d3.HierarchyRectangularNode<HierarchyDataNode> | null = d
        while (node && node.depth > 1) node = node.parent
        return node ? color(node.data.name) : '#ccc'
      })
      .attr('fill-opacity', d => 0.9 - d.depth * 0.15)
      .attr('d', arc as any)
      .attr('cursor', 'pointer')
      .on('mouseenter', function (event, d) {
        d3.select(this).attr('fill-opacity', 1).attr('stroke', '#2D2A24').attr('stroke-width', 2)
        setHoveredNode({ name: d.data.name, value: d.value || 0, depth: d.depth })
      })
      .on('mouseleave', function (_, d) {
        d3.select(this).attr('fill-opacity', 0.9 - d.depth * 0.15).attr('stroke', 'none')
        setHoveredNode(null)
      })

    // Labels for top-level segments
    g.selectAll('text')
      .data(root.descendants().filter(d => d.depth === 1 && (d.x1 - d.x0) > 0.15))
      .join('text')
      .attr('transform', d => {
        const x = (d.x0 + d.x1) / 2 * 180 / Math.PI
        const y = (d.y0 + d.y1) / 2
        return `rotate(${x - 90}) translate(${y},0) rotate(${x < 180 ? 0 : 180})`
      })
      .attr('dy', '0.35em')
      .attr('text-anchor', 'middle')
      .attr('font-size', '10px')
      .attr('font-family', 'Inter, sans-serif')
      .attr('fill', '#2D2A24')
      .attr('font-weight', 600)
      .text(d => d.data.name.length > 12 ? d.data.name.slice(0, 10) + '…' : d.data.name)

    // Center label
    g.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '-0.2em')
      .attr('font-size', '14px')
      .attr('font-family', '"Cormorant Garamond", serif')
      .attr('font-weight', 700)
      .attr('fill', '#2D2A24')
      .text(data.name)

    g.append('text')
      .attr('text-anchor', 'middle')
      .attr('dy', '1em')
      .attr('font-size', '10px')
      .attr('fill', '#9E9A90')
      .text(`${root.descendants().length - 1} items`)

  }, [data, width, height])

  return (
    <Box>
      {title && (
        <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#2D2A24" mb={3}>
          {title}
        </Heading>
      )}
      <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} position="relative" display="flex" justifyContent="center">
        <svg ref={svgRef} width={width} height={height} />
        {hoveredNode && (
          <Box position="absolute" top={3} right={3} bg="rgba(250,243,232,0.97)" border="1px solid" borderColor="#E4E2DC" borderRadius="md" p={3}>
            <Text fontSize="sm" fontWeight={600} color="#2D2A24">{hoveredNode.name}</Text>
            <Text fontSize="xs" color="#9E9A90">Value: {hoveredNode.value.toLocaleString()}</Text>
            <Text fontSize="xs" color="#96770B">Depth: {hoveredNode.depth}</Text>
          </Box>
        )}
      </Box>
    </Box>
  )
}
