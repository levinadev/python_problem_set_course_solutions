"""
Урок 8.3 "lambda, map, filter", шаг 4

На вход подаётся строка из слов через пробел. Используя `filter`, оставьте только слова длиной
больше 3 и выведите получившийся список.
"""

words = input().split()
print(list(filter(lambda w: len(w) > 3, words)))
