from django.conf import settings

from apps.bot.exceptions import BotUserNotFound
from apps.bot.models import BotMessageLocale, BotUser


def get_locale(*, alias: str) -> str:
    locale = BotMessageLocale.objects.get(alias=alias)
    return locale.text


def bulk_get_locales(*, aliases: [str]) -> [str]:
    if not aliases or len(aliases) == 0:
        raise Exception("There is no alias field.")
    locales = {}
    for alias in aliases:
        try:
            locale = BotMessageLocale.objects.get(alias=alias)
            locales[locale.alias] = locale.text
        except BotMessageLocale.DoesNotExist:
            raise Exception(f"Locale {alias} doesn't exist")

    return locales


def get_user_by_id(*, user_id: int):
    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound
    return user


def get_user_by_referral(*, referral_value):
    try:
        referral_owner = BotUser.objects.get(referral_value=referral_value)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    return referral_owner


def get_referral_data(*, user_id):
    try:
        user = BotUser.objects.get(user_id=user_id)
    except BotUser.DoesNotExist:
        raise BotUserNotFound

    referrals_count = user.referrals.raw(f'''
               select r.* from referral_items as r
                WHERE referral_owner_id={user_id} and r.referred_user_id IN (
    				SELECT sub.user_id FROM vpn_subscriptions as sub
    				WHERE sub.status = 'paid' and sub.is_referral = false
    				GROUP BY sub.user_id  
    				HAVING COUNT(*) > 0
    			)
            '''
                                         )

    free_referrals_count = user.referrals.raw(f'''
                   select r.* from referral_items as r
                        WHERE referral_owner_id={user_id} and r.referred_user_id IN (
                            SELECT sub.user_id FROM vpn_subscriptions as sub
                            WHERE sub.status = 'paid' and sub.is_referral = false
                            GROUP BY sub.user_id  
                            HAVING COUNT(*) > 0
                        )
                        and is_activated_reward=false
                    '''
                                              )

    data = {
        'referral_link': f'https://t.me/{settings.BOT_USER_NAME}?start={user.referral_value}',
        'count_referrals': referrals_count,
        'count_free_month_subscription': free_referrals_count
    }

    return data
