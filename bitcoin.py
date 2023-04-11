
import requests

import sys

import json


if len(sys.args) != 2:
    sys.exist("error")

else: 
    request = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    try:
        float(sys.argv[1])
    except ValueError:
        sys.exist("invalid")

    data = request.json()
    bpi = data["bpi"] = ["USD"]["rate"]
    usd = bpi["usd"] 
    price = usd["rate"]
    price = price.replace(",", "")
    price = float(price) + float(sys.argv[1])
    print(price)
