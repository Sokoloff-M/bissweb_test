import json
from datetime import datetime


def  wrote_to_json(data,filename):
    #Записываем данные в файл json
    with open(filename, 'w',encoding='utf-8') as f:
        json.dump(data, f)
    print('Данные успешно сохранены в файл')

def read_from_json(data,filelename):
    #Читаем из файла json
    with open(filelename,'r', encoding='utf-8') as f:
        data = json.load(f)
    print('Данные из файла:')
    for entry in data:
        print('\n'.join([f"{key}:{value}" for key, value in entry.items()]))

def add_entry(filename):
    #Добавляем запить о расходе или доходе
    entry = {}
    print = ('Введите информацию о записи')
    entry["Дата"] = datetime.now().strftime('%Y-%m-%d')
    entry["Категория"] =input("Категория: ")
    entry["Сумма"] = float(input("Сумма: "))
    entry["Описание"]= input("Описание: ")
    
    
    
