import urllib.request
import json


btc_pair = "XBTUSD"
eth_pair = "ETHUSD"
gno_pair = "GNOUSD"
stelar_pair = "XLMUSD"
monero_pair = "XMRUSD"
bch_pair = "BCHUSD"
etc_pair = "ETCUSD"
xrp_pair = "XRPUSD"
zec_pair = "ZECUSD"
dash_pair = "DASHUSD"
ltc_pair = "LTCUSD"
eos_pair = "EOSUSD"
rep_pair = "REPUSD"

btc_code_key = "XXBTZUSD"
eth_code_key = "XETHZUSD"
gno_code_key = "GNOUSD"
stelar_code_key = "XXLMZUSD"
monero_code_key = "XXMRZUSD"
bch_code_key = "BCHUSD"
etc_code_key = "XETCZUSD"
xrp_code_key = "XXRPZUSD"
zec_code_key = "XZECZUSD"
dash_code_key = "DASHUSD"
ltc_code_key = "XLTCZUSD"
eos_code_key = "EOSUSD"
rep_code_key = "XREPZUSD"

btc_name = "btc"
eth_name = "eth"
gno_name = "gno"
stelar_name = "stelar"
monero_name = "monero"
bch_name = "bch"
etc_name = "etc"
xrp_name = "xrp"
zec_name = "zec"
dash_name = "dash"
ltc_name = "ltc"
eos_name = "eos"
rep_name = "rep"

kraken_url = "https://api.kraken.com/0/public/Depth?pair="
kraken_result_key = "result"
kraken_bids_key = "bids"

first_element_index = 0

wrong_data = ""

class kraken_marketplace(object):

	def __init__(self):
		super (kraken_marketplace, self).__init__()
		
	def get_raw_data(self, currency):
		pair = self.get_pair(currency)
		if pair != wrong_data:
			response = urllib.request.urlopen(kraken_url + pair)
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
		code_key = self.get_code_key(currency)
		if kraken_result_key in json_data and json_data != wrong_data and code_key != wrong_data:
			bids = json_data[kraken_result_key][code_key][kraken_bids_key]
			return bids[first_element_index][first_element_index]
		return 0.0

	def get_code_key(self, currency):
		if currency == btc_name:
			return btc_code_key
		elif currency == eth_name:
			return eth_code_key
		elif currency == gno_name:
			return gno_code_key
		elif currency == stelar_name:
			return stelar_code_key
		elif currency == monero_name:
			return monero_code_key
		elif currency == bch_name:
			return bch_code_key
		elif currency == etc_name:
			return etc_code_key
		elif currency == xrp_name:
			return xrp_code_key
		elif currency == zec_name:
			return zec_code_key
		elif currency == dash_name:
			return dash_code_key
		elif currency == ltc_name:
			return ltc_code_key
		elif currency == eos_name:
			return eos_code_key
		elif currency == rep_name: 
			return rep_code_key
		else:
			return ""

	def get_pair(self, currency):
		if currency == btc_name:
			return btc_pair
		elif currency == eth_name:
			return eth_pair
		elif currency == gno_name:
			return gno_pair
		elif currency == stelar_name:
			return stelar_pair
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
		else:
			return ""
