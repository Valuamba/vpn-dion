import React from "react";
import "./Block.scss";

function Block({ children, className }) {
	const classes = "block " + className;
	return (
		<div className={classes}>{children}</div>
	);
}

export default Block;