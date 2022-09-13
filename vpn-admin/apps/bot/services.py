from django.db import transaction

from apps.bot.models import Message, BotUser, ReferralItem
from apps.bot.selectors import get_user_by_referral, get_user_by_id
from lib.str_utils import build_referral_value


def add_feedback_message(*, user_id: int, message_id: int, text: str) -> Message:
    message = Message.objects.create(
        consumer_id=user_id,
        message_id=message_id,
        text=text
    )
    return message


@transaction.atomic()
def add_bot_user(*, user_id: int, user_name: str, first_name: str, last_name: str, referral_value=None):
    new_user = BotUser.objects.create(
        user_id=user_id,
        user_name=user_name,
        first_name=first_name,
        last_name=last_name,
        referral_value=build_referral_value(user_id=user_id)
    )

    if referral_value:
        referral_owner = get_user_by_referral(referral_value=referral_value)
        referral_item = ReferralItem.objects.create(
            referral_owner_id=referral_owner.user_id,
            referred_user_id=new_user.user_id,
            is_activated_reward=False
        )
        # logger.info(
        #     f'Add new user {new_user.user_id} with referral {referral_owner.user_id}' if referral_id else f'Add new user {new_user.user_id}'
        #     )

    return new_user


def update_user(*, user_id, user_name: str, first_name: str, last_name: str, referral_value=None):
    user = get_user_by_id(user_id=user_id)

    user.user_name = user_name
    user.first_name = first_name
    user.last_name = last_name

    if not user.referral_item and referral_value:
        referral_owner = BotUser.objects.get(referral_value=referral_value)
        referral_id = ReferralItem.objects.create(
            referral_owner_id=referral_owner.user_id,
            referred_user_id=user.user_id,
            is_activated_reward=False
        )
        # logger.info(f'Add referral {referral_id} of user {user_id}')

    user.save()

