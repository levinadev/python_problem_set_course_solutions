"""
Урок 8.5 "Области видимости и замыкания", шаг 4

Напишите функцию `make_counter()`, которая возвращает функцию-счётчик: при каждом вызове она
возвращает следующее число, начиная с 1 (используйте `nonlocal`). Считайте натуральное число `n`,
вызовите счётчик `n` раз и выведите полученные числа через пробел.
"""

def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count
    return counter


c = make_counter()
print(" ".join(str(c()) for _ in range(int(input()))))
