# https://www.youtube.com/watch?v=yARJCvZujV4
# Imports
import requests
import string
import random

def checkquota():
    r_url = 'https://www.random.org/quota/?format=plain'
    
    quota = int(requests.get(r_url).text)
    if quota < 1:
        raise Exception("Quota aufgebraucht")
    return quota
    
def generate_pwd_from_str(**params):
    checkquota()

    length = params.get("length", 10)
    digits = params.get("digits", "on")
    loweralpha = params.get("loweralpha", "on")
    upperalpha = params.get("upperalpha", "on")
    unique = params.get("unique", "on")

    return requests.get('https://www.random.org/strings/?num=1&len={}&digits={}&upperalpha={}&loweralpha={}&unique={}&rnd=new&format=plain'.format(length, digits, upperalpha, loweralpha, unique))

generate_pwd_from_str(length=20)

