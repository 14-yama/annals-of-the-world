/* ─── D3 Radar Chart — Annals of the World ─── */
import React, { useRef, useEffect } from 'react'
import { Box, Heading } from '@chakra-ui/react'
import * as d3 from 'd3'

interface RadarDataPoint {
  axis: string
  value: number
}

interface RadarSeries {
  name: string
  color: string
  values: RadarDataPoint[]
}

interface RadarChartProps {
  series: RadarSeries[]
  title?: string
  maxValue?: number
  width?: number
  height?: number
}

export default function RadarChart({ series, title, maxValue = 100, width = 400, height = 400 }: RadarChartProps) {
  const svgRef = useRef<SVGSVGElement>(null)

  useEffect(() => {
    if (!svgRef.current || series.length === 0) return
    const svg = d3.select(svgRef.current)
    svg.selectAll('*').remove()

    const axes = series[0].values.map(v => v.axis)
    const n = axes.length
    const radius = Math.min(width, height) / 2 - 60
    const angleSlice = (Math.PI * 2) / n
    const cx = width / 2, cy = height / 2

    const g = svg.append('g').attr('transform', `translate(${cx},${cy})`)

    // Grid circles
    const levels = 5
    for (let i = 1; i <= levels; i++) {
      const r = (radius / levels) * i
      g.append('circle')
        .attr('r', r)
        .attr('fill', 'none')
        .attr('stroke', '#E4E2DC')
        .attr('stroke-width', 0.5)
        .attr('stroke-dasharray', i < levels ? '2,3' : 'none')

      g.append('text')
        .attr('x', 4).attr('y', -r)
        .attr('font-size', '8px').attr('fill', '#96770B')
        .text(`${Math.round((maxValue / levels) * i)}`)
    }

    // Axis lines and labels
    axes.forEach((axis, i) => {
      const angle = angleSlice * i - Math.PI / 2
      const x = Math.cos(angle) * radius
      const y = Math.sin(angle) * radius

      g.append('line')
        .attr('x1', 0).attr('y1', 0)
        .attr('x2', x).attr('y2', y)
        .attr('stroke', '#D6D3CC').attr('stroke-width', 0.5)

      const labelX = Math.cos(angle) * (radius + 20)
      const labelY = Math.sin(angle) * (radius + 20)
      g.append('text')
        .attr('x', labelX).attr('y', labelY)
        .attr('text-anchor', 'middle')
        .attr('dominant-baseline', 'middle')
        .attr('font-size', '10px')
        .attr('font-family', 'Inter, sans-serif')
        .attr('fill', '#524E44')
        .attr('font-weight', 500)
        .text(axis.length > 14 ? axis.slice(0, 12) + '…' : axis)
    })

    // Data polygons
    const rScale = d3.scaleLinear().domain([0, maxValue]).range([0, radius])

    series.forEach(s => {
      const points = s.values.map((v, i) => {
        const angle = angleSlice * i - Math.PI / 2
        const r = rScale(v.value)
        return [Math.cos(angle) * r, Math.sin(angle) * r] as [number, number]
      })

      const line = d3.lineRadial<RadarDataPoint>()
        .radius(d => rScale(d.value))
        .angle((_, i) => i * angleSlice)
        .curve(d3.curveLinearClosed)

      // Fill polygon
      g.append('path')
        .datum(s.values)
        .attr('d', line as any)
        .attr('fill', s.color)
        .attr('fill-opacity', 0.15)
        .attr('stroke', s.color)
        .attr('stroke-width', 2)

      // Dots
      points.forEach(([x, y]) => {
        g.append('circle')
          .attr('cx', x).attr('cy', y).attr('r', 3)
          .attr('fill', s.color).attr('stroke', '#fff').attr('stroke-width', 1)
      })
    })

    // Legend
    const legend = svg.append('g').attr('transform', `translate(${width - 120}, 20)`)
    series.forEach((s, i) => {
      const lg = legend.append('g').attr('transform', `translate(0, ${i * 18})`)
      lg.append('rect').attr('width', 10).attr('height', 10).attr('rx', 2).attr('fill', s.color)
      lg.append('text').attr('x', 14).attr('y', 9).attr('font-size', '10px').attr('fill', '#2D2A24').text(s.name)
    })

  }, [series, maxValue, width, height])

  return (
    <Box>
      {title && (
        <Heading fontFamily='"Cormorant Garamond", serif' fontSize="xl" fontWeight={700} color="#2D2A24" mb={3}>
          {title}
        </Heading>
      )}
      <Box bg="white" border="1px solid" borderColor="#E4E2DC" borderRadius="lg" p={4} display="flex" justifyContent="center">
        <svg ref={svgRef} width={width} height={height} />
      </Box>
    </Box>
  )
}
