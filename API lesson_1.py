

import requests
import json
from pprint import pprint


# Задание 1
req = requests.get('http://api.github.com/users/USERNAME/repos')
main_link = 'http://api.github.com/users'
user = '/USERNAME'
repos = '/repos'
req = requests.get(f'{main_link}{user}{repos}')
if req.ok:
    data = json.loads(req.text)
    i = 0
    while i < len(data):
        x = data[i]['name']
        i = i + 1
        pprint(x)
    with open('data_set.json', w, encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)







