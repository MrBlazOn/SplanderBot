import telegram

def start(bot, update):
    bot.send_message(chat_id = update.message.chat_id, text = "I'm a bot, please talk to me!")

def random_unsplash_photo(bot, update):
	bot.send_photo(chat_id = update.message.chat_id, photo = 'https://source.unsplash.com/1600x900/')
