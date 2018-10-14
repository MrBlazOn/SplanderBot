# System modules import
import requests
import os

# Server changes processing class
class BotHandler:

	def __init__(self, token):
		self.token = token
		self.api_url = "https://api.telegram.org/bot{}/".format(token)

	def get_updates(self, offset = None, timeout = 30):
		method = 'getUpdates'
		params = {'timeout': timeout, 'offset': offset}
		resp = requests.get(self.api_url + method, params)

		try:
			result_json = resp.json()['result']
			return result_json
		except KeyError as key_error_message:
                print('Exception while obtaining data from server: ', key_error_message)

	def send_message(self, chat_id, text):
		params = {'chat_id': chat_id, 'text': text}
		method = 'sendMessage'
		resp = requests.post(self.api_url + method, params)
		return resp

	def get_last_update(self):
		get_result = self.get_updates()
		last_update = {}

		if len(get_result) > 0:
			last_update = get_result[-1]

		return last_update
