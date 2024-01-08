import React, { useEffect, useRef, useState } from 'react'
import 'src/styles/common-styles.css'
import { getEvents } from 'src/requests/EventRequests'
import Text from 'components/simple/Text'
import { Sheet } from '@mui/joy'


const Landing = () => {
	const [events, setEvents] = useState([])
	
	const EventElement = (event) => {
		if (!event && !event?.name) {
			return <Text> something broke with this event </Text>
		}
		return (
			<Sheet className='flex' style={{ height: '200px', width: '500px' }}>
				<Text>{event.name}</Text>
				{event.bracket && (<Text>{event.bracket}</Text>)}
				{event.stream && (<Text>{event.stream}</Text>)}
				{event.numAttendees && (<Text>{event.numAttendees}</Text>)}
			</Sheet>
		)
	}

	useEffect(() => {
		setEvents(getEvents())
	})

	return (
		<div className='full flex flex-col justify-center align-center'>
			<h1>
				SmashNB I guess
			</h1>

			<div className='flex'>
				<EventElement event={{name: 'asd'}} />
			</div>
		</div>
	)
}

export default Landing