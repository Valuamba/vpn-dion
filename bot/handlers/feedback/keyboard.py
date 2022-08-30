from common.keyboard.utility_keyboards import NavCD, NavType
from common.services.vpn_client_webapi import gettext
from utils.markup_constructor import InlineMarkupConstructor


class FeedbackMarkup(InlineMarkupConstructor):

    async def get_feedback_keyboard(self):
        cancel = await gettext('cancel')
        actions = [
            {'text': cancel, 'callback_data': NavCD(type=NavType.BACK).pack()}
        ]
        return self.markup(actions, [1])

    async def get_success_keyboard(self):
        cancel = await gettext('backToMenu')
        actions = [
            {'text': cancel, 'callback_data': NavCD(type=NavType.BACK).pack()}
        ]
        return self.markup(actions, [1])


InlineM = FeedbackMarkup()