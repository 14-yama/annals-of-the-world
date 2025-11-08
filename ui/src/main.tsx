import React from 'react'
import { createRoot } from 'react-dom/client'
// Chakra UI v3 minimal setup using system preset
import { ChakraProvider, Theme } from '@chakra-ui/react'
import App from './App'
import system from './theme'

const root = createRoot(document.getElementById('root')!)
root.render(
  <React.StrictMode>
  {/* Provide the concrete system value from ./theme */}
  <ChakraProvider value={system}>
      {/* Theme wrapper applies background + fg tokens */}
      <Theme appearance="light">
        <App />
      </Theme>
    </ChakraProvider>
  </React.StrictMode>
)
