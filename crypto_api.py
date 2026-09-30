import os
import requests

api_key = os.getenv("MIMO_CRYPTO_CRAZE_API_KEY")
url = "https://crypto-craze.mimo.dev/api/coins/bitcoin"
headers = {"api-key": api_key}
def get_crypto_price():
  request = requests.get(url, headers=headers)
  return request.json()
crypto = get_crypto_price()
symbol = crypto["symbol"]
price_usd = crypto["priceUsd"]
print(symbol)
print(price_usd)