import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react'

export default defineConfig({
  plugins: [react()],
  server: {
    port: 5173,
    open: true,
    strictPort: false,
    fs: {
      // Allow Vite to serve symlinked files in ui/public/{audit-reports,governance,enrichment}
      // which point to ../data/* (one level outside the ui/ root).
      allow: ['..'],
    },
    proxy: {
      // Local bot server — General's Command Post on port 7474
      '/local-bots': {
        target: 'http://localhost:7474',
        rewrite: (path) => path.replace(/^\/local-bots/, ''),
        changeOrigin: true,
      },
    },
  },
  appType: 'spa',
})
