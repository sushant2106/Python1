import requests
import json

resp=requests.get('http://127.0.0.1:8000/')


print(resp.text)