import telegram
from unsplash.api import Api
from unsplash.auth import Auth

client_id = "1904d81ebf366e14d1d5ce804d0f268a29126d9a18d27703ab554b92570fffe6"
client_secret = "fc68dbac271c9450d7d157daac2ce9bb633088cc3447f1f228b74597205d842d"
redirect_uri = "urn:ietf:wg:oauth:2.0:oob"
code = ""

auth = Auth(client_id, client_secret, redirect_uri, code=code)
unsplash_api = Api(auth)

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "I'm a bot, please talk to me!")

def random_unsplash_photo(bot, update):
	random_photo = unsplash_api.photo.random()
	print(random_photo)
	bot.send_photo(chat_id = update.message.chat_id, photo = random_photo)
