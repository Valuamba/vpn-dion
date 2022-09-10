import React from "react";
import { Link } from "react-router-dom";
import SpollerItem from "./SpollerItem";
import MainButton from "../UI/MainButton";
import Breadcrumbs from "./Breadcrumbs";

function Devices({ selectedTariff }) {
	let listItems = [];
	for (let i = 0; i < selectedTariff.devices_number; i++) {
		listItems.push(`item ${i}`);
	}

	const shownBreadcrumbs = ['', '', 'hidden'];

	return (
		<div className="devices">
			<Breadcrumbs hidden={shownBreadcrumbs} />
			<div className="devices__container content__container">
				<div data-spollers="" data-spoller-devices="" data-spollers-speed="300" className="spollers devices__block _spoller-init">
					{listItems.map((elem, i) => (
						<SpollerItem key={listItems[i]} SpollerData={selectedTariff} counter={i + 1} />
					))}
				</div>
				<div className="devices__add"></div>
			</div>
			<MainButton>
				<Link to='/invoice'>К оплате</Link>
			</MainButton>
		</div>
	);
}

export default Devices;