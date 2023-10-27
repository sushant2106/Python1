import os
import requests
import time

api_key = os.getenv('ALPHAVANTAGE_API_KEY')
url = 'https://www.alphavantage.co/query?function=OVERVIEW&symbol={}&apikey={}'
symbols = ['AAPL', 'GOOG', 'TSLA', 'MSFT', 'AAPL']

results=[]
start=time.time()
for symbol in symbols:
    print('Working on Symbole {}'.format(symbol))
    resonse=requests.get(url.format(symbol,api_key))
    results.append(resonse.json())

end=time.time()

print(results)