from app.branches import user_auth, profile
from app.branches.profile import locals as profile
from app.branches.account_procedure import locals as account_procedure
from app.branches.admin.get_checks import get_checks_locals
from app.branches.user_auth import locals as user_auth_local
from app.branches.check import locals as check
from app.branches.admin import locals as admin
from app.branches.admin.check import check_locals

DialogDict = {}
locals = [user_auth_local, check, admin, check_locals, get_checks_locals, account_procedure, profile]

InlineCommon = {
    'back': 'Назад'
}

DialogCondition = {
    'true': 'да',
    'false': 'нет'
}

Common = {
    'user': '<a href="tg://user?id=%s">%s</a>'
}

NotifyLocals = {
    'checkWasCreated': 'Пользователь, %s, добавил чек %s.\n'
                       'Необходимо подтвердить проверку фотографии и получение оригинала.',
    'checkPhotoWasConfirmed': 'Фото чека %s было подтверждено ответственным %s.\n'
                              'Баллов начисленно: %s',
    'checkPhotoWasDeclined': 'Фото чека %s было отклонено ответственным %s.\n'
                             'Комментарий: %s',
    'givingOriginalWasConfirmed': 'Получение оригинала чека %s было подтверждено ответственным %s.\n'
                                  'Баллов начисленно: %s',
    'givingOriginalWasDeclined': 'Получение оригинала чека %s было отклонено ответственным %s.\n'
                                 'Комментарий: %s',
    'userRoleWasChanged': 'Администратор изменил вашу роль. Теперь вы: %s',
    'adminBlockUser': 'Администратор %s вас.',
}



for local in locals:
    for k, v in local.build_locale().items():
        DialogDict[k] = v

    for k, v in InlineCommon.items():
        DialogDict['inline.%s' % k] = v

    for k, v in DialogCondition.items():
        DialogDict['dialog.%s' % k] = v

    for k, v in NotifyLocals.items():
        DialogDict['notify.%s' % k] = v

    for k, v in Common.items():
        DialogDict['common.%s' % k] = v
