import ccxt
from pprint import pprint

binance = ccxt.binance({})
binance.load_markets()
pprint(binance.symbols)


