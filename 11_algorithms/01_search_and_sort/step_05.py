"""
Урок 11.1 "Поиск и сортировка", шаг 5

На вход подаётся строка из целых чисел через пробел (различных значений не меньше двух). Выведите
второе по величине различное значение. Решите задачу за один проход по списку, без сортировки.
"""

numbers = [int(x) for x in input().split()]
first = second = None
for x in numbers:
    if first is None or x > first:
        first, second = x, first
    elif x != first and (second is None or x > second):
        second = x
print(second)
