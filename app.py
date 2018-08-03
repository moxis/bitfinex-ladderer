import ccxt
import json

with open("api_key.json", "r") as f:
    keys = json.load(f)

bitfinex = ccxt.bitfinex({
    'enableRateLimit': True,
    **keys,
})

capital = float(input('Total capital: '))
lower_range = float(input("Lower boundary: "))
upper_range = float(input("Upper boundary: "))
d = (upper_range - lower_range)/10

type = input("BUY (1) OR SELL (2): ")
if type == "1":
    func = bitfinex.create_limit_buy_order
    type_written = "LONG"
else:
    func = bitfinex.create_limit_sell_order
    type_written = "SHORT"

for x in range(0, 11):
    price = round(lower_range + x * d, 1)
    amount = round((capital/11)/price, 6)
    func('BTC/USDT', amount, price, {'type': 'limit'})
    print(f"Placed a {type_written} order for {amount} BTC at a price of {price}")
