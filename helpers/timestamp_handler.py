import datetime


timestamp_format = "%A, %d. %B %Y %I:%M%p"

class timestamp_handler(object):
	
	def __init__(self):
		super(timestamp_handler, self).__init__()

	def display_current_timestamp(self):
		print("\nOn a date: " + self.get_current_timestamp())

	def get_current_timestamp(self):
		return datetime.datetime.now().strftime(timestamp_format)