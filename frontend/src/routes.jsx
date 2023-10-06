import React from 'react'
import { useRoutes } from 'react-router-dom'
import Slippis from './files/slippis'
import Landing from './landing/Landing'
import Login from './auth/login'
 

const Routes = () =>{
	const routes = useRoutes([
		{
			path: '/',
			element: <Landing />
		},
		{
			path: '/login',
			element: <Login />
		},
		{
			path: '/slippis',
			element: <Slippis />
		}
	])

	return routes
}

export default Routes