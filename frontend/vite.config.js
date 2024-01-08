import { defineConfig } from 'vite'
import react from '@vitejs/plugin-react-swc'
import { resolve } from 'path'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [react()],
  resolve: {
    alias: {
      'src': resolve(__dirname, 'src'),
      'ax': resolve(__dirname, 'src/ax.jsx'),
      'components': resolve(__dirname, 'src/components')
    }
  },
  server: {
    port: 3000,
    host: '127.0.0.1'
  }
})
