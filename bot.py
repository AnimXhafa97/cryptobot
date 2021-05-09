import cbpro
import pandas as pd
import numpy as np
import websocket, json, asyncio, copra, csv
from IPython.display import display
from tabulate import tabulate
from copra.websocket import Channel, Client
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands, AverageTrueRange
from ta.momentum import RSIIndicator
from pymongo import MongoClient

socket = "wss://ws-feed.pro.coinbase.com"

#API KEYS
SECRET = 'o1UkRvnp9JsMTOqCsqxDjJJGWJuVmwDMBawRNgFwKse7Fxf1YgLHomLKJaBHxCddcjhuHT1MKBr/A++QcfbDuA=='
PUBLIC = '5bd728b19bb79b8ddd492127eafc06c3'

data = pd.DataFrame()



class Mod_Client(Client):
    def on_message(self, message):
        global data
        data = data.append(message, ignore_index=True)

loop = asyncio.get_event_loop()
ws_btc = Mod_Client(loop, Channel('ticker', ['BTC-USD']))
#ws_eth = Mod_Client(loop, Channel('ticker', ['ETC-USD']))

try:
    loop.run_forever()

except KeyboardInterrupt:
    loop.run_until_complete(ws_btc.close())
    loop.close()

data = data.fillna(0)

rsi_indicator = RSIIndicator(data.get('price'), fillna=True)
df['RSI'] = rsi_indicator.rsi(data.get('price'))

display(data.get('RSI'))



