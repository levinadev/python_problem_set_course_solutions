"""
Урок 11.1 "Поиск и сортировка", шаг 6

Слияние. Даны две строки с целыми числами через пробел, каждая отсортирована по возрастанию.
Объедините их в один отсортированный список, не используя `sort()` и `sorted()`: двигайтесь по обоим
спискам указателями и каждый раз берите меньший элемент. Выведите числа через пробел.
"""

a = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
i = j = 0
result = []
while i < len(a) and j < len(b):
    if a[i] <= b[j]:
        result.append(a[i])
        i += 1
    else:
        result.append(b[j])
        j += 1
result += a[i:] + b[j:]
print(" ".join(map(str, result)))
