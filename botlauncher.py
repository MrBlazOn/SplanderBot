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

    start_handler = CommandHandler('start', commands.start)
    dispatcher.add_handler(start_handler)

    random_handler = CommandHandler('random', commands.random_unsplash_photo)
    dispatcher.add_handler(random_handler)

    by_request_handler = CommandHandler('search', commands.photo_by_request, pass_args = True)
    dispatcher.add_handler(by_request_handler)

    helper_hendler = CommandHandler('help', commands.help)
    dispatcher.add_handler(helper_hendler)

    many_photos_hendler = CommandHandler('few', commands.many_photos)
    dispatcher.add_handler(many_photos_hendler)

    updater.start_polling()

    logging.basicConfig(format = '%(asctime)s - %(name)s - %(levelname)s - %(message)s', level = logging.INFO)

if __name__ == '__main__':
    try:
        launchbot()
    except KeyboardInterrupt:
        exit()