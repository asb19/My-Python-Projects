import asyncio
import json
from time import sleep
import csv

from telethon import TelegramClient, events
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

api_id = '9056976'
api_hash = '8726e15c2ce627e8f3378081ed21f4a6'
name = 'token'
channel = -1001614280935
# user_id=2110450700
# user_id=619382602
# user_id=542437856

async def main():
    async with TelegramClient(name, api_id, api_hash) as client:
       # get all the users and print them
        count=0
        async def sendMessage(entity, message):
            
            await client.send_message(entity, message)



        
        # await sendMessage(PeerUser(5291531488),"hello, please use this link to join https://t.me/+_Xbu-KVEQs4zNDBl")

        # @client.on(events.NewMessage())
        # async def handler(event):
        #     print(event)
        #     await event.reply('Hey!')
        
        # @client.on(events.Raw())
        # async def handler(event):
        #     print(event)
            # await event.reply('Hey!')
        a=[]
        
        async for u in client.iter_participants(channel, aggressive=True):
            sleep(2)
            count=count+1
            
            # print(u)
            # await sendMessage(PeerUser(u.id),"hello")
            # client.send_message(entity=PeerUser(u.id), message="hello")
            a.append(json.dumps({"tgid":u.id, "firstName": u.first_name, "lastName": u.last_name, "username": u.username, "phone": u.phone }))
            sleep(5)
            print(u.id, u.first_name, u.last_name, u.username, count)
        
        with open('csvdata993.csv', "w") as csv_file:
            writer = csv.writer(csv_file, delimiter=',')
            writer.writerow(["tgid","firstName", "lastName", "userName", "phone"])
            for line in a:
                writer.writerow(json.loads(line).values())

        await client.run_until_disconnected()

# Only this line changes, the rest will work anywhere.
# Jupyter
# await main()

# Otherwise
asyncio.run(main())