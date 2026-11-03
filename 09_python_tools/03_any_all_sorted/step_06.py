"""
Урок 9.3 "Функции any(), all(), sorted()", шаг 6

На вход подаётся строка из целых чисел через пробел. С помощью `all()` проверьте, все ли числа
чётные, и выведите `True` или `False`.
"""

numbers = [int(x) for x in input().split()]
print(all(x % 2 == 0 for x in numbers))
