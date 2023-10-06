import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import env from './src/env'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      'src': resolve(__dirname, 'src'),
      'ax': resolve(__dirname, 'src/ax.jsx')
    }
  },
  server: {
    port: 3000,
    host: '127.0.0.1'
  }
})
