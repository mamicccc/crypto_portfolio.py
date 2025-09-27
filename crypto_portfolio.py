import requests

portfolio = {
    "bitcoin": 0.05,   # BTC miktarı
    "ethereum": 1.2,   # ETH miktarı
    "dogecoin": 1500   # DOGE miktarı
}

def get_price(symbol):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={symbol}&vs_currencies=usd"
    data = requests.get(url).json()
    return data[symbol]["usd"]

total = 0
for coin, amount in portfolio.items():
    price = get_price(coin)
    value = price * amount
    total += value
    print(f"{coin.capitalize()}: {amount} = ${value:,.2f}")

print("Total Portfolio Value: $", round(total, 2))
