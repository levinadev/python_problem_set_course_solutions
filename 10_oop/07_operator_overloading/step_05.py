"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 5

Создайте класс `Library`, конструктор которого принимает список книг. Реализуйте `__contains__()`,
чтобы работал оператор `in` (без учёта регистра). Считайте строку с названиями книг через `;` и
название для поиска. Выведите `True` или `False`.
"""

class Library:
    def __init__(self, books):
        self.books = [b.lower() for b in books]

    def __contains__(self, title):
        return title.lower() in self.books


lib = Library(input().split(";"))
print(input() in lib)
