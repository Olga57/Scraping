import requests
from pprint import pprint
from bs4 import BeautifulSoup
import pandas as pd

text = input("Введите професиию, должность или компанию: ")
url = 'https://hh.ru'
params = {'clusters': 'true',
          'ored_clusters': 'true',
          'enable_snippets': 'true',
          'salary': '',
          'text': text,
          'st': 'searchVacancy'
          }


headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}
response = requests.get(url+'/search/vacancy', params = params, headers = headers)


dom = BeautifulSoup(response.text, 'html.parser')
vacancy_list = dom.find_all('div',{'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})
vacancies_hh = []
while True:
    for vacancy in vacancy_list:
        current_vacancy = {}
        vacancy_salary = vacancy.find('span', {'data-qa':'vacancy-serp__vacancy-compensation'},
                                      {'class':['bloko-header-section-3, bloko-header-section-3_lite']})
        vacancy_data = vacancy.find('a', {'class':'bloko-link'})
        vacancy_link = vacancy_data['href']
        vacancy_name = vacancy_data.getText(),
        website = url
        current_vacancy['name'] = vacancy.name
        current_vacancy['link'] = vacancy_link
        current_vacancy['website'] = website
    if vacancy_salary == None:
        current_vacancy['min_salary'] = 'None'
        current_vacancy['max_salary'] = 'None'
        current_vacancy['currency'] = 'None'

    else:
        salary = vacancy_salary.getText().replace("\u202f", "").split(' ')
        if len(salary) == 3 and salary[0] == 'от':
            current_vacancy['min_salary'] = int(salary [1])
            current_vacancy['max_salary']  = 'None'
            current_vacancy['currency'] = salary[-1]
        if len(salary) == 3 and salary[0] == 'до':
            current_vacancy['min_salary'] = 'None'
            current_vacancy['max_salary'] = int(salary[1])
            current_vacancy['currency'] = salary[-1]
        if len(salary) == 4:
            current_vacancy['min_salary'] = int(salary[0])
            current_vacancy['max_salary'] = int(salary[2])
            current_vacancy['currency'] = salary[-1]
        vacancies_hh.append(current_vacancy)
    next_page = dom.find('a', {'data-qa':'pager-next'}, {'class':'bloko-button'})
    if next_page != None:
        next_link = next_page['href']
        response = requests.get(url + next_link,headers = headers)
        dom = BeautifulSoup(response.text, 'html.parser')
        vacancy_list = dom.find_all('div',{'class': 'vacancy-serp-item__row vacancy-serp-item__row_header'})
        continue
    else:
         break

total_vacancies_hh = pd.DataFrame(vacancies_hh)
total_vacancies_hh.to_csv('hh.csv',encoding='utf-8')
print(total_vacancies_hh)


