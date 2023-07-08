import requests
import json

url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to="+"2017-09-26 00:00:00"+"&count=200"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

#print(response.text)

data = json.loads(response.text)

print([tuple(item.values()) for item in data ])