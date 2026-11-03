"""
Урок 8.4 "Рекурсия", шаг 2

Напишите рекурсивную функцию `factorial(n)` (без циклов). Считайте целое неотрицательное число и
выведите его факториал. Помните: `0! = 1`.
"""

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)


print(factorial(int(input())))
