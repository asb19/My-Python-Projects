from h11 import CLIENT
from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest, EditExportedChatInviteRequest, GetExportedChatInviteRequest
from telethon.tl.custom.adminlogevent import AdminLogEvent
from telethon.tl.functions.channels import GetParticipantsRequest, EditBannedRequest, GetFullChannelRequest, EditAdminRequest
from telethon.tl.types import InputPeerEmpty, InputChannel, ChannelParticipantsSearch, InputPeerChannel, ChannelParticipantsRecent, ChannelParticipantsAdmins, PeerChannel, ChatBannedRights, InputPeerUser, ChannelAdminLogEventsFilter, ChatAdminRights, PeerUser
import json
import asyncio
from telethon import events
from telethon.sessions import StringSession


# api_id =  17821989 

api_id = 17821989
api_hash = "06a69aecf578ac30ec21258194a84dee"
# api_id =  13391192 
        #Enter Yor 32 Character API Hash
# api_hash = '06a69aecf578ac30ec21258194a84dee'   
# api_hash = 'e942944e84f44241542a324b30d54540'   
        #Enter Your Mobile Number With Country Code.
phone = '+918816945172' 
# bot_token = "5515533637:AAFYNv5V2sauTkvyM8OjB-XrWUoc6uS8Rnk"  

# with TelegramClient(StringSession("1BQANOTEuMTA4LjU2LjEzMAG7Fbrjt9I/PhliBr3/lOBeRrTFO0y5a8gD+gReA/L4s2mlpTNekCR4M6VJyu5248zd5KlJ2urnT8IUk0FbZlXPFqFBsbYHwe2dQs8pAt7rRj+DZzY4Z/6aSwo7bPL+SyvnKQ2xHShjKTuPaXHVvgEnEHFUgvGnKzD8f+LrKGOx48Hk+Y9Et6ruKUeBCDAlNy7Ucto/KeJ40uTlhmKQYPR1keMbFM67921SspDSS21maye5NbUfqWCJ3nBXiZngUkncY94ii6wo3IAm+GYKdq+ALKYnBMMa8F+nsfGMK0StmrFHHGAkfVLmA0+mSa6Q5pyIVOu3zUhKEtsed5mob5eu6Q=="), api_id, api_hash) as client:
#     # print(client.get_participants(PeerChannel(1605180285)))

#     # client.loop.run_until_comrulete(client.send_message('me', 'Hi'))


client = TelegramClient(phone,api_id,api_hash).start()
# client = TelegramClient('x` x   /PhliBr3/lOBeRrTFO0y5a8gD+gReA/L4s2mlpTNekCR4M6VJyu5248zd5KlJ2urnT8IUk0FbZlXPFqFBsbYHwe2dQs8pAt7rRj+DZzY4Z/6aSwo7bPL+SyvnKQ2xHShjKTuPaXHVvgEnEHFUgvGnKzD8f+LrKGOx48Hk+Y9Et6ruKUeBCDAlNy7Ucto/KeJ40uTlhmKQYPR1keMbFM67921SspDSS21maye5NbUfqWCJ3nBXiZngUkncY94ii6wo3IAm+GYKdq+ALKYnBMMa8F+nsfGMK0StmrFHHGAkfVLmA0+mSa6Q5pyIVOu3zUhKEtsed5mob5eu6Q==',api_id,api_hash)

# with TelegramClient(StringSession("1BQANOTEuMTA4LjU2LjEzMAG7s2GsGPRGQ18SlHsZFMblsCo05dJOBXH1tjasvX8W5Ba3uv4D27qs1cGV558Tqf6fZFNPRXAy4Rhcs/g7bscamlvRwtqUkKkzYV5CMgvaKKlkGv21bWcI8+gCPl6fzxA/Pz13hpK94/bR66lQBqBPcPki95wP9PlCsvq2H03FE1ryr+t/SG7okwYlSZiZ35Ut11U//f0RvqV9HNKJeO2Fr9zCWBktdN8qNStuzuWxshUGaCIpLEJmQB5hkJp/fMEGdfoDHEc646xA97YM4YPGJseJPLBF/nD+ylNqHA+QEUGDc7pYwjIIqzwkc0AA3JXSUjT37vvztxTlwCZk5NXrLQ=="), api_id, api_hash) as client:
#     print(client.get_me())
#     client.run_until_disconnected()

client.connect()

print("client")
print(client.get_me())
# print(client.get_participants(PeerChannel(1562893392)))
# print("user-1\n",client.get_entity(entity=PeerUser(1118210272)))


