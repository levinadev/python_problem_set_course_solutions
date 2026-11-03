"""
Урок 9.1 "zip() и enumerate()", шаг 7

Даны две строки с одинаковым количеством целых чисел через пробел. С помощью `zip()` получите список
попарных сумм и выведите его.
"""

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
print([x + y for x, y in zip(a, b)])
