import React from 'react'
import { Box, Heading, Text } from '@chakra-ui/react'

// Minimal embedded demo node for a well-known person already present in the data.
const demoNode = {
  id: 3,
  slug: 'henry_viii',
  title: 'Henry VIII',
  type: 'Person',
  description: 'King of England (1509–1547). Central figure in the English Reformation.',
  governance: {
    status: 'APPROVED',
    workflow_stage: 'final'
  }
}

export default function Demo() {
  return (
    <Box mb={6} p={4} borderWidth={1} borderRadius="md">
      <Box display="flex" justifyContent="space-between" alignItems="center">
        <Heading size="md">Demo: Node preview</Heading>
        <Box as="span" bg="green.500" color="white" px={2} py={1} borderRadius="md" fontSize="sm">Read-only</Box>
      </Box>
      <Box mt={3}>
        <Heading size="sm">{demoNode.title} <Text as="span" fontSize="sm" color="gray.600">({demoNode.slug})</Text></Heading>
        <Text mt={2}>{demoNode.description}</Text>
        <Text mt={2} fontSize="sm" color="gray.600">Type: {demoNode.type} • Status: {demoNode.governance.status}</Text>
      </Box>
    </Box>
  )
}
