import React, { useEffect, useState } from 'react'
import { box } from '../landing/styles'
import '../styles/common-styles.css'
import axios from 'axios'

const Slippis = () => {
	const [files, setFiles] = useState([])
	
	useEffect(() => {
		fetchFiles()
	})

	const fetchFiles = () => {
		axios.get('localhost:8000/files-ls').then((res) => {
			let fakeData = [
				{
					name: 'slippifile1.slp'
				},
				{
					name: 'slippert.slp'
				}
			]
			setFiles(fakeData)
		}).catch((err) => {
			let fakeData = [
				{
					name: 'slippifile1.slp'
				},
				{
					name: 'slippert.slp'
				}
			]
			setFiles(fakeData)
		})
	}

	const fileRow = (file) => {
		return (
			<div>
				{ file.name }
			</div>
		)
	}

	return (
		<div className='full flex justify-center align-center'>
			<div className='full flex-col' style={{...box, paddingTop: '50px'}}>
				<div className='flex justify-center'>files!</div>
				<div className='w-full flex'>
					{
						files.map((file) => fileRow(file))
					}
				</div>
			</div>
		</div>
	)
}

export default Slippis