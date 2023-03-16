from telethon.sync import TelegramClient
from telethon.tl.functions.messages import GetDialogsRequest
from telethon.tl.functions.channels import GetParticipantsRequest
from telethon.tl.functions.contacts import SearchRequest
from telethon.tl.types import InputPeerEmpty, InputChannel, ChannelParticipantsSearch, InputPeerChannel, ChannelParticipantsRecent, ChannelParticipantsAdmins
import json

print("het")

class Scraper():
     def __init__(self):
        #Enter Your 7 Digit Telegram API ID.
        self.api_id =  17821989 
        #Enter Yor 32 Character API Hash
        self.api_hash = '06a69aecf578ac30ec21258194a84dee'   
        #Enter Your Mobile Number With Country Code.
        self.phone = '+918816945172'   

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


     def membersFetch(self):
        #connecting to telegram and checking if you are already authorized. 
        #Otherwise send an OTP code request and ask user to enter the code 
        #they received on their telegram account.
        #After logging in, a .session file will be created. This is a database file which makes your session persistent.
        channel = self.client.get_entity(InputPeerChannel(1666928242,3811261580640880030))
        # print(channel)
        participants = self.client(GetParticipantsRequest(InputChannel(channel.id,channel.access_hash),filter=ChannelParticipantsAdmins(), offset=0,limit=10,hash=0))
        
        for user in participants.users:

            print(user.first_name,user.phone)
        # if not self.client.is_user_authorized():
        #     self.client.send_code_request(self.phone)
        #     self.client.sign_in(self.phone, input('Enter verification code: '))

     def search(self):
        result = self.client(SearchRequest(q="animal", limit=10))
        for channel in result.chats:
            channelInfo = self.client.get_entity(InputPeerChannel(channel.id, channel.access_hash))
            participants = self.client(GetParticipantsRequest(InputPeerChannel(channel.id, channel.access_hash),ChannelParticipantsAdmins(),0,10,0))
            print(participants.users)
      
     def fetchFroupos(self):
        chats = []
        last_date = None
        chunk_size = 200
        groups=[]
 
        result = self.client(GetDialogsRequest(
             offset_date=last_date,
             offset_id=0,
             offset_peer=InputPeerEmpty(),
             limit=chunk_size,
             hash = 0
         ))
        chats.extend(result.chats)
        for chat in chats:
                try:
                    if chat.megagroup!= True:
                        groups.append(chat)
                except:
                    continue
        for i in range(2):
            print(groups[i])



if __name__ == '__main__':
    telegram = Scraper()
    telegram.connect()
    telegram.search()
    # telegram.membersFetch()
    # telegram.fetchFroupos()
    print("connected")
    