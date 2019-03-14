import urllib.request
import json


cryptopia_url = "https://www.cryptopia.co.nz/api/GetMarkets/BTC"
cryptopia_data_key = "Data"
cryptopia_label_key = "Label"
cryptopia_bid_price_key = "BidPrice"

dictionary_label_key = "label"
dictionary_bid_price_key = "bid_price"
dictionary_calculation_key = "calculation"
dictionary_final_price_key = "final_price"

number_of_percentage_decimals = 10

class cryptopia_marketplace(object):

	def __init__(self):
		super (cryptopia_marketplace, self).__init__()
		
	def get_raw_data(self):
		response = urllib.request.urlopen(cryptopia_url)
		return response.read()

	def get_json_from_raw_data(self):
		raw_data = self.get_raw_data()
		return json.loads(raw_data)

	def get_formated_data(self, highest_marketplace_price): 
		json_data = self.get_json_from_raw_data()
		data_pairs = json_data[cryptopia_data_key]
		dictionaries = []
		for element in data_pairs:
			dictionary = {}
			dictionary[dictionary_label_key] = element[cryptopia_label_key]
			dictionary[dictionary_bid_price_key] = str(element[cryptopia_bid_price_key])
			dictionary[dictionary_calculation_key] = str(element[cryptopia_bid_price_key]) + " * " + str(highest_marketplace_price)
			dictionary[dictionary_final_price_key] =  round(float(element[cryptopia_bid_price_key]) * highest_marketplace_price, number_of_percentage_decimals)
			dictionaries.append(dictionary)
		return dictionaries