SELECT c.pkid, place, discount_percentage, is_default FROM public.vpn_countries as c 
INNER JOIN public.vpn_instances as i on country_id = c.pkid
WHERE i.is_online=True
GROUP BY c.pkid, place, discount_percentage
		

SELECT * FROM public.vpn_instances
select * from public.bot_user		
		
SELECT p.pkid, p.protocol, p.is_default FROM public.vpn_protocols as p
INNER JOIN public.vpn_instances_protocols ON vpn_instances_protocols.vpnprotocol_id = p.pkid 
INNER JOIN public.vpn_instances vpn_instances2 ON vpn_instances2.pkid = vpn_instances_protocols.vpninstance_id
WHERE vpn_instances2.is_online=True
GROUP BY p.pkid, protocol


SELECT c.pkid, place, discount_percentage, is_default FROM public.vpn_countries as c 
INNER JOIN public.vpn_instances as i on country_id = c.pkid
WHERE i.is_online=True
GROUP BY c.pkid, place, discount_percentage


DECLARE @user_id CONSTANT integer := 395040322;

DELETE FROM public.vpn_items
USING public.vpn_subscriptions
WHERE vpn_items.vpn_subscription_id = vpn_subscriptions.pkid and vpn_subscriptions.user_id <> @user_id;

delete from public.vpn_subscriptions as s
where s.user_id <> 395040322

delete from public.referral_items

delete from public.bot_user as u
where u.user_id <> 395040322

select * from public.vpn_items