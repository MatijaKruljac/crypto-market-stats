from terminaltables import AsciiTable

from controllers.simple_data_handler import simple_data_handler

from marketplaces.cryptopia.cryptopia_marketplace import cryptopia_marketplace
from marketplaces.cryptopia.cryptopia_marketplace import dictionary_label_key
from marketplaces.cryptopia.cryptopia_marketplace import dictionary_bid_price_key
from marketplaces.cryptopia.cryptopia_marketplace import dictionary_calculation_key
from marketplaces.cryptopia.cryptopia_marketplace import dictionary_final_price_key


label_header_title = "LABEL"
bid_price_header_title = "BID PRICE"
calculation_header_title = "CALCULATION"
final_price_header_title = "FINAL PRICE ($ USD)"

default_currency = "btc"

simple_data_handler = simple_data_handler()
simple_data_handler.get_marketplaces_prices(default_currency)

cryptopia_marketplace = cryptopia_marketplace()

class complex_data_handler(object):

	def __init__(self):
		super(complex_data_handler, self).__init__()
		self.lowest_marketplace_price = 0
		self.highest_marketplace_price = 0

	def get_data(self):
		self.lowest_marketplace_price = simple_data_handler.get_lowest_price()
		self.highest_marketplace_price = simple_data_handler.get_highest_price()
		dictionaries = cryptopia_marketplace.get_formated_data(self.highest_marketplace_price)

		table_data = [
			[label_header_title, bid_price_header_title, 
    		 calculation_header_title, final_price_header_title]
    		]

		for dictionary in dictionaries:
			table_data.append([
				dictionary[dictionary_label_key], dictionary[dictionary_bid_price_key], 
				dictionary[dictionary_calculation_key], dictionary[dictionary_final_price_key]
			])

		ascii_table = AsciiTable(table_data)
		return ascii_table.table

	def get_lowest_marketplace_price_conclusion(self):
		return "Lowest price is {0} USD($).".format(self.lowest_marketplace_price)

	def get_highest_marketplace_price_conclusion(self):
		return "Highest price is {0} USD($).".format(self.highest_marketplace_price)
