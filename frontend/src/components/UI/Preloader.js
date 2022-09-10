import React from "react";
import "./Preloader.scss";

function Preloader() {
	return (
		<div className="preloader">
			<div className="lds-facebook">
				<div></div>
				<div></div>
				<div></div>
			</div>
		</div>
	);
}

export default Preloader;