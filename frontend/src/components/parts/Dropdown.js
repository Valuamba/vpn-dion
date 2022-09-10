import React, { useState, useRef, useEffect } from "react";
import "./Dropdown.scss";
import { COUNTRIES } from "../../lib/data";

function Dropdown() {
	const [isClosed, setIsClosed] = useState(true);
	const dropdownRef = useRef(null);

	useEffect(() => {
		const closeMenu = e => {

		};

		document.body.addEventListener('click', closeMenu);

		return () => document.body.removeEventListener('click', closeMenu);
	}, []);

	return (
		<div ref={dropdownRef} className={"devices__dropdown " + (isClosed ? 'closed' : "")}>
			<h2 onClick={() => setIsClosed(prev => !prev)} className="devices__dropdown-title" value="">Выберите страну</h2>
			<ul className="devices__dropdown-list">
				{COUNTRIES.map((country) => (
					<li key={country.id} className="devices__dropdown-item">{country.country}</li>
				))}
			</ul>
		</div>
	);
}

export default Dropdown;