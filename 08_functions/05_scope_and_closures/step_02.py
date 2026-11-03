"""
Урок 8.5 "Области видимости и замыкания", шаг 2

Создайте глобальную переменную `visits = 0` и функцию `add_visit()`, которая увеличивает её на 1
(используйте `global`). Считайте целое неотрицательное число `n`, вызовите функцию `n` раз и
выведите `visits`.
"""

visits = 0


def add_visit():
    global visits
    visits += 1


for _ in range(int(input())):
    add_visit()
print(visits)
