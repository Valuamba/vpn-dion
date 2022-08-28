from common.services.vpn_client_webapi import send_get, send_post


async def get_user_referral_data(user_id, vpn_client):
    result = await send_get(vpn_client, f'bot_user/referral/{user_id}')
    return result.parsed
    # return {
    #     'count_referrals': 4,
    #     'count_free_month_subscription': 2,
    #     'referral_link': 'https://t.me/FCK_RKN_bot?start=ref37207531d0a1'
    # }


async def activate_free_month_subscription(user_id, vpn_client):
    result = await send_post(vpn_client, f'subscription/create-referral-subscription', json_body={
        'user_id': user_id,
        'month_duration': 1
    })
    return result.parsed