import requests
import json
import time
''':('''

def get_employers():
    req = requests.get('https://api.hh.ru/employers')
    data = req.content.decode()
    req.close()
    count_of_employers = json.loads(data)['found']
    employers = []
    i = 0
    j = count_of_employers
    k = 0
    while i < j and k < 10:
        req = requests.get('https://api.hh.ru/employers/' + str(i + 1))
        data = req.content.decode()
        req.close()
        jsObj = json.loads(data)
        '''try:'''
        employers.append([jsObj['id'], jsObj['name'], jsObj['open_vacancies']])
        i += 1
        k += 1
        '''except:
            i += 1
            j += 1'''
        if i % 200 == 0:
            time.sleep(0.2)
    return employers
