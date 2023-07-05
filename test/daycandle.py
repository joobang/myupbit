import requests

url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to="+"2020-01-01 00:00:00"+"&count=1"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)