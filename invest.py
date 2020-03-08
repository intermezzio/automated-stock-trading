import sys
sys.path.insert(0, './investment-strategies')
# import functions in this repo that manage the portfolio
sys.path.insert(0, './stock-market-prediction/python')
# import functions in the algorithm repo that manage the portfolio

from firstTrades import chooseToBuy, sellAll


def initialize(context):

	set_symbol_lookup_date("2020-01-01")
	
	schedule_function(
		chooseToBuy,
		date_rules.every_day(),
		time_rules.market_open(minutes=1)
	)

	schedule_function(
		sellAll,
		date_rules.every_day(),
		time_rules.market_close(minutes=2)
	)