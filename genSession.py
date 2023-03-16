from pyrogram import Client
from telethon.sync import TelegramClient
from telethon.sessions import StringSession
from termcolor import colored, cprint
from pyfiglet import figlet_format

def main():
    while True:
        cprint(colored(figlet_format('Telegram', "smslant"), "cyan", attrs=['bold']))
        cprint(colored("Session generator\n", "magenta", attrs=['bold']))
        cprint("[p] Pyrogram\n[t] Telethon", "yellow")
        opt = input(colored("Choose your option: ", "green")).lower()
        if "p" in opt:
            cprint("You've selected pyrogram", "magenta")
            APP_ID = int(input(colored("Enter APP ID here: ", "green")))
            API_HASH = input(colored("Enter API HASH here: ", "green"))
            with Client(":mttttetmory:", api_id=APP_ID, api_hash=API_HASH) as app:
                app.storage.SESSION_STRING_FORMAT=">B?256sQ?"
                session_str = app.export_session_string()
                if app.get_me().is_bot:
                    user_name = input(colored("Enter the username: ", "green"))
                    msg = app.send_message(user_name, session_str)
                else:
                    msg = app.send_message("me", session_str)
                msg.reply_text(
                    "⬆️ This String Session is generated using https://tgsession.infotelbot.com \nPlease subscribe @InFoTelGroup ",
                    quote=True,
                )
                cprint("please check your Telegram Saved Messages/user's PM for the StringSession ", "yellow")
            break

        elif "t" in opt:
            cprint("You've selected Telethon", "magenta")
            APP_ID = int(input(colored("Enter APP ID here: ", "green")))
            API_HASH = input(colored("Enter API HASH here: ", "green"))
            with TelegramClient(StringSession(), APP_ID, API_HASH) as client:
                session_str = client.session.save()
                if client.is_bot():
                    user_name = input("Enter the username: ")
                    msg = client.send_message(user_name, session_str)
                else:
                    msg = client.send_message("me", session_str)
                msg.reply(
                    "⬆️ This String Session is generated using https://tgsession.infotelbot.com \nPlease subscribe @InFoTelGroup "
                )
                cprint("please check your Telegram Saved Messages/User's PM for the StringSession ", "yellow")
            break
            
        else:
            cprint("Invalid option try again", "red")
        

if __name__ == "__main__":
    main()