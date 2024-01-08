import { Typography } from "@mui/joy"
import { forwardRef } from "react"

const Text = forwardRef((props, ref) => {

	const defaultProps = {
		variant: "soft"
	}

	props = {...defaultProps, ...props}

	return (
		<Typography
			ref={ref}
			{...props}
		> {props.children}</Typography>
	)
})

Text.propTypes = {...Typography.propTypes}

export default Text
