import React from "react";
import "./Discount.scss";

function Discount({ children }) {
	return (
		<span className="discount">{children}</span>
	);
}

export default Discount;