"""
Урок 3.3 "Вложенные условия", шаг 2

Считайте число. Если оно больше 0, выведите `Positive`, если меньше 0, выведите `Negative`, иначе
`Zero`.
"""

n = int(input())
if n > 0:
    print("Positive")
elif n < 0:
    print("Negative")
else:
    print("Zero")
