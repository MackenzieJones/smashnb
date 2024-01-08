const path = require('path')

module.exports = function override(config, env) {
  // Add an alias for axios
  config.resolve.alias = {
    ...config.resolve.alias,
    ax: path.resolve(__dirname, 'src/ax.jsx'),
    components: path.resolve(__dirname, 'src/components/simple'),
  }

  return config
}
