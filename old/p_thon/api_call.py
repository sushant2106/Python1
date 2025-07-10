import requests
import os

# replace the "demo" apikey below with your own key from https://www.alphavantage.co/support/#api-key
url = 'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY&symbol=IBM&interval=5min&apikey=demo'
print(os.getenv('TIME_SERIES_DAILY'))
r = requests.get(url)
data = r.json()

# print(data)