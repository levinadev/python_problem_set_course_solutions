"""
Урок 9.7 "Итераторы и генераторы (yield)", шаг 3

Напишите генератор `even_numbers(limit)`, который выдаёт чётные числа от 0 до `limit` включительно.
Считайте целое неотрицательное число и выведите значения генератора через пробел.
"""

def even_numbers(limit):
    for i in range(0, limit + 1, 2):
        yield i


print(*even_numbers(int(input())))
