import React from 'react'
import { useRoutes } from 'react-router-dom'
import Slippis from './files/slippis'
import Landing from './landing/Landing'
 

const Router = () =>{
	const routes = useRoutes([
		{
			path: '/',
			element: <Landing />
		},
		{
			path: '/slippis',
			element: <Slippis />
		}
	])

	return routes
}

export default Router