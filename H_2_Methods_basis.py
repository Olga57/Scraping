##2. Изучить список открытых API (https://www.programmableweb.com/category/all/apis). Найти среди них любое, требующее авторизацию (любого типа). Выполнить запросы к нему, пройдя авторизацию. Ответ сервера записать в файл

import requests
import json
from pprint import pprint

version = '5.131'
access_token = 'f*********'

url = 'https://api.vk.com/method/groups.get'
params = {'v':'5.131',
          'access_token':access_token,}
response = requests.get(url, params=params)

j_data = response.json()
pprint(j_data)

if response.ok:
    j_data = response.json()
    with open('groups.json', 'w', encoding = 'utf-8') as f:
        json.dump(j_data, f, ensure_ascii=False)
else:
    print('Ошибка. Необходима проверка')
