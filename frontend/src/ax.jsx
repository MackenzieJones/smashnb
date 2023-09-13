import axios from 'axios'

const axiosInstance = axios.create({ baseURL: 'http://localhost:8000' })

axiosInstance.interceptors.request.use(
	(config) => {
		const bearerToken = localStorage.getItem('token')

		if (bearerToken) {
			config.headers['Authorization'] = `Bearer ${bearerToken}`
		}
		return config
	},
	(error) => {
		return Promise.reject(error)
	}
)

export default axiosInstance