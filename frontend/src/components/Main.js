import React from "react";
import Tariffs from "./pages/Tariffs";
import Devices from "./parts/Devices";
import Invoice from "./pages/Invoice";
import Success from "./pages/Success";
import Error from "./pages/Error";
import { Routes, Route } from "react-router-dom";
import { ExtendVpnselectedTariff } from "../lib/data";

function Main({ setSelectedTariff, groupedByMonth, selectedTariff, state }) {

	switch (state) {
		case 'MakeAnOrder':
			return (
				<div className="main">
					<Routes>
						<Route path="/tariffs" element={<Tariffs groupedByMonth={groupedByMonth} setSelectedTariff={setSelectedTariff} />} />
						<Route path="/devices" element={<Devices selectedTariff={selectedTariff} />} />
						<Route path="/invoice" element={<Invoice selectedTariff={selectedTariff} />} />

						<Route path="/success" element={<Success />} />
						<Route path="/error" element={<Error />} />
					</Routes>
				</div>
			);
		case 'ExtendVpnSubscription':
			return (
				<div className="main">
					<Routes>
						<Route path="/invoice" element={<Invoice selectedTariff={ExtendVpnselectedTariff} onlyInvoiceOpen={true} />} />

						<Route path="/success" element={<Success />} />
						<Route path="/error" element={<Error />} />
					</Routes>
				</div>
			);
		default:
	}

	// if (state === 'MakeAnOrder') {
	// 	return (
	// 		<div className="main">
	// 			<Routes>
	// 				<Route path="/tariffs" element={<Tariffs groupedByMonth={groupedByMonth} setSelectedTariff={setSelectedTariff} />} />
	// 				<Route path="/devices" element={<Devices />} />
	// 				<Route path="/invoice" element={<Invoice selectedTariff={selectedTariff} />} />
	// 			</Routes>
	// 		</div>
	// 	);
	// }
	// return (
	// 	<div className="main">
	// 		<Routes>
	// 			<Route path="/invoice" element={<Invoice selectedTariff={ExtendVpnselectedTariff} />} />
	// 		</Routes>
	// 	</div>
	// );
}

export default Main;