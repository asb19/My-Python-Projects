import json
from time import sleep, time
from telethon import TelegramClient

import csv


# Use your own values here
# api_id = '13391192'
# api_hash = 'e942944e84f44241542a324b30d54540'
# name = 'prod38'
# channel = -1001605180285

api_id = '17821989'
api_hash = '06a69aecf578ac30ec21258194a84dee'
name = 'amir'
channel = -1001717856740

client = TelegramClient(name, api_id, api_hash)

client.start()  
# get all the channels that I can access
# channels = {d.entity.username: d.entity
#             for d in .get_dialogs()
#             if d.is_channel}

# choose the one that I want list users from
# channel = channels[channel]

# get all the users and print them
count=0
a=[]
for u in client.iter_participants(channel, aggressive=True):
    sleep(2)
    count=count+1
    # client.send_message(entity=u.id, message="hello")
    sleep(2)
    print(u.id, u.first_name, u.last_name, u.username, count)
    a.append(json.dump({"tgid":u.id, "firstName": u.first_name, "lastName": u.last_name, "username": u.username }))
    if count==5:
        break

with open('csvdata.csv', "wb") as csv_file:
        writer = csv.writer(csv_file, delimiter=',')
        for line in a:
            writer.writerow(line)

#fino a qui il codice
client.disconnect()