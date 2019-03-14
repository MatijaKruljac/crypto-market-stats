import sys
import os

from controllers.simple_data_handler import simple_data_handler
from controllers.simple_data_handler import lowest_price_prefix
from controllers.simple_data_handler import highest_price_prefix
from controllers.complex_data_handler import complex_data_handler

from helpers.loading_indicator_handler import loading_indicator_handler
from helpers.internet_connection_handler import internet_connection_handler
from helpers.timestamp_handler import timestamp_handler
from helpers.user_inputs_for_marketplaces import currencies_user_inputs


simple_data_handler = simple_data_handler()
complex_data_handler = complex_data_handler()

loading_indicator_handler = loading_indicator_handler()
internet_connection_handler = internet_connection_handler()
timestamp_handler = timestamp_handler()

def present_simple_data(currency):
	if internet_connection_handler.check_connection() is False:
		return
	loading_indicator_handler.show()
	timestamp_handler.display_current_timestamp()
	print("\n")
	print("SIMPLE DATA - {0}".format(currency))
	simple_table = simple_data_handler.get_data(currency)
	print(simple_table)
	lowest_conclusion = simple_data_handler.get_conclusion(lowest_price_prefix)
	print(lowest_conclusion)
	highest_conclusion = simple_data_handler.get_conclusion(highest_price_prefix)
	print(highest_conclusion)

def present_complex_data():
	if internet_connection_handler.check_connection() is False:
		return
	loading_indicator_handler.show()
	timestamp_handler.display_current_timestamp()
	print("\n")
	print("COMPLEX DATA - Cryptopia")
	cryptopia_complex_data = complex_data_handler.get_data()
	print(cryptopia_complex_data)
	highest_marketplace_price_conclusion = complex_data_handler.get_highest_marketplace_price_conclusion()
	print(highest_marketplace_price_conclusion)
	lowest_marketplace_price_conclusion = complex_data_handler.get_lowest_marketplace_price_conclusion()
	print(lowest_marketplace_price_conclusion)

def print_main_menu():
	print("\n")
	print("main menu")
	print("----------------------------")
	print("(s) - simple data")
	print("(c) - complex data")
	print("(r) - clear display")
	print("(t) - terminate program")
	print("----------------------------")

def print_currencies_simple_data_sub_menu():
	print("\n")
	print("enter currency name")
	print("----------------------------")
	print("btc, eth, neo, gno, stelar") 
	print("monero, bch, etc, xrp, zec") 
	print("dash, ltc, eos, rep, iota") 
	print("trx, gnt, omg")
	print("----------------------------")
	print("(m) - main menu")
	print("----------------------------")

def listen_for_main_menu_user_input():
	print_main_menu()
	user_input = input("Your choice: ")

	if user_input == "s":
		listen_for_currencies_menu_user_input()
	elif user_input == "c":
		present_complex_data()
		listen_for_main_menu_user_input()
	elif user_input == "r":
		os.system('clear')
		listen_for_main_menu_user_input()
	elif user_input == "t":
		print("Program terminated... :(\n")
		sys.exit()
	else:
		print("Glup si! Probaj opet!\n")
		listen_for_main_menu_user_input()

def listen_for_currencies_menu_user_input():
	print_currencies_simple_data_sub_menu()
	user_input = input("Your choice: ")

	if user_input in currencies_user_inputs:
		present_simple_data(user_input)
		listen_for_currencies_menu_user_input()
	elif user_input == "m":
		listen_for_main_menu_user_input()
	else:
		print("Glup si! Probaj opet!\n")
		listen_for_currencies_menu_user_input()

if __name__ == "__main__":
	listen_for_main_menu_user_input()
	

