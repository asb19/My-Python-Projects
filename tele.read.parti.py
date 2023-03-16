from telethon.sync import TelegramClient
from telethon import functions, types

with TelegramClient(name, api_id, api_hash) as client:
    result = client(functions.messages.GetMessageReadParticipantsRequest(
        peer='username',
        msg_id=42
    ))
    for x in result:
        print(x)