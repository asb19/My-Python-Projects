from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.types import InputPeerEmpty, InputChannel, ChannelParticipantsSearch, InputPeerChannel, ChannelParticipantsRecent, ChannelParticipantsAdmins
import json
import asyncio
from telethon import events

print("het")

class Scraper():
     def __init__(self):
        #Enter Your 7 Digit Telegram API ID.
        self.api_id =  12383296 
        #Enter Yor 32 Character API Hash
        self.api_hash = 'ba8b148e652911b94484fb0a2c962d7d'   
        #Enter Your Mobile Number With Country Code.
        self.phone = '+918837332128'   

        self.client = TelegramClient(self.phone, self.api_id, self.api_hash)
        self.members=[]

    
     def connect(self):
        #connecting to telegram and checking if you are already authorized. 
        #Otherwise send an OTP code request and ask user to enter the code 
        #they received on their telegram account.
        #After logging in, a .session file will be created. This is a database file which makes your session persistent.
        
        self.client.start()
        # if not self.client.is_user_authorized():
        #     self.client.send_code_request(self.phone)
        #     self.client.sign_in(self.phone, input('Enter verification code: '))
    #     @client.on(events.NewMessage(pattern='(?i)hello.+'))
    #     async def handler(event):
    # # Respond whenever someone says "Hello" and something else
    #         await event.reply('Hey!')

     def membersFetch(self):
        #connecting to telegram and checking if you are already authorized. 
        #Otherwise send an OTP code request and ask user to enter the code 
        #they received on their telegram account.
        #After logging in, a .session file will be created. This is a database file which makes your session persistent.
        channel = self.client.get_entity(InputPeerChannel(1412971229,-585494633818529210))
        # print(channel)
        participants = self.client(GetParticipantsRequest(InputChannel(channel.id,channel.access_hash),filter=ChannelParticipantsAdmins(), offset=0,limit=10,hash=0))
        
        print(participants.stringify())
        for user in participants.users:

            print(user.stringify())
        # if not self.client.is_user_authorized():
        #     self.client.send_code_request(self.phone)
        #     self.client.sign_in(self.phone, input('Enter verification code: '))


if __name__ == '__main__':
    telegram = Scraper()
    telegram.connect()
    telegram.membersFetch()
    print("connected")
    