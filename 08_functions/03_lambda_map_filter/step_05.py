"""
Урок 8.3 "lambda, map, filter", шаг 5

На вход подаётся строка из целых чисел через пробел. С помощью `map` и `lambda` получите список, где
каждое число удвоено, и выведите его.
"""

numbers = map(int, input().split())
print(list(map(lambda x: x * 2, numbers)))
