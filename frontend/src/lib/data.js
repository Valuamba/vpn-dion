export const GROUPED_BY_MONTH_DURATION = [
	{
		id: 1, // добавил id для отрисовки списков
		month_duration: 12,
		tariffs: [
			{
				id: 1, // добавил id для отрисовки списков
				month_duration: 12,
				devices_number: 1,
				price: 1500,
				currency: "RUB",
				discount: 20,
			},
			{
				id: 2, // добавил id для отрисовки списков
				month_duration: 12,
				devices_number: 2,
				price: 2000,
				currency: "RUB",
				discount: 20,
			},
		],
	},
	{
		id: 2, // добавил id для отрисовки списков
		month_duration: 6,
		tariffs: [
			{
				id: 1, // добавил id для отрисовки списков
				month_duration: 6,
				devices_number: 1,
				price: 1500,
				currency: "RUB",
				discount: 20,
			},
			{
				id: 2, // добавил id для отрисовки списков
				month_duration: 6,
				devices_number: 2,
				price: 1700,
				currency: "RUB",
				discount: 20,
			},
			{
				id: 3, // добавил id для отрисовки списков
				month_duration: 6,
				devices_number: 3,
				price: 1500,
				currency: "RUB",
				discount: 20,
			},
			{
				id: 4, // добавил id для отрисовки списков
				month_duration: 6,
				devices_number: 4,
				price: 2500,
				currency: "RUB",
				discount: 20,
			},
		],
	},
	{
		id: 3, // добавил id для отрисовки списков
		month_duration: 3,
		tariffs: [
			{
				id: 1, // добавил id для отрисовки списков
				month_duration: 3,
				devices_number: 1,
				price: 1500,
				currency: "RUB",
				discount: 43,
			},
			{
				id: 2, // добавил id для отрисовки списков
				month_duration: 3,
				devices_number: 2,
				price: 2020,
				currency: "RUB",
				discount: 23,
			},
			{
				id: 3, // добавил id для отрисовки списков
				month_duration: 3,
				devices_number: 3,
				price: 2489,
				currency: "RUB",
				discount: 10,
			},
			{
				id: 4, // добавил id для отрисовки списков
				month_duration: 3,
				devices_number: 4,
				price: 3000,
				currency: "RUB",
				discount: 73,
			},
			{
				id: 5, // добавил id для отрисовки списков
				month_duration: 3,
				devices_number: 5,
				price: 3500,
				currency: "RUB",
				discount: 73,
			},
		],
	},
];

export const COUNTRIES = [
	{
		country: "Belarus",
		id: "BY",
		discount: 0,
	},
	{
		country: "Norway",
		id: "NW",
		discount: 56,
	},
	{
		country: "Germany",
		id: "GR",
		discount: 23,
	},
	{
		country: "Russia",
		id: "RU",
		discount: 7,
	},
	{
		country: "USA",
		id: "US",
		discount: 20,
	},
];
export const PROTOCOLS = [
	{
		protocol: "Wiregurad",
		id: 4,
	},
	{
		protocol: "OpenVpn",
		id: 5,
	},
];

export const ExtendVpnselectedTariff = {
	subscription_id: 123123,
	month_duration: 12,
	price: 2002,
	discount: 20,
	currency: "RUB",
	devicesNumber: 3,
};
export const VpnTariffState = {
	MakeAnOrder: "MakeAnOrder",
	ExtendVpnSubscription: "ExtendVpnSubscription",
};