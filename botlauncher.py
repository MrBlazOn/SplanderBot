# Local files import
import config
import commands

# Telegram bot module import
import logging
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

splander = telegram.Bot(token = config.token)

def launchbot():
    updater = Updater(token = config.token)
    dispatcher = updater.dispatcher

    start_handler = CommandHandler('start', commands.start(splander, updater))
    dispatcher.add_handler(start_handler)

    updater.start_polling()

    logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

if __name__ == '__main__':
    try:
        launchbot()
    except KeyboardInterrupt:
        exit()