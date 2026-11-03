"""
Урок 6.5 "Вложенные списки и матрицы", шаг 2

Дана матрица. Выведите сумму всех её элементов.

Формат ввода: в первой строке количество строк матрицы `n`, далее `n` строк с целыми числами через
пробел. Считать матрицу можно так: `matrix = [[int(x) for x in input().split()] for _ in
range(int(input()))]`
"""

matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]
print(sum(sum(row) for row in matrix))
