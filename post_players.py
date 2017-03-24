import requests
import json
from random import choice, random

URL = "http://127.0.0.1:5050/users/"
PLAYERS = ['Player',"User","Gamer","Person","Boss"]

for i in range(20):
    headers = {'content-type': 'application/json'}
    name = "{}-{}".format(choice(PLAYERS), int(random()*100))
    wins = int(random()*100)
    battles = wins + int(random()*150)
    exp_total = int(random() * 5000)
    payload = json.dumps({'name': name, 'battles_total':battles, "exp_total":exp_total,
                "wins_total":wins})
    requests.post(URL, data=payload, headers=headers)

