import urllib.request
import json


btc_pair = "btcusd"
eth_pair = "ethusd"
neo_pair = "neousd"
monero_pair = "xmrusd"
bch_pair = "bchusd"
etc_pair = "etcusd"
xrp_pair = "xrpusd"
zec_pair = "zecusd"
dash_pair = "dshusd"
ltc_pair = "ltcusd"
eos_pair = "eosusd"
rep_pair = "repusd"
iota_pair = "iotusd"
trx_pair = "trxusd"
gnt_pair = "gntusd"
omg_pair = "omgusd"

btc_name = "btc"
eth_name = "eth"
neo_name = "neo"
monero_name = "xmr"
bch_name = "bch"
etc_name = "etc"
xrp_name = "xrp"
zec_name = "zec"
dash_name = "dash"
ltc_name = "ltc"
eos_name = "eos"
rep_name = "rep"
iota_name = "iota"
trx_name = "trx"
gnt_name = "gnt"
omg_name = "omg"

bitfinex_url = "https://api.bitfinex.com/v1/book/"
bitfinex_bids_key = "bids"
bitfinex_price_key = "price"

first_element_index = 0

wrong_data = ""

class bitfinex_marketplace(object):

	def __init__(self):
		super (bitfinex_marketplace, self).__init__()
		
	def get_raw_data(self, currency):
		pair = self.get_pair(currency)
		if pair != wrong_data:
			response = urllib.request.urlopen(bitfinex_url + pair)
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
		if bitfinex_bids_key in json_data and json_data != wrong_data:
			first_object_data = json_data[bitfinex_bids_key][first_element_index]
			return first_object_data[bitfinex_price_key]
		return 0.0

	def get_pair(self, currency):
		if currency == btc_name:
			return btc_pair
		elif currency == eth_name:
			return eth_pair
		elif currency == neo_name:
			return neo_pair
		elif currency == monero_name:
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
		elif currency == eos_name:
			return eos_pair
		elif currency == rep_name:
			return rep_pair
		elif currency == iota_name:
			return iota_pair
		elif currency == trx_name:
			return trx_pair
		elif currency == gnt_name:
			return gnt_pair
		elif currency == omg_name: 
			return omg_pair
		else:
			return ""



