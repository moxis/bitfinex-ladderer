# Bitfinex Ladderer

This program aims to help traders ladder their positions on Bitfinex over a specified price range. Position size will be equally calculated and uniformly distributed.

**DISCLAIMER: USE AT YOUR OWN RISK. I AM NOT RESPONSIBLE FOR TRADING LOSSES. THIS IS NOT A MONEY MAKING PROGRAM!!**

### Prerequisites

* Python 3+

Install these modules through pip:

```
$ pip install ccxt
```

### Installing

Firstly go to Bitfinex and create a new pair of API Keys. Please ensure that you have all trading permissions enabled. Create a new file called **api_key.json** with the following contents:

```
{
  "apiKey": "PUT YOUR KEY HERE",
  "secret": "PUT YOUR SECRET HERE"
}

```

Afterwards, place the JSON file into the same directory as the script.

### Usage

Simply start the script and follow the instructions. Below is an example of laddering LONGS for BTC from $6600 to $6700. 

```
$ python app.py
$ Total Capital: TOTAL AMOUNT YOU WANT TO LADDER IN DOLLARS
$ Lower Boundary: 6600
$ Upper Boundary: 6700
$ BUY (1) OR SELL (2): 1
```

