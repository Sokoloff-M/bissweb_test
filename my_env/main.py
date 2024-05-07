import json


with open('data.json', 'r',encoding='utf-8') as f:
    data = json.load(f)
    print(data)

for key,values in data.items():
    print(f'{key}: {values}')
#Отображает баланс
# def balance():
#     pass
# #Добавение записи
# def Adding_an_entry():
#     pass
# #Редактирование записи
# def Editing_an_entry():
#     pass
# #Поиск по записи
# def Search_through_records():
#     pass
