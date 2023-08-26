import React from 'react'
import { useRoutes } from 'react-router-dom'
import Landing from './landing/Landing'

const Router = () =>{
	const routes = useRoutes([
		{
			path: '/',
			element: <Landing />,
			children: []
		}
	])

	return routes
}

export default Router