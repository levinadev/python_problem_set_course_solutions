"""
Урок 8.6 "Декораторы", шаг 6

Напишите декоратор `memoize`, который запоминает результаты функции для уже встречавшихся аргументов
(в словаре). Украсьте им рекурсивную функцию `fib(n)` (`fib(0) = 0`, `fib(1) = 1`). Считайте `n` (до
90) и выведите `fib(n)`.

Без запоминания рекурсия для больших `n` работает слишком долго и не уложится в лимит времени.
"""

def memoize(func):
    cache = {}

    def wrapper(n):
        if n not in cache:
            cache[n] = func(n)
        return cache[n]
    return wrapper


@memoize
def fib(n):
    if n < 2:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(int(input())))
