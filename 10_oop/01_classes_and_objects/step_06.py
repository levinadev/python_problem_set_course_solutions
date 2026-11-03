"""
Урок 10.1 "Классы, объекты, атрибуты и методы", шаг 6

Создайте класс `Clicker` с атрибутом `value`, равным 0 при создании, и методом `click()`, который
увеличивает `value` на 1. Считайте целое неотрицательное число `n`, создайте объект, вызовите
`click()` `n` раз и выведите `value`.
"""

class Clicker:
    def __init__(self):
        self.value = 0

    def click(self):
        self.value += 1


c = Clicker()
for _ in range(int(input())):
    c.click()
print(c.value)
