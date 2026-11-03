"""
Урок 9.6 "Полезные функции Python (min, max, sum, abs, round, len)", шаг 2

Даны пять целых чисел.

Выведите минимальное, а затем максимальное число.
"""

numbers = [int(input()) for _ in range(5)]
print(min(numbers))
print(max(numbers))
