import React, { } from "react";
import "./InfoTariffLinkItem.scss";
import Discount from "../UI/Discount";

function InfoTariffLinkItem({ dataTariff }) {
	const month_duration = dataTariff.month_duration;
	const devices_number = dataTariff.devices_number;
	const result_price = dataTariff.price;
	const currency = dataTariff.currency;
	const discount = dataTariff.discount;
	return (
		<div className="info-tariffs__item">
			<h2 className="mon-count">{month_duration}</h2>
			<h2 className="mon-text">месяцев</h2>
			<h2 className="subscription">подписки</h2>
			<h3 className="devices-number"><span>{devices_number}</span> устройство</h3>
			<h3 className="price">{result_price} {currency}</h3>
			<Discount className="discount">{discount}%</Discount>
		</div>
	);
}

export default InfoTariffLinkItem;