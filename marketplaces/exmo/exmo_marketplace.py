import urllib.request
import json


btc_pair = "BTC_USD"
eth_pair = "ETH_USD"
xmr_pair = "XMR_USD"
bch_pair = "BCH_USD"
etc_pair = "ETC_USD"
xrp_pair = "XRP_USD"
zec_pair = "ZEC_USD"
dash_pair = "DASH_USD"
ltc_pair = "LTC_USD"

btc_name = "btc"
eth_name = "eth"
xmr_name = "xmr"
bch_name = "bch"
etc_name = "etc"
xrp_name = "xrp"
zec_name = "zec"
dash_name = "dash"
ltc_name = "ltc"

exmo_url = "https://api.exmo.com/v1/trades/?pair="
exmo_price_key = "price"

first_element_index = 0

wrong_data = ""

class exmo_marketplace(object):

	def __init__(self):
		super (exmo_marketplace, self).__init__()
		
	def get_raw_data(self, currency):
		pair = self.get_pair(currency)
		if pair != wrong_data:
			response = urllib.request.urlopen(exmo_url + pair)
			if response.getcode() == 404:
				return wrong_data
			return response.read()
		return wrong_data

	def get_json_from_raw_data(self, currency):
		raw_data = self.get_raw_data(currency)
		if raw_data != wrong_data:
			return json.loads(raw_data)
		return wrong_data

	def get_price(self, currency):
		json_data = self.get_json_from_raw_data(currency)
		exmo_pair_key = self.get_pair(currency)
		if exmo_pair_key == wrong_data:
			return 0.0
		if exmo_pair_key in json_data and json_data != wrong_data:
			prices = []
			for element in json_data[exmo_pair_key]:
				price = float(element[exmo_price_key])
				prices.append(price)
			sorted_prices = sorted(prices)
			price_index = len(sorted(prices)) - 1
			return sorted_prices[price_index]
		return 0.0

	def get_pair(self, currency):
		if currency == btc_name:
			return btc_pair
		elif currency == eth_name:
			return eth_pair
		elif currency == xmr_name:
			return monero_pair
		elif currency == bch_name:
			return bch_pair
		elif currency == etc_name:
			return etc_pair
		elif currency == xrp_name:
			return xrp_pair
		elif currency == zec_name:
			return zec_pair
		elif currency == dash_name:
			return dash_pair
		elif currency == ltc_name:
			return ltc_pair
		else:
			return ""


