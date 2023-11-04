import os
import asyncio
import aiohttp
import time
import requests

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']
results=[]


async def get_symbol():
    async with aiohttp.ClientSession() as session:
        for symbol in symbols:
          print('Working on Symbole {}'.format(symbol))
          resonse=await session.get(url.format(symbol,api_key),ssl=False)
          results.append(await resonse.json())
   





# # loop=asyncio.get_event_loop()
# # loop.run_until_complete(get_symbol())
# # loop.close()

asyncio.run(get_symbol())



    











