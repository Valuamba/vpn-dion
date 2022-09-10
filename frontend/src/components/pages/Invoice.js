import React, { useRef } from "react";
import Breadcrumbs from "..//parts/Breadcrumbs";
import MainButton from "../UI/MainButton";
import Discount from "../UI/Discount";
import Checkbox from "../UI/Checkbox";
import "./Invoice.scss";

function Invoice({ selectedTariff, onlyInvoiceOpen }) {
	const shownBreadcrumbs = ['', '', ''];

	const mainBtnRef = useRef(null);

	const isAllow = () => {
		if (mainBtnRef.current.classList.contains('locked')) {
			mainBtnRef.current.classList.remove('locked');
		} else {
			mainBtnRef.current.classList.add('locked');
		}
	}
	const month_duration = selectedTariff.month_duration;
	const devices_number = selectedTariff.devices_number;
	const result_price = selectedTariff.price;
	const currency = selectedTariff.currency;
	const discount = selectedTariff.discount;
	return (
		<div className="payment">
			<Breadcrumbs hidden={shownBreadcrumbs} onlyInvoiceOpen={onlyInvoiceOpen} />
			<div className="payment__container">
				<div className="payment__block">
					<h2 className="payment__title">Доступ к VPN на {month_duration} месяцев.</h2>
					<div className="payment__info-content">
						<div className="payment__info">
							<div className="payment__currency">
								<div className="payment__initial">{result_price} {currency}</div>
							</div>
							<div className="payment__mon">{month_duration} месяцев</div>
							<div className="payment__devices">{devices_number} устройств</div>
							<Discount>{discount}%</Discount>
						</div>
					</div>
					<Checkbox isAllow={isAllow} />
				</div>
			</div>
			<MainButton className={'transparent'}>
				<a ref={mainBtnRef} className={"locked"} href="https://pay.freekassa.ru/?m=21411&oa=1000&currency=RUB&o=123&s=5571cc611760840c125878986150f68b">К оплате</a>
			</MainButton>
		</div>
	);
}

export default Invoice;