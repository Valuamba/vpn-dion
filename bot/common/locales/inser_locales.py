from app.common.locals import DialogDict
from app.common.models.nosql import MessageLocale


async def update_message_locales():
    db_locales = await MessageLocale.find().to_list()
    db_locales = [d.alias for d in db_locales]
    locales = []

    for k, v in DialogDict.items():
        if not k in db_locales:
            locales.append(MessageLocale(alias=k, text=v))

    if len(locales) > 0:
        await MessageLocale.insert_many(locales)


async def