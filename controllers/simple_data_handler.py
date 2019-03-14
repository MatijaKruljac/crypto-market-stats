from terminaltables import AsciiTable

from marketplaces.bitfinex.bitfinex_marketplace import bitfinex_marketplace
from marketplaces.kraken.kraken_marketplace import kraken_marketplace
from marketplaces.exmo.exmo_marketplace import exmo_marketplace


bitfinex_marketplace_name = "Bitfinex"
kraken_marketplace_name = "Kraken"
exmo_marketplace_name = "Exmo"

marketplace_header_title = "MARKETPLACE"
price_header_title = "PRICE (USD $)"
percentage_header_title = "PERCENTAGE (%)"

lowest_price_prefix = "lowest"
highest_price_prefix = "highest"
lowest_price_prefix_value = "LOWEST PRICE: "
highest_price_prefix_value = "HIGHEST PRICE: "

first_element_index = 0
number_of_percentage_decimals = 5
number_of_percentage_table_decimals = 2

bitfinex_marketplace = bitfinex_marketplace()
kraken_marketplace = kraken_marketplace()
exmo_marketplace = exmo_marketplace()

class simple_data_handler(object):

	def __init__(self):
		super(simple_data_handler, self).__init__()
		self.bitfinex_price = 0
		self.kraken_price = 0
		self.exmo_price = 0

	def get_data(self, currency):
		self.get_marketplaces_prices(currency)

		bitfinex_percentage = round(self.get_bitfinex_percentage(), number_of_percentage_decimals)
		kraken_percentage = round(self.get_kraken_percentage(), number_of_percentage_decimals)
		exmo_percentage = round(self.get_exmo_percentage(), number_of_percentage_decimals)

		bitfinex_percentage_for_table = str(round(bitfinex_percentage * 100, number_of_percentage_table_decimals))
		kraken_percentage_for_table = str(round(kraken_percentage * 100, number_of_percentage_table_decimals))
		exmo_percentage_for_table = str(round(exmo_percentage * 100, number_of_percentage_table_decimals))

		table_data = [
    		[marketplace_header_title, price_header_title, percentage_header_title],
    		[bitfinex_marketplace_name, str(self.bitfinex_price), bitfinex_percentage_for_table],
    		[kraken_marketplace_name, str(self.kraken_price), kraken_percentage_for_table],
    		[exmo_marketplace_name, str(self.exmo_price), exmo_percentage_for_table]
		]

		ascii_table = AsciiTable(table_data)
		return ascii_table.table

	def get_marketplaces_prices(self, currency):
		self.bitfinex_price = float(bitfinex_marketplace.get_price(currency))
		self.kraken_price = float(kraken_marketplace.get_price(currency))
		self.exmo_price = float(exmo_marketplace.get_price(currency))

	def get_highest_price(self):
		sorted_prices = sorted([self.bitfinex_price, self.kraken_price, self.exmo_price])
		highest_price_index = len(sorted_prices) - 1
		return sorted_prices[highest_price_index]

	def get_lowest_price(self):
		sorted_prices = sorted([self.bitfinex_price, self.kraken_price, self.exmo_price])
		return sorted_prices[first_element_index]

	def get_bitfinex_percentage(self):
		return self.calculate_percentage(self.bitfinex_price)

	def get_kraken_percentage(self):
		return self.calculate_percentage(self.kraken_price)

	def get_exmo_percentage(self):
		return self.calculate_percentage(self.exmo_price)

	def calculate_percentage(self, marketplace_price):
		highest_price = self.get_highest_price()
		if marketplace_price == 0 or highest_price == 0:
			return 0.0
		return 1 - (marketplace_price/highest_price)

	def get_conclusion(self, prefix):
		bitfinex_percentage = round(self.get_bitfinex_percentage(), number_of_percentage_decimals)
		kraken_percentage = round(self.get_kraken_percentage(), number_of_percentage_decimals)
		exmo_percentage = round(self.get_exmo_percentage(), number_of_percentage_decimals)

		if prefix == lowest_price_prefix:
			return self.get_lowest_price_and_highest_percentage_conclusion(bitfinex_percentage, kraken_percentage, exmo_percentage)
		elif prefix == highest_price_prefix:
			return self.get_highest_price_and_lowest_percentage_conclusion(bitfinex_percentage, kraken_percentage, exmo_percentage)
		else:
			return ""

	def get_lowest_price_and_highest_percentage_conclusion(self, bitfinex_percentage, kraken_percentage, exmo_percentage):
		dictionary = {bitfinex_marketplace_name: bitfinex_percentage, kraken_marketplace_name: kraken_percentage, exmo_marketplace_name: exmo_percentage}
		interesting_market_place = sorted(dictionary.keys(), key=lambda k: dictionary[k], reverse=True)[first_element_index]

		if interesting_market_place == bitfinex_marketplace_name:
			return self.get_conclusion_message(lowest_price_prefix_value, interesting_market_place, str(self.bitfinex_price), str(bitfinex_percentage))
		elif interesting_market_place == kraken_marketplace_name:
			return self.get_conclusion_message(lowest_price_prefix_value, interesting_market_place, str(self.kraken_price), str(kraken_percentage))
		elif interesting_market_place == exmo_marketplace_name:
			return self.get_conclusion_message(lowest_price_prefix_value, interesting_market_place, str(self.exmo_price), str(exmo_percentage))
		else:
			return ""

	def get_highest_price_and_lowest_percentage_conclusion(self, bitfinex_percentage, kraken_percentage, exmo_percentage):
		dictionary = {bitfinex_marketplace_name: bitfinex_percentage, kraken_marketplace_name: kraken_percentage, exmo_marketplace_name: exmo_percentage}
		sorted_dictionary = sorted(dictionary.keys(), key=lambda k: dictionary[k], reverse=True)
		interesting_market_place_index = len(sorted_dictionary) - 1
		interesting_market_place = sorted_dictionary[interesting_market_place_index]

		if interesting_market_place == bitfinex_marketplace_name:
			return self.get_conclusion_message(highest_price_prefix_value, interesting_market_place, str(self.bitfinex_price), str(bitfinex_percentage))
		elif interesting_market_place == kraken_marketplace_name:
			return self.get_conclusion_message(highest_price_prefix_value, interesting_market_place, str(self.kraken_price), str(kraken_percentage))
		elif interesting_market_place == exmo_marketplace_name:
			return self.get_conclusion_message(highest_price_prefix_value, interesting_market_place, str(self.exmo_price), str(exmo_percentage))
		else:
			return ""

	def get_conclusion_message(self, prefix, marketplace_name, marketplace_price, marketplace_percentage):
		return "{0} Marketplace {1} with price {2} and with percentage -{3}.".format(prefix, marketplace_name, marketplace_price, marketplace_percentage)

		