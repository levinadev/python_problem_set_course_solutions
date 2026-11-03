"""
Урок 8.5 "Области видимости и замыкания", шаг 6

Напишите функцию `make_accumulator()`, которая возвращает функцию `add(x)`: она прибавляет `x` к
накопленной сумме и возвращает новую сумму. Считайте строку с целыми числами через пробел, передайте
их по очереди в `add` и выведите все промежуточные суммы через пробел.
"""

def make_accumulator():
    total = 0

    def add(x):
        nonlocal total
        total += x
        return total
    return add


add = make_accumulator()
print(" ".join(str(add(int(x))) for x in input().split()))
