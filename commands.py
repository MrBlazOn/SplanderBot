import telegram
from unsplash.api import Api
from unsplash.auth import Auth

from config import *

auth = Auth(client_id, client_secret, redirect_uri, code = code)
unsplash_api = Api(auth)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "I'm a bot, please talk to me!")

def random_unsplash_photo(bot, update):
	random_photo = unsplash_api.photo.random()
	photo_id = random_photo[0].id
	bot.send_photo(chat_id = update.message.chat_id, photo = 'unsplash.com/photos/{}'.format(photo_id))

def photo_by_request(bot,update):
	new_list=update.message.text.split()
	needed_photo=unsplash_api.photo.random()
	photo_id=random_photo[0].id
	bot.send_photo(chat_id = update.message.chat_id, photo = 'unsplash.com/photos/{}'.format(new_list[1])+{}.format(photo_id))