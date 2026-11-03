"""
Урок 8.3 "lambda, map, filter", шаг 6

На вход подаётся строка из целых чисел через пробел. С помощью `filter` и `lambda` оставьте только
чётные числа и выведите получившийся список.
"""

numbers = map(int, input().split())
print(list(filter(lambda x: x % 2 == 0, numbers)))
