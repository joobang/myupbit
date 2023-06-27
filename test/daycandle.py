import requests

url = "https://api.upbit.com/v1/candles/days?market=KRW-BTC&to=2023-01-01 00:00:00&count=100"

headers = {"accept": "application/json"}

response = requests.get(url, headers=headers)

print(response.text)