"""
Урок 10.6 "Методы класса и статические методы", шаг 3

Создайте класс `Person` с атрибутами `name` и `age` и методом класса (`@classmethod`)
`from_string(s)`, который создаёт объект из строки вида `Anna,25`. Считайте такую строку, создайте
объект через `from_string` и выведите `{name} ({age})`.
"""

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls, s):
        name, age = s.split(",")
        return cls(name, int(age))


p = Person.from_string(input())
print(f"{p.name} ({p.age})")
