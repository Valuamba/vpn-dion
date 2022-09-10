import React, { useState } from "react";
import "./Checkbox.scss";

function Checkbox({ isAllow }) {
	const [checked, setChecked] = useState(false);
	const allowPaymentHanlder = () => {
		setChecked(prev => !prev);
		isAllow(checked);
	}

	return (
		<div className="checkbox">
			<input onChange={allowPaymentHanlder} id="c_1" className="checkbox__input" type="checkbox" />
			<label htmlFor="c_1" className="checkbox__label">
				<span className="checkbox__text">
					Я согласен с условиями оферты рекуррентных платежей и политики обработки
					персональных данных
				</span>
			</label>
		</div>
	);
}

export default Checkbox;