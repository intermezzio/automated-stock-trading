import sys

sys.path.insert(0, './config')
sys.path.insert(0, './stock-market-prediction/python')

import datetime
import time
import pytz
import requests
import alpaca_trade_api as tradeapi

from config import *
from predict_market import est_perc_increase

# # load the alpaca account
# api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v2')

# # get account details
# account = api.get_account()

# positions = api.list_positions()

# api.submit_order('AAPL',10,'buy','limit','gtc',170.50)

############################################################################################


# URLs for accessing the ALPACA API_KEY
BASE_URL = "https://paper-api.alpaca.markets"
ACCOUNT_URL = f"{BASE_URL}/v2/account"
ORDERS_URL = f"{BASE_URL}/v2/orders"
DELETE_URL = f"{BASE_URL}/v2/positions"
HEADERS = {
	"APCA-API-KEY-ID": API_KEY,
	"APCA-API-SECRET-KEY": SECRET_KEY
}
IEX_BASE_URL = "https://cloud.iexapis.com/v1"

# r = requests.get(ACCOUNT_URL, headers=HEADERS)

def make_order(symbol, qty, side, order_type, time_in_force):
	data = {
		"symbol": symbol,
		"qty": qty,
		"side": side,
		"type": order_type,
		"time_in_force": time_in_force
	}
	return requests.post(ORDERS_URL, json=data, headers=HEADERS)
# r = make_order("JNUG", 100, "buy", "market", "gtc")
# r = make_order("FAZ", 1000, "buy", "market", "gtc")
# print(r.content)

def account_money():
	json_response = requests.get(ACCOUNT_URL, headers=HEADERS).json()
	money = float(json_response['cash'])
	return money

def opening_buys(symbols, account_money=account_money()):
	est_increases = dict()
	current_prices = dict()
	for symbol in symbols:
		current_prices[symbol] = get_stock_price(symbol)
		est_increases[symbol] = est_perc_increase(symbol, current_prices[symbol])

	best_prospects = max(est_increases, key=est_increases.get)
	print(best_prospects)
	print(est_increases[best_prospects])
	if est_increases[best_prospects] > 1:
		# buy this stock
		r = make_order(best_prospects, account_money // current_prices[best_prospects], "buy", 
			"market", "gtc")
		return r.json()
	return 0

def get_stock_price(symbol):
	IEX_DATA_URL = f"{IEX_BASE_URL}/stock/{symbol}/batch"
	data = {
		"types": "quote",
		"token": IEX_API_TOKEN,
		"filter": "open"
	}
	json_response = requests.get(IEX_DATA_URL, params=data).json()
	return json_response["quote"]["open"]

def liquidate():
	requests.delete(DELETE_URL, headers=HEADERS)
	requests.delete(ORDERS_URL, headers=HEADERS)

if __name__ == "__main__":

	while True:
		d = datetime.datetime.now(pytz.timezone('US/Eastern'))
		try:
			print(d)
			if d.hour == 9 and d.minute == 30:
				print('buying now')
				stuff = opening_buys(["JNUG", "NUGT", "JDST", "DUST"])
				print(f"info: {stuff}")
			elif d.hour == 15 and d.minute == 58:
				print('liquidate')
				liquidate()
			time.sleep(60)
		except Exception as e:
			print(e)
			continue