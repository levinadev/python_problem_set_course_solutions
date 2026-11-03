"""
Урок 10.3 "Инкапсуляция", шаг 4

Создайте класс `Worker` с приватным атрибутом `__salary`. Реализуйте: конструктор `__init__()`;
свойство `salary` с помощью декоратора `@property`; сеттер `salary` с помощью декоратора
`@salary.setter`. Считайте начальную и новую зарплату (каждую с новой строки). Создайте объект с
начальной зарплатой, измените зарплату через сеттер и выведите новое значение.
"""

class Worker:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        self.__salary = value


w = Worker(int(input()))
w.salary = int(input())
print(w.salary)
