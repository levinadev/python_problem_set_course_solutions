"""
Урок 8.6 "Декораторы", шаг 4

Напишите декоратор с параметром `repeat(n)`, который вызывает украшенную функцию `n` раз. Считайте
число `n` и строку. Объявите функцию `say(text)`, которая выводит текст, украсьте её `@repeat(n)` и
вызовите со считанной строкой.
"""

def repeat(n):
    def decorator(func):
        def wrapper(*args):
            for _ in range(n):
                func(*args)
        return wrapper
    return decorator


n = int(input())


@repeat(n)
def say(text):
    print(text)


say(input())
