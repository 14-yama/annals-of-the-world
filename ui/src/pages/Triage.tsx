import React, { useEffect, useState } from 'react'
import {
  Table,
  Input,
  Button,
  Box,
  Text,
  HStack,
  NativeSelect
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
      <HStack mb={4}>
        <Button colorPalette="blue" onClick={download}>Download decisions (CSV)</Button>
      </HStack>
      <Table.Root>
        <Table.Header>
          <Table.Row>
            <Table.ColumnHeader>id</Table.ColumnHeader>
            <Table.ColumnHeader>slug</Table.ColumnHeader>
            <Table.ColumnHeader>file</Table.ColumnHeader>
            <Table.ColumnHeader>suggested</Table.ColumnHeader>
            <Table.ColumnHeader>action</Table.ColumnHeader>
            <Table.ColumnHeader>notes</Table.ColumnHeader>
          </Table.Row>
        </Table.Header>
        <Table.Body>
          {rows.map(r => (
            <Table.Row key={r.slug}>
              <Table.Cell>{r.id}</Table.Cell>
              <Table.Cell><Text as="span" fontFamily="mono">{r.slug}</Text></Table.Cell>
              <Table.Cell>{r.file}</Table.Cell>
              <Table.Cell>{r.suggested_action}</Table.Cell>
              <Table.Cell>
                <NativeSelect.Root size="sm">
                  <NativeSelect.Field value={(decisions[r.slug] && decisions[r.slug].decision) || ''} onChange={(e: React.ChangeEvent<HTMLSelectElement>) => onDecision(r.slug, 'decision', e.target.value)}>
                    <option value="">--</option>
                    <option value="approve">Approve</option>
                    <option value="ignore">Ignore</option>
                    <option value="needs_review">Needs review</option>
                  </NativeSelect.Field>
                </NativeSelect.Root>
              </Table.Cell>
              <Table.Cell>
                <Input size="sm" value={(decisions[r.slug] && decisions[r.slug].notes) || ''} onChange={(e: React.ChangeEvent<HTMLInputElement>) => onDecision(r.slug, 'notes', e.target.value)} />
              </Table.Cell>
            </Table.Row>
          ))}
        </Table.Body>
      </Table.Root>
    </Box>
  )
}
