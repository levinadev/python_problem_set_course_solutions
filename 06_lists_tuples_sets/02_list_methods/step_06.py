"""
Урок 6.2 "Методы списков", шаг 6

В первой строке целые числа через пробел, во второй число `x`. Удалите из списка все вхождения `x`
(если они есть) и выведите список.
"""

numbers = [int(x) for x in input().split()]
x = int(input())
while x in numbers:
    numbers.remove(x)
print(numbers)
