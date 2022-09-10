import React, { useEffect, useRef } from "react";
import SpollerItem from "../parts/SpollerItem";
import Breadcrumbs from "../parts/Breadcrumbs";
import "./Tariffs.scss";

function Tariffs({ setSelectedTariff, groupedByMonth }) {
	const shownBreadcrumbs = ['', 'hidden', 'hidden'];

	const spollersBlock = useRef(null);
	useEffect(() => {
		spollersBlock.current.classList.add('_spoller-init');
	});
	return (
		<div className="tariffs">
			<Breadcrumbs hidden={shownBreadcrumbs} />
			<div className="tariffs__container">
				<div ref={spollersBlock} data-spollers data-spoller-tariffs data-spollers-speed="300" className="spollers tariffs__block">

					{groupedByMonth.map(itemSpoller => (
						<SpollerItem key={itemSpoller.id} isTariff={true} setSelectedTariff={setSelectedTariff} SpollerData={itemSpoller} />
					))}

				</div>
			</div>
		</div>
	);
}

export default Tariffs;