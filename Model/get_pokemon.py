import json
import requests

response = requests.get('https://pokeapi.co/api/v2/pokemon/?limit=802')
d = dict()

def jprint(j_obj):
    text = json.dumps(j_obj, sort_keys=True, indent=4)
    print(text)

def data():
    for i in range(len(response.json().get('results'))):
        name = response.json().get('results')[i].get('name')
        url = response.json().get('results')[i].get('url')
        d[name] = url
