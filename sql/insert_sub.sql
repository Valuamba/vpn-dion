select * from public.vpn_subscriptions
select * from public.vpn_devices
select * from public.bot_user

INSERT INTO public.vpn_subscriptions(
	id, month_duration, devices_number, status, is_referral, price_currency, price, discount, subscription_end, tariff_id, user_id, days_duration, reminder_state, created_at, update_at)
	VALUES ('afc74279-1a85-4424-a316-58145148ce30', 1, 1, 'paid', true, 'RUB', 4000, 20, '2022-09-29 07:18:01+00', 2, 1607078784, 22, 7, '2022-08-31 13:04:33.086293+00', '2022-08-31 13:04:33.086343+00');