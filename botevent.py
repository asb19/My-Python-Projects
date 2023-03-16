# from telegram.ext import Updater, MessageHandler, Filters


# def new_member(bot, update):
#     print(update)
#     for member in update.message.new_chat_members:
#         update.message.reply_text('Welcome')
#         print(member)
#         # if member.username == 'YourBot':
#         #     update.message.reply_text('Welcome')

# updater = Updater('5515533637:AAFYNv5V2sauTkvyM8OjB-XrWUoc6uS8Rnk')

# updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))

# updater.start_polling()
# updater.idle()

# import logging
# from telegram import Update
# from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

# logging.basicConfig(
#     format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
#     level=logging.INFO
# )

# async def start(update: Update, context: ContextTypes.us):
#     await context.bot.send_message(chat_id=update.effective_chat.id, text="I'm a bot, please talk to me!")

# if __name__ == '__main__':
#     application = ApplicationBuilder().token('5515533637:AAFYNv5V2sauTkvyM8OjB-XrWUoc6uS8Rnk').build()
    
#     start_handler = CommandHandler('start', start)
#     application.add_handler(start_handler)
    
#     application.run_polling()


from telegram.ext import Updater, MessageHandler, Filters

def new_member(update, context):
    for member in update.message.new_chat_members:
        if member.username == 'YourBot':
            update.message.reply_text('Welcome')


def new_chat(update, context):
    print(context)
    for member in update.message.new_chat_members:
        if member.username == 'YourBot':
            update.message.reply_text('Welcome')

updater = Updater('5421778576:AAF0bg2oIr6YftEPUi1cw7B7miPRPK2uVQA', use_context=True)  # use_context will be True by default in version 13+

updater.dispatcher.add_handler(MessageHandler(Filters.status_update.new_chat_members, new_member))
updater.dispatcher.add_handler(MessageHandler(Filters.status_update.message, new_member))

updater.start_polling()
updater.idle()