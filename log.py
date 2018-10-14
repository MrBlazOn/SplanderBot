def heroku_log(last_chat_id, last_chat_name, last_chat_text):
	log = 'User [{0}] {1} typed \"{2}\"'.format(last_chat_id, last_chat_name, last_chat_text)
	print(log)