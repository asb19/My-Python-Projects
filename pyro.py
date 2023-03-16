from pyrogram import Client, filters

from pyrogram.types import (
    Message,
    Poll,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    CallbackQuery,
)
import time

api_id = 5425925404
api_hash = "7341006429668092470"
bot_token = "5425925404:AAEsxH74d2umN2c5-4rwzd_IwWFS11_csNE"



# app = Client(
#     "amir",
#     api_id=api_id, api_hash=api_hash
# )

app = Client(
    "cp_fk_bot",
    api_id=api_id, api_hash=api_hash,
    bot_token=bot_token
)

async def main():
    async with app:
        print(await app.get_me())
        # c=await app.get_chat_members(chat_id=-1001562893392)
        # async for i in app.get_chat_members(chat_id=-1001562893392):
        #     print(i)
        count=0
        # while True:
        #     links = []
        #     for i in range(20):
        #         link = await app.create_chat_invite_link(chat_id=-1001655847278, member_limit=1)
        #         print(link)
        #         links.append(link)
        #         count=count+1
        #         print(count)
        #     time.sleep(5)

        #     for i in links:
        #         expire = await app.revoke_chat_invite_link(chat_id=-1001655847278, invite_link=i.invite_link)
        #         print(expire)
        #         count+=1
        #         print(count)
        #     time.sleep(30)

        # x = await app.add_chat_members(chat_id=-1001562893392, user_ids=[5515533637])
        non_anonymous_poll = filters.create(
            lambda *_: _[2].poll is not None and not _[2].poll.is_anonymous
                )

        forwardchannel = -1001726846911
        startmsg: str = """
        start message
        """


        @app.on_message(filters.command("start") & filters.private)
        async def start(client, message):
            await message.reply(
                startmsg,
            )


        @app.on_message(
            ~filters.service
            & ~filters.game
            & ~filters.channel
            & ~filters.linked_channel
            & ~non_anonymous_poll
        )
        async def viewcounter(client, message):
            forward = await message.forward(forwardchannel)
            await forward.forward(message.chat.id)
            await forward.delete()


        @app.on_message(
            (filters.service | filters.game | filters.channel | non_anonymous_poll)
        )
        async def notsupported(client, message):
            await message.reply(
                "sorry but this type of message not supported (non anonymous polls or games (like @gamebot or @gamee) or message from channels or service messages)",
                reply_markup=InlineKeyboardMarkup(
                    [[InlineKeyboardButton("delete this message", "deleterrormessage")]]
                ),
            )


        @app.on_callback_query(filters.regex("^deleterrormessage"))
        async def delerrmsg(client: app, cquery: CallbackQuery):
            await cquery.message.delete()


            


app.run(main())




