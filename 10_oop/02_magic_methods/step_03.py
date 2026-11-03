"""
Урок 10.2 "Магические методы (__init__, __str__)", шаг 3

Создайте класс `Book`.

Конструктор принимает название книги и имя автора.

Реализуйте метод `__str__()`, который возвращает строку в формате

    Название - Автор

Выведите объект с помощью `print()`.
"""

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"{self.title} - {self.author}"


book = Book(input(), input())
print(book)
