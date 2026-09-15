import requests

def fetch_data(option):
  url = f"https://swapi.mimo.dev/api/{option}/"
  data = []
  try:
    response = requests.get(url)
    response.raise_for_status()
    data = response.json()
    print(len(data))
  except requests.HTTPError as e:
    print(f"Error fetching data: {e}")
    return None

  return data

data = fetch_data("people")

if data:
  for d in data:
    print(d["name"])
  else:
    print("Unable to download data")

option = input("Enter an option: ").strip().lower()
data = fetch_data(option)
