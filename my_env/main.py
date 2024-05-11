import json
from datetime import datetime

def write_to_json(data, filename):
    """Записывает данные в JSON файл."""
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)
    print("Данные успешно записаны в файл.")

def read_from_json(filename):
    """Читает данные из JSON файла и возвращает их."""
    with open(filename, 'r') as f:
        data = json.load(f)
    return data

def add_entry(filename, date, category, amount, description):
    """Добавляет новую запись о расходе или доходе."""
    entry = {
        "Дата": date,
        "Категория": category,
        "Сумма": amount,
        "Описание": description
    }

    try:
        # Подтверждение перед сохранением данных в файл
        confirmation = input("Хотите сохранить эту запись? (y/n): ")
        if confirmation.lower() == "y" or "д":
            with open(filename, 'r+') as f:
                data = json.load(f)
                data.append(entry)
                f.seek(0)
                json.dump(data, f, indent=4)
                print("Новая запись успешно добавлена.")
        else:
            print("Добавление записи отменено.")
    except Exception as e:
        print(f"Ошибка при добавлении записи: {e}")

def main():
    """Основная функция программы."""
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
            data = read_from_json(filename)
            for entry in data:
                print("\n".join([f"{key}: {value}" for key, value in entry.items()]))
                print()
        elif choice == "2":
            # Добавляем новую транзакцию
            date = input("Введите дату (ДД-ММ-ГГГГ): ")
            category = input("Введите категорию: ")
            amount = float(input("Введите сумму: "))
            description = input("Введите описание: ")
            add_entry(filename, date, category, amount, description)
        elif choice == "3":
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
