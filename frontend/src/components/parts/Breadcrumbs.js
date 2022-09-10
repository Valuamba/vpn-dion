import React from "react";
import "./Breadcrumbs.scss";
import { Link } from "react-router-dom";

function Breadcrumbs({ hidden, onlyInvoiceOpen }) {
	return (
		<nav className="controls">
			<ul className="controls__container content__container">
				<Link to="/tariffs" className={hidden[0] + (onlyInvoiceOpen ? 'hidden' : "")}><li className={"controls__item btn-tariffs "}>Тарифы</li></Link>
				<Link to="/devices" className={hidden[1] + (onlyInvoiceOpen ? 'hidden' : "")}><li className={"controls__item btn-tariffs "}>Устройства</li></Link>
				<Link to="/invoice" className={hidden[2]}><li className={"controls__item btn-tariffs "}>Оплата </li></Link>
			</ul>
		</nav>
	);
}

export default Breadcrumbs;
