import axiosInstance from 'ax'
import { API_URL } from 'src/env'


export const getEvents = (
	fromDate,
	toDate,
	region,
	searchString,
	skip,
	limit
) => {
	const params = {
		fromDate: fromDate,
		toDate: toDate,
		region: region,
		searchString: searchString,
		skip: skip,
		limit: limit
	}

	axiosInstance.get(`${API_URL}/events`, params)
	.then((res) => {
		console.log('Success', res.data)
	})
}