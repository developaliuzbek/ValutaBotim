import requests
from pprint import pprint

def airboshla(pul):
    response=requests.get(url=f'https://v6.exchangerate-api.com/v6/d0fc939eb2488897b26d967b/pair/USD/UZS/{pul}')
    malumot=response.json()
    return malumot