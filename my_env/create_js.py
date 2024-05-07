import json

data = {
    "Дата": "2024-05-02",
    "Категория": "Расход",
    "Сумма": "1500",
    "Описание": "Покупка продуктов"

}

with open('data.json', 'w',encoding='utf-8') as f:
        f.write(json.dumps(data, indent=4,ensure_ascii=False))
                
print("Файл с данными создан",data)