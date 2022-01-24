### Задание 1
### Посмотреть документацию к API GitHub,
### разобраться как вывести список репозиториев для конкретного пользова
import requests
from pprint import pprint
import json
user = 'Olga57'
url = f'https://api.github.com/users/{user}/repos'
response = requests.get(url)
##j_data = response.json()
##pprint(j_data)
if response.ok:
    repos = response.json()
    with open('repos_json','w') as f:
        json.dump(response.json(),f)
    with open('repos_json','r') as f:
        from_file = json.load(f)
    print(f'Список репозиториев пользователя {user}:')

    for el in repos:
        print(el['name'])
    print(f'/nВыгрузка из файла:')
    pprint(from_file)