from aiogram import Bot
from aiogram.fsm.context import FSMContext
# from vpn_api_client.api.api import list_vpn_countrys

from common.services.vpn_client_webapi import gettext
from handlers.menu import StateF
from handlers.menu.keyboard import InlineM
from utils.fsm.fsm_utility import dialog_info
from utils.fsm.pipeline import FSMPipeline
from utils.fsm.step_types import CallbackResponse

fsmPipeline = FSMPipeline()


async def help_info(ctx, bot: Bot, state: FSMContext, vpn_client):
    await dialog_info(ctx, bot, state, text=await gettext("menuHelp"),
                      reply_markup=await InlineM.get_help_keyboard())


async def locations_info(ctx, bot: Bot, state: FSMContext, vpn_client):
    countries = [] #await list_vpn_countrys.asyncio(client=vpn_client)
    countries_name_arr = [c.country for c in countries]

    text = (await gettext('listAvailableLocations')).format(countries='\n'.join(countries_name_arr))
    await dialog_info(ctx, bot, state, text=text,
                      reply_markup=await InlineM.get_locations_command())


async def about_info(ctx, bot: Bot, state: FSMContext, vpn_client):
    await dialog_info(ctx, bot, state, text=await gettext("about"),
                      reply_markup=await InlineM.get_help_keyboard())


def setup(prev_menu):

    fsmPipeline.set_pipeline([
        CallbackResponse(state=StateF.Help, handler=prev_menu[1],
                         information=help_info,
                         filters=[prev_menu[0]],
                         ),
        CallbackResponse(state=StateF.AvailableLocations, handler=prev_menu[1],
                         information=locations_info,
                         filters=[prev_menu[0]],
                         ),
        CallbackResponse(state=StateF.About, handler=prev_menu[1],
                         information=about_info,
                         filters=[prev_menu[0]],
                         ),
    ])