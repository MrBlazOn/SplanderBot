from telegram.ext import BaseFilter

class FilterOfCommands(BaseFilter):
	ListofCommands = ['random', 'search', 'few']
	def filter(self, message):
		if ListofCommads not in massage.text :
			return False
		else:
			return True