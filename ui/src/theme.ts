/*
 * Annals of the World — "Marble & Antiquity" Theme
 * The Library of Alexandria — White Stone, Roman Letters, Golden Accents
 */
import { createSystem, defaultConfig, defineConfig } from '@chakra-ui/react'

const config = defineConfig({
  theme: {
    tokens: {
      colors: {
        marble: {
          50:  { value: '#FAFAF8' },
          100: { value: '#F5F4F0' },
          200: { value: '#EEEDEA' },
          300: { value: '#E4E2DC' },
          400: { value: '#D6D3CC' },
          500: { value: '#C4C0B7' },
          600: { value: '#9E9A90' },
          700: { value: '#787469' },
          800: { value: '#524E44' },
          900: { value: '#2D2A24' },
        },
        gold: {
          50:  { value: '#FBF7EC' },
          100: { value: '#F3EAD0' },
          200: { value: '#E8D6A8' },
          300: { value: '#DCC07D' },
          400: { value: '#D4AF37' },
          500: { value: '#C9A84C' },
          600: { value: '#B8920E' },
          700: { value: '#96770B' },
          800: { value: '#745C09' },
          900: { value: '#4A3A06' },
        },
        empire: {
          50:  { value: '#F9F0F0' },
          100: { value: '#E8CECE' },
          200: { value: '#D4A5A5' },
          300: { value: '#C08080' },
          400: { value: '#A45A5A' },
          500: { value: '#8B3A3A' },
          600: { value: '#712D2D' },
          700: { value: '#5A2222' },
          800: { value: '#3D1717' },
          900: { value: '#200C0C' },
        },
        stone: {
          50:  { value: '#F8F6F0' },
          100: { value: '#EDE9DF' },
          200: { value: '#E0DCD2' },
          300: { value: '#D1CCC0' },
          400: { value: '#B8B2A4' },
          500: { value: '#9E9788' },
          600: { value: '#817A6C' },
          700: { value: '#645E52' },
          800: { value: '#47423A' },
          900: { value: '#2A2722' },
        },
        cosmos: {
          50:  { value: '#EEF2FA' },
          100: { value: '#C8D6F0' },
          200: { value: '#A2BAE6' },
          300: { value: '#7C9EDB' },
          400: { value: '#5682D1' },
          500: { value: '#3B6BC2' },
          600: { value: '#2F569E' },
          700: { value: '#23417A' },
          800: { value: '#182C56' },
          900: { value: '#0C1832' },
        },
      },
      fonts: {
        heading: { value: '"Cormorant Garamond", Georgia, serif' },
        body:    { value: '"Inter", system-ui, sans-serif' },
        mono:    { value: '"JetBrains Mono", monospace' },
        display: { value: '"Cinzel", "Cormorant Garamond", serif' },
      },
    },
  },
})

const system = createSystem(defaultConfig, config)

export default system
