import uuid


def build_referral_value(*, user_id: int):
    return 'ref' + str(user_id)[:-4] + str(uuid.uuid4())[:4]