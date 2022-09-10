import React from "react";
import "./MainButton.scss";

function MainButton({ children, className }) {
	const classes = "main-button green " + className;
	return (
		<div className={classes}>{children}</div>
	);
}


export default MainButton;