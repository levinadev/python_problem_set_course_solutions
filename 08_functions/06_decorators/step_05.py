"""
Урок 8.6 "Декораторы", шаг 5

Напишите декоратор `count_calls`, который считает, сколько раз была вызвана функция, и хранит это
число в атрибуте `calls` функции-обёртки. Украсьте им функцию `ping()`, которая ничего не делает.
Считайте целое неотрицательное число `k`, вызовите `ping()` `k` раз и выведите `ping.calls`.
"""

def count_calls(func):
    def wrapper(*args):
        wrapper.calls += 1
        return func(*args)
    wrapper.calls = 0
    return wrapper


@count_calls
def ping():
    pass


for _ in range(int(input())):
    ping()
print(ping.calls)
