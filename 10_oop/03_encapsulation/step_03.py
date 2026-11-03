"""
Урок 10.3 "Инкапсуляция", шаг 3

Создайте класс `Worker` с приватным атрибутом `__salary`. Реализуйте конструктор `__init__()`,
который принимает зарплату. Используя декоратор `@property`, создайте свойство `salary`, позволяющее
получить значение зарплаты. Считайте зарплату (целое число), создайте объект класса и выведите
зарплату через свойство.
"""

class Worker:
    def __init__(self, salary):
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary


w = Worker(int(input()))
print(w.salary)
