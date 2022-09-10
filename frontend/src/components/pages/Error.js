import React from "react";
import "./PaymentStatus.scss";

function Error() {
	return (
		<div className="page-status error">
			<div className="page-status__block error">
				<div className="page-status__icon error">
					<span className="_icon-close"></span>
				</div>
				<h1 className="page-status__text">Оплата не прошла</h1>
			</div>
			<button data-close-web-app className="page-status__btn error">Ок</button>
		</div>
	);
}

export default Error;