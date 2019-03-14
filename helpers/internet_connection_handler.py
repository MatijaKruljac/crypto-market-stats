import socket


ping_url = "www.google.com"
ping_port = 80

connection_exist_message = "Internet connection exist."
connection_doesnt_exist_message = "Internet connection doesn't exist."

class internet_connection_handler(object):

	def __init__(self):
		super(internet_connection_handler, self).__init__()
		
	def check_connection(self):
		if self.is_connectable():
			print(connection_exist_message)
			return True
		else:
			print(connection_doesnt_exist_message)
			return False

	def is_connectable(self):
	    try:
	        socket.create_connection((ping_url, ping_port))
	        return True
	    except OSError:
	        pass
	    return False