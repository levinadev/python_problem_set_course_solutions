"""
Урок 9.3 "Функции any(), all(), sorted()", шаг 4

На вход подаётся строка из целых чисел через пробел. Отсортируйте их по убыванию и выведите
получившийся список.
"""

numbers = [int(x) for x in input().split()]
print(sorted(numbers, reverse=True))
