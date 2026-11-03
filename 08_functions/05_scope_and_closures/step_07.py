"""
Урок 8.5 "Области видимости и замыкания", шаг 7

Напишите функцию `make_power(n)`, которая возвращает функцию, возводящую аргумент в степень `n`.
Создайте с её помощью функции `square = make_power(2)` и `cube = make_power(3)`. Считайте целое
число и выведите его квадрат и куб через пробел.
"""

def make_power(n):
    return lambda x: x ** n


square = make_power(2)
cube = make_power(3)
x = int(input())
print(square(x), cube(x))
