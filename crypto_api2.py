import os
import requests

api_key = os.getenv("MIMO_CRYPTO_CRAZE_API_KEY")

headers = {"api-key": api_key}
def get_crypto_price(coin_id):
  url = f"https://crypto-craze.mimo.dev/api/coins/{coin_id}"
  request = requests.get(url, headers=headers)
  return request.json()
crypto = get_crypto_price("ethereum")
def print_crypto_price(crypto):
  symbol = crypto["symbol"]
  price_usd = crypto["priceUsd"]
  print(symbol)
  print(price_usd)
print_crypto_price(crypto)
print_crypto_price(get_crypto_price("bitcoin"))
print_crypto_price(get_crypto_price("solana"))