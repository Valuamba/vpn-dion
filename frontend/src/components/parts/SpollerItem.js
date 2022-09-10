import React, { useState, useRef, useEffect } from "react";
import { Link } from "react-router-dom";
import "./SpollerItem.scss";
import Block from "../UI/Block";
import Dropdown from "./Dropdown";
import InfoTariffLinkItem from "./InfoTariffLinkItem";
import { _slideUp, _slideDown } from "../../lib/functionsVPN";

function SpollerItem({ setSelectedTariff, isTariff, SpollerData, counter }) {
	const [isOpen, setIsOPen] = useState(false);
	const btnRef = useRef(null);
	const bodyRef = useRef(null);

	useEffect(() => {
		if (isOpen) {
			_slideDown(bodyRef.current, 0);
		} else {
			_slideUp(bodyRef.current, 0);
		}
	});

	const SpollerTariffBody = () => {
		return (
			<Block className="spollers__item">
				<button
					ref={btnRef}
					onClick={() => setIsOPen(prev => !prev)}
					data-spoller=""
					type="button"
					className={"spollers__title " + (isOpen ? "_spoller-active" : "")}>
					{SpollerData.month_duration + " месяцев"}
				</button>
				<div ref={bodyRef} className="spollers__body">
					<div className="info-tariffs">
						{SpollerData.tariffs.map(dataTariff => (
							<Link onClick={() => { setSelectedTariff(dataTariff); }} key={dataTariff.id} to="/devices">
								<InfoTariffLinkItem setSelectedTariff={setSelectedTariff} dataTariff={dataTariff} />
							</Link>
						))}
					</div>
				</div>
			</Block>
		);
	}

	const SpollerDevicesBody = () => {
		return (
			<Block className="spollers__item">
				<button
					ref={btnRef}
					onClick={() => setIsOPen(prev => !prev)}
					data-spoller=""
					type="button"
					className={"spollers__title " + (isOpen ? "_spoller-active" : "")}>
					Устройство {counter}
				</button>
				<div ref={bodyRef} className="spollers__body">
					<Dropdown />
					<div className="options devices__options">
						<div className="options__item">
							<input hidden="" id="o_1_1" className="options__input" type="radio" value="r_0_1" name="option1" />
							<label htmlFor="o_1_1" className="options__label">
								<span className="options__text">Wiregurad</span>
							</label>
						</div>
						<div className="options__item">
							<input hidden="" id="o_1_2" className="options__input" type="radio" value="r_1_1" name="option1" />
							<label htmlFor="o_1_2" className="options__label">
								<span className="options__text">OpenVpn</span>
							</label>
						</div>
					</div>
				</div>
			</Block>
		);
	}
	if (isTariff) {
		return <SpollerTariffBody />;
	} else {
		return <SpollerDevicesBody />;
	}
}

export default SpollerItem;

