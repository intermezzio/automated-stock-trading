import sys

sys.path.insert(0, './config')
sys.path.insert(0, './stock-market-prediction/strategies/QEA')

import datetime
import time
import pytz
import requests
import random
import alpaca_trade_api as tradeapi

from config import *
from predict_market import est_perc_increase

# load the alpaca account
api = tradeapi.REST(APCA_API_KEY_ID, APCA_API_SECRET_KEY, api_version='v2', 
	base_url=APCA_API_BASE_URL)

# get account details
account = api.get_account()
print(account)
account_money = float(account.cash)
print(f"${account_money}")

positions = api.list_positions()
print(positions)

# api.submit_order('AAPL',10,'buy','limit','gtc',170.50)

def opening_buys(symbols, account_money=account_money):
	est_increases = dict()
	current_prices = dict()
	for symbol in symbols:
		current_prices[symbol] = float(api.alpha_vantage.current_quote(symbol)["05. price"])
		print(current_prices[symbol])
		est_increases[symbol] = random.uniform(0.95, 1.05) # est_perc_increase(symbol, current_prices[symbol])

	buy_ticker = max(est_increases, key=est_increases.get)
	print(buy_ticker)
	print(est_increases[buy_ticker])
	if est_increases[buy_ticker] > 1:
		# buy this stock
		r = 1 #api.submit_order(buy_ticker, account_money // current_prices[buy_ticker], 
			#"buy", "market", "gtc")
		print(account_money // current_prices[buy_ticker])
		return r.json()
	return 0

def liquidate():
	api.cancel_all_orders()


if __name__ == "__main__" and len(sys.argv) > 1 and sys.argv[1] == "auto":
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
