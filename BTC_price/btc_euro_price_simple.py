#!/usr/bin/env python

#imports
import requests

#get json request
response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
data = response.json()


print("BTC Price: " + data["bpi"]["EUR"]["rate"] + "€")


