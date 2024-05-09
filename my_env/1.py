import json

def write_to_json(data, filename):
    """Записывает данные в JSON файл."""
    with open(filename, 'w') as f:
        json.dump(data, f)
    print("Данные успешно записаны в файл.")

def read_from_json(filename):
    """Читает данные из JSON файла и выводит их в консоль."""
    with open(filename, 'r') as f:
        data = json.load(f)
    print("Данные из файла:")
    for entry in data:
        print("\n".join([f"{key}: {value}" for key, value in entry.items()]))

def add_entry(filename):
    """Добавляет новую запись о расходе или доходе."""
    entry = {}
    print("Введите информацию о записи:")
    entry["Дата"] = input("Дата (гггг-мм-дд): ")
    entry["Категория"] = input("Категория: ")
    entry["Сумма"] = float(input("Сумма: "))
    entry["Описание"] = input("Описание: ")

    with open(filename, 'r+') as f:
        data = json.load(f)
        data.append(entry)
        f.seek(0)
        json.dump(data, f)

    print("Новая запись успешно добавлена.")

def main():
    filename = 'transactions.json'
    initial_data = []

    # Записываем исходные данные в файл
    write_to_json(initial_data, filename)

    while True:
        print("\nМеню:")
        print("1. Просмотреть все транзакции")
        print("2. Добавить новую транзакцию")
        print("3. Выйти")

        choice = input("Выберите действие: ")

        if choice == "1":
            # Читаем и выводим все транзакции из файла
            read_from_json(filename)
        elif choice == "2":
            # Добавляем новую транзакцию
            add_entry(filename)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
