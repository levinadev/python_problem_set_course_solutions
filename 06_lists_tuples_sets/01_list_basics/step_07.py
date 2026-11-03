"""
Урок 6.1 "Основы списков", шаг 7

На вход подаётся строка из целых чисел через пробел. Замените в списке все отрицательные числа на 0
и выведите список.
"""

numbers = [int(x) for x in input().split()]
for i in range(len(numbers)):
    if numbers[i] < 0:
        numbers[i] = 0
print(numbers)
