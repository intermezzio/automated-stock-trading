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

# load the alpaca account
api = tradeapi.REST(API_KEY, SECRET_KEY, api_version='v2', 
	base_url="https://paper-api.alpaca.markets")

# get account details
account = api.get_account()
print(account)

positions = api.list_positions()
print(positions)

# api.submit_order('AAPL',10,'buy','limit','gtc',170.50)