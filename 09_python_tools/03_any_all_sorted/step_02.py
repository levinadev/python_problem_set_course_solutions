"""
Урок 9.3 "Функции any(), all(), sorted()", шаг 2

На вход подаётся строка из целых чисел через пробел. С помощью `any()` проверьте, есть ли среди них
положительное число, и выведите `True` или `False`.
"""

numbers = [int(x) for x in input().split()]
print(any(x > 0 for x in numbers))
