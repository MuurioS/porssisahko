import requests

url = "https://api.porssisahko.net/v1/latest-prices.json"
response = requests.get(url)
data = response.json()

hours = data["prices"]
hour_prices = []
for hour in hours:
    hour_price = hour["price"]
    hour_prices.append(hour_price)

cheapest_price = min(hour_prices)
most_expensive_price = max(hour_prices)
average_price = sum(hour_prices)/len(hour_prices)
print(f"Average price: {average_price:.2f} c/kWh")
print(f"Cheapest price: {cheapest_price:.2f} c/kWh")
print(f"Most expensive price: {most_expensive_price:.2f} c/kWh")