# Local files import
import config

# Telegram bot module import
import logging
from telegram.ext import Updater
from telegram.ext import CommandHandler

def launchbot():
    updater = Updater(token = config.token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', start)
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

if __name__ == '__main__':
    try:
        launchbot()
    except KeyboardInterrupt:
        exit()

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text="I'm a bot, please talk to me!")