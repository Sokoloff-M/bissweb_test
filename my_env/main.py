import json
from my_env import datas


with open(datas.json, 'r', encoding='utf-8') as file:
    datas = json.load(file) 

transactions = datas["transactions"]

for transaction in transactions:
     print(transaction)



#Отображает баланс
def balance():
    pass
#Добавение записи
def Adding_an_entry():
    pass
#Редактирование записи
def Editing_an_entry():
    pass
#Поиск по записи
def Search_through_records():
    pass
