import unittest
import json
from main import write_to_json, read_from_json, add_entry

class TestTransactions(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Подготовим тестовые данные и сохраняем их в файл
        cls.data = [
            {"Дата": "2024-05-02", "Категория": "Расход", "Сумма": 1500, "Описание": "Покупка продуктов"},
            {"Дата": "2024-05-03", "Категория": "Доход", "Сумма": 2000, "Описание": "Зарплата"}
        ]
        cls.filename = 'test_transactions.json'
        write_to_json(cls.data, cls.filename)

    def test_write_to_json(self):
        # Вызываем тестируемую функцию
        write_to_json(self.data, self.filename)

        # Проверяем, что файл содержит правильные данные
        with open(self.filename, 'r') as f:
            written_data = json.load(f)
        self.assertEqual(self.data, written_data)

    def test_read_from_json(self):
        # Вызываем тестируемую функцию
        read_data = read_from_json(self.filename)

        # Проверяем, что данные были успешно прочитаны и соответствуют ожидаемым
        self.assertEqual(self.data, read_data)

    def test_add_entry(self):
        # Подготовим тестовые данные
        new_entry = {"Дата": "2024-05-04", "Категория": "Доход", "Сумма": 3000, "Описание": "Премия"}

        # Вызываем тестируемую функцию
        add_entry(self.filename, new_entry["Дата"], new_entry["Категория"], new_entry["Сумма"], new_entry["Описание"])

        # Проверяем, что новая запись была успешно добавлена в файл
        with open(self.filename, 'r') as f:
            updated_data = json.load(f)
        self.assertIn(new_entry, updated_data)

if __name__ == '__main__':
    unittest.main()
