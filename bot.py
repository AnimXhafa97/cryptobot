import cbpro
import pandas as pd
import numpy as np
import websocket, json, asyncio, copra, csv
from copra.websocket import Channel, Client
from ta import add_all_ta_features
from ta.utils import dropna
from ta.volatility import BollingerBands, AverageTrueRange
from pymongo import MongoClient
# wsClient = cbpro.WebsocketClient(socket, products=["BTC-USD", "ETH-USD"], channels=["ticker"])

# allows for use of public client methods (https://github.com/danpaquin/coinbasepro-python), not needed right now
# mongo_client = MongoClient('mongodb://localhost:27017/')
# public_client = cbpro.PublicClient()

socket = "wss://ws-feed.pro.coinbase.com"

#API KEYS
SECRET = 'o1UkRvnp9JsMTOqCsqxDjJJGWJuVmwDMBawRNgFwKse7Fxf1YgLHomLKJaBHxCddcjhuHT1MKBr/A++QcfbDuA=='
PUBLIC = '5bd728b19bb79b8ddd492127eafc06c3'



def stream_ticker_data():
    json_message = json.loads(message)
    print(json_message)
    # try:
    #     loop.run_forever()

    # except KeyboardInterrupt:
    #     loop.run_until_complete(ws.close())
    #     loop.close()

loop = asyncio.get_event_loop()
ws = Client(loop, Channel('ticker', ['BTC-USD', 'ETH-USD']))




