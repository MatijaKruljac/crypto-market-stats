import sys
import os
import time


loaded_data_message = "Data is successfully loaded!"

class loading_indicator_handler(object):

	def __init__(self):
		super(loading_indicator_handler, self).__init__()

	def show(self):
		self.run()
		self.show_loaded_data_message()

	def show_loaded_data_message(self):
		sys.stdout.write("\r" + loaded_data_message)  
		sys.stdout.flush()

	def run(self):
		spinner = ['Loading data... |', 'Loading data... /', 'Loading data... -',
				   'Loading data... \\', 'Loading data... |', 'Loading data... /', 
				   'Loading data... -', 'Loading data... \\']
		index = 0
		while index < len(spinner):
		    sys.stdout.write("\r" + spinner[index])  
		    sys.stdout.flush()
		    time.sleep(.2)
		    index += 1