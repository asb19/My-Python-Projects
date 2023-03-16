from time import sleep, time
from telethon import TelegramClient
from telethon.tl.types import PeerUser, PeerChat, PeerChannel

# Use your own values here
# api_id = '13391192'
# api_hash = 'e942944e84f44241542a324b30d54540'
# name = 'prod38'
# channel = -1001605180285

api_id = '17821989'
api_hash = '06a69aecf578ac30ec21258194a84dee'
name = 'amir'
channel = -1001717856740

# client = TelegramClient(name, api_id, api_hash)

async with TelegramClient(session_name, api_id, api_hash) as client:
   await client.send_message('me', 'Hello, myself!')
   print(await client.download_profile_photo('me')) 
   

       

client.start(main())  
# get all the channels that I can access
# channels = {d.entity.username: d.entity
#             for d in .get_dialogs()
#             if d.is_channel}

# choose the one that I want list users from
# channel = channels[channel]

# get all the users and print them
# count=0
# async def sendMessage(entity, message):
#     await client.send_message(entity, message)
# for u in client.iter_participants(channel, aggressive=True):
#     sleep(2)
#     count=count+1
#     sendMessage(PeerUser(u.id),"hello")
#     # client.send_message(entity=PeerUser(u.id), message="hello")
#     sleep(2)
#     print(u.id, u.first_name, u.last_name, u.username, count)




#fino a qui il codice
client.disconnect()