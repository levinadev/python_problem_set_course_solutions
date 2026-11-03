"""
Урок 9.6 "Полезные функции Python (min, max, sum, abs, round, len)", шаг 7

На вход подаётся строка из целых чисел через пробел. Выведите размах, то есть разность между
максимальным и минимальным числом.
"""

numbers = [int(x) for x in input().split()]
print(max(numbers) - min(numbers))
