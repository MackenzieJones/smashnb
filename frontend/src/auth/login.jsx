import { useNavigate, useLocation } from "react-router"
import { useState } from "react"
import useAuth from "./useAuth"
import '../styles/common-styles.css'
import axios from 'ax'



const Login = () => {
	const navigate = useNavigate()

	const location = useLocation()
	const from = location.state?.from?.pathname
	const { auth, setAuth } = useAuth()
	const [error, setError] = useState("")

	const handleSubmit = async (e) => {
		e.preventDefault()
		const username = e.target.elements.email.value
		const password = e.target.elements.password.value
		try {
			const res = await axios.post("/token", {
				username,
				password
			}, {
				headers: {
					'Content-Type': 'multipart/form-data'
				}
			}).then((res) => {
				if (res?.data?.access_token) {
					const role = res?.data.role
					setAuth({ role: `${role}`, name: `${username}` })
					localStorage.setItem('token', res.data.access_token)

					if (from) {
						navigate(from, { replace: true })
					} else {
						navigate('/')
					}
				} else {
					setError(res.message)
				}
			})
		} catch (err) {
			console.log(err)
		}
	}


	return (
		<div>
			<form onSubmit={handleSubmit}>
				<div className="flex-col" style={{ width: '300px', padding: '1rem' }}>
					<div style={{ width: '300px' }}> login </div>

					<label for="email">email</label>
					<input type="text" id="email" name="email"/>

					<label for="password">password</label>
					<input type="password" id="password" name="password"/>

					<input type="submit" value="Submit" style={{ width: '100px' }}/>
				</div>
			</form>
		</div>
	)
}

export default Login