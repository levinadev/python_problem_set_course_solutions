"""
Урок 11.1 "Поиск и сортировка", шаг 2

Линейный поиск. В первой строке целые числа через пробел, во второй число `x`. Выведите индекс
первого вхождения `x` в список или `-1`, если его нет. Не используйте методы `index()` и `find()`,
пройдите по списку циклом.
"""

numbers = [int(x) for x in input().split()]
x = int(input())
result = -1
for i in range(len(numbers)):
    if numbers[i] == x:
        result = i
        break
print(result)
