import requests

url = "https://api.porssisahko.net/v1/latest-prices.json"
response = requests.get(url)
data = response.json()

hours = data["prices"]
hour_prices = []
for hour in hours:
    hour_price = hour["price"]
    hour_prices.append(hour_price)

print(hour_prices)