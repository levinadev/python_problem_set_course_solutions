"""
Урок 10.2 "Магические методы (__init__, __str__)", шаг 2

Создайте класс `Person`.

Реализуйте конструктор `__init__()`, который принимает имя и возраст.

Создайте объект класса и выведите имя и возраст.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p = Person(input(), int(input()))
print(p.name)
print(p.age)
