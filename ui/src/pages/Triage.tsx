import React, { useEffect, useState } from 'react'
import {
  Table,
  Thead,
  Tbody,
  Tr,
  Th,
  Td,
  Select,
  Input,
  Button,
  Box,
  Text,
  Stack
} from '@chakra-ui/react'

type OrphanRow = {
  cluster: string
  file: string
  id: string
  slug: string
  suggested_action: string
}

function parseCSV(text: string): OrphanRow[] {
  const lines = text.split(/\r?\n/).filter(Boolean)
  if (!lines.length) return []
  const headers = lines[0].split(',').map(h => h.replace(/\"/g, '').trim())
  const rows: OrphanRow[] = []
  for (let i = 1; i < lines.length; i++) {
    const cols = lines[i].split(',')
    const obj: any = {}
    for (let j = 0; j < headers.length; j++) {
      obj[headers[j]] = (cols[j] || '').replace(/^"|"$/g, '')
    }
    rows.push(obj as OrphanRow)
  }
  return rows
}

export default function Triage() {
  const [rows, setRows] = useState<OrphanRow[]>([])
  const [decisions, setDecisions] = useState<Record<string, {decision: string; notes: string}>>({})

  useEffect(() => {
    const url = (import.meta as any).env?.VITE_ORPHAN_CSV_URL || '/data/orphan_nodes.csv'
    fetch(url)
      .then(r => r.text())
      .then(txt => setRows(parseCSV(txt)))
      .catch(() => setRows([]))
  }, [])

  const onDecision = (slug: string, key: string, value: string) => {
    setDecisions(prev => ({ ...prev, [slug]: { ...(prev[slug] || {decision: '', notes: ''}), [key]: value } }))
  }

  const download = () => {
    const header = ['cluster','file','id','slug','suggested_action','decision','notes']
    const lines = [header.join(',')]
    rows.forEach(r => {
      const d = decisions[r.slug] || {decision: '', notes: ''}
      const esc = (v: any) => '"' + String(v || '').replace(/"/g, '""') + '"'
      lines.push([r.cluster, r.file, r.id, r.slug, r.suggested_action, d.decision, d.notes].map(esc).join(','))
    })
    const blob = new Blob([lines.join('\n')], { type: 'text/csv;charset=utf-8;' })
    const url = URL.createObjectURL(blob)
    const a = document.createElement('a')
    a.href = url
    a.download = 'orphan_triage_decisions.csv'
    a.click()
    URL.revokeObjectURL(url)
  }

  return (
    <Box>
      <Stack direction="row" spacing={4} mb={4}>
        <Button colorScheme="blue" onClick={download}>Download decisions (CSV)</Button>
      </Stack>
      <Table>
        <Thead>
          <Tr>
            <Th>id</Th>
            <Th>slug</Th>
            <Th>file</Th>
            <Th>suggested</Th>
            <Th>action</Th>
            <Th>notes</Th>
          </Tr>
        </Thead>
        <Tbody>
          {rows.map(r => (
            <Tr key={r.slug}>
              <Td>{r.id}</Td>
              <Td><Text as="code">{r.slug}</Text></Td>
              <Td>{r.file}</Td>
              <Td>{r.suggested_action}</Td>
              <Td>
                <Select size="sm" value={(decisions[r.slug] && decisions[r.slug].decision) || ''} onChange={e => onDecision(r.slug, 'decision', e.target.value)}>
                  <option value="">--</option>
                  <option value="approve">Approve</option>
                  <option value="ignore">Ignore</option>
                  <option value="needs_review">Needs review</option>
                </Select>
              </Td>
              <Td>
                <Input size="sm" value={(decisions[r.slug] && decisions[r.slug].notes) || ''} onChange={e => onDecision(r.slug, 'notes', e.target.value)} />
              </Td>
            </Tr>
          ))}
        </Tbody>
      </Table>
    </Box>
  )
}
