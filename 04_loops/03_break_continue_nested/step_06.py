"""
Урок 4.3 "break, continue и вложенные циклы", шаг 6

Считайте натуральное число `n`. Выведите в одну строку через пробел числа от 1 до `n`, пропуская
числа, кратные 3. Используйте `continue`.
"""

n = int(input())
result = []
for i in range(1, n + 1):
    if i % 3 == 0:
        continue
    result.append(str(i))
print(" ".join(result))
