import React from 'react'
import { Box, Container, Heading } from '@chakra-ui/react'
import Demo from './pages/Demo'

export default function App() {
  return (
    <Container maxW="container.lg" py={6}>
      <Heading mb={4}>Annals — Orphan Nodes Triage</Heading>
      <Box>
        <Demo />
      </Box>
    </Container>
  )
}