rights = ChatBannedRights(
            until_date=0,
            view_messages=True,
            send_messages=None,
            send_media=True,
            send_stickers=True,
            send_gifs=True,
            send_games=True,
            send_inline=True,
            embed_links=True
            )

admin_rights = ChatAdminRights(
    post_messages=True,
    add_admins=True,
    anonymous=True,

)

iter_admins = ChannelAdminLogEventsFilter(join=True,leave=None,invite=True)

# channel = client.get_entity(InputPeerChannel(1655847278,-1069446140722316534))
# channel = client.get_entity(PeerChannel(1655847278))
# for i in client.iter_admin_log(channel,join=True):
#     print(i.action.invite.link, i.user_id)
# print(channel.stringify())

# x=client(GetExportedChatInviteRequest(peer=InputChannel(1518864748, 2189535559500740598),link="https://t.me/+htWDyEh0EDw3MjU1"))
# print("X-1", x)

# x=client(EditAdminRequest(channel=-1001619493291,user_id=5438961582, admin_rights=admin_rights, rank="Admin"))
# print("X-1", x)




    


# client.send_message(InputChannel(channel.id,channel.access_hash),message="Hey all")

# @client.on(events.ChatAction(chats=[InputPeerChannel(1666928242,3811261580640880030)]))
# async def handler(event):
#     print(event)
#     # Respond whenever someone says "Hello" and something else
#     if event.user_joined:
#         user = await event.get_user()
#         print(user)
#         await event.reply('Welcome to the group!')
#     if event.user_added:
#         user = await event.get_user()
#         print(user)
#         await event.reply('Welcome to the group!')

@client.on(events.MessageDeleted(InputPeerChannel(1666928242,3811261580640880030)))
async def handler(event):
    print(event.stringify())
    # Respond whenever someone says "Hello" and something else
    # if event.user_joined:
    #     user = await event.get_user()
    #     print(user)
    #     await event.reply('Welcome to the group!')
    # if event.user_added:
    #     user = await event.get_user()
    #     print(user)
    await event.reply('deleted!', event)

@client.on(events.Raw())
async def handler(event):
    print(event)
    # Respond whenever someone says "Hello" and something else
    # if event.user_joined:
    #     user = await event.get_user()
    #     print(user)
    #     await event.reply('Welcome to the group!')
    # if event.user_added:
    #     user = await event.get_user()
    #     print(user)
    

# @client.on(events.NewMessage(InputPeerChannel(channel.id,channel.access_hash)))
# async def handler(event):
#     print("hey")
#     # print(event)
#     data = await client(EditBannedRequest(InputChannel(channel.id, channel.access_hash),InputPeerUser(1118210272, -6258420905972364418), rights))
#     print("ban data",data.stringify())

#     # if event.new_chat_members:
#     #     print(event.new_chat_members)
#     # Respond whenever someone says "Hello" and something else
#     # await event.reply('Hey!')

@client.on(events.NewMessage)
async def handler(event):
    print("hey")
    # print(event)
    # data = await client(EditBannedRequest(InputChannel(channel.id, channel.access_hash),InputPeerUser(1118210272, -6258420905972364418), rights))
    # print("ban data",data.stringify())

    # if event.new_chat_members:
    #     print(event.new_chat_members)
    # Respond whenever someone says "Hello" and something else
    # await event.reply('Hey!')

# async def extraTask(channel,user):
#     for i in client.iter_admin_log(entity=channel,join=True):
#             if i.user_id==user.id:
#                 link = i.action.invite.link
#                 # got the link
#                 print(link)
#                 # perform link expiry
#                 # EditExportedChatInviteRequest()

#                 #db operation
#                 await asyncio.sleep(0.2)

#                 break


@client.on(events.ChatAction(chats=None))
async def handler(event):
    print(event.stringify())
    # Respond whenever someone says "Hello" and something else
    if event.user_joined:
        user = await event.get_user()
        print(user)
        await event.reply('Welcome to the added group!')
        # await extraTask(event.action_message.peer_id,user)
        
        # data = await client(EditBannedRequest(InputChannel(1118210272,-6258420905972364418),InputPeerUser(user.id, user.access_hash), rights))
        # print(data.stringify())
    if event.user_left:
        user = await event.get_user()
        print(user)
        
    if event.user_added:
        user = await event.get_user()
        print(user)
        await event.reply('Welcome to the added group!')


# @client.on(events.UserUpdate(chats=None))
# async def handler(event):
#     # If someone is uploading, say something
#     print("update", event.stringify())
#     client.get_stats()
#     if event.uploading:
#         await client.send_message(event.user_id, 'What are you sending?')


with client:
    client.run_until_disconnected()
           