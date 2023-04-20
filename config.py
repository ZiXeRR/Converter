import requests
import json

exchanges = {
    'доллар': 'USD',
    'рубль': 'RUB'

}

TOKEN = '6256811351:AAGaYyArQnWXKcGhLwmVGAaqKgnkyAkP-m8'

base_key = 'USD'
sym_key = 'RUB'
amount = 1

r1 = requests.get(f"https://v6.exchangerate-api.com/v6/5f3d2ba1970175b2f4c0741e/pair/{base_key}/{sym_key}/{amount}")
resp = json.loads(r1.content)
