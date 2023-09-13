import React, { ReactDOM } from 'react'
import logo from './logo.svg'
import './App.css'
import { useRoutes, BrowserRouter, Routes, Route } from "react-router-dom"
import Router from './routes'

function App() {
	return (
		<BrowserRouter>
			<Router />
		</BrowserRouter>
	) 
}

export default App
