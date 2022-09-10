import React from "react";
import "./PaymentStatus.scss";

function Success() {
	return (
		<div className="page-status success">
			<div className="page-status__block success">
				<div className="page-status__icon success">
					<span className="_icon-check"></span>
				</div>
				<h1 className="page-status__text">Оплата прошла успешно</h1>
			</div>
			<button data-close-web-app className="page-status__btn success">Ок</button>
		</div>
	);
}

export default Success;
