// Minimal safe theme/system for Chakra UI v3
// Export a concrete system object to pass into <ChakraProvider value={...}>
import { defaultSystem } from '@chakra-ui/react'

// Keep this deliberately small and non-invasive. We provide a concrete
// system object (based on Chakra's defaultSystem) and tweak only the
// color mode config so it behaves predictably in the demo.
const system: any = {
  ...defaultSystem,
  _config: {
    // preserve any existing config while ensuring sensible defaults
    ...((defaultSystem as any)?._config),
    initialColorMode: 'light',
    useSystemColorMode: false,
  },
}

export default system
// (removed previous legacy extendTheme usage)
