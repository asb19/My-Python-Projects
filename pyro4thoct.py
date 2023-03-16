import json
from pyrogram import Client

api_id = 12079424
api_hash = "c83a7649ee6afe26068b859a45340ca1"

app = Client("prod40", api_id=api_id, api_hash=api_hash)


async def main():
    x=[]
    async with app:
    #     async for i in app.get_messages(chat_id=-1001726846911, message_ids=[48]):
    #         x.append(i)
        # y = await app.get_messages(chat_id=-1001726846911, message_ids=[48])
        # print(y)
        # print(await app.get_me())
        # async for i in app.iter_:
        #     print(i)

        async for i in app.get_chat_members(chat_id=-1001717856740):
            print(i)
        await app.send_message(chat_id=5291531488, text="hello")

    # count=0

    # for i in x:
    #     print(i)
    #     if count==5:
    #         break
    #     count=count+1
    
            






app.run(main())