import React, { useState } from "react";
import { BrowserRouter } from "react-router-dom";
import Main from "./components/Main";
import Preloader from "./components/UI/Preloader";
import { GROUPED_BY_MONTH_DURATION, VpnTariffState } from "./lib/data";

function App() {
	const state = VpnTariffState.MakeAnOrder; // ExtendVpnSubscription MakeAnOrder
	const [chosenTariff, setChosenTariff] = useState({});
	const setSelectedTariff = (selectedTariff) => {
		setChosenTariff(selectedTariff);
	}

	return (
		<BrowserRouter>
			<div className="wrapper">
				<Main setSelectedTariff={setSelectedTariff} groupedByMonth={GROUPED_BY_MONTH_DURATION} selectedTariff={chosenTariff} state={state} />
			</div>
			<Preloader />
		</BrowserRouter>
	);
}

export default App;
