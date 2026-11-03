"""
Урок 8.6 "Декораторы", шаг 2

Напишите декоратор `shout`, который переводит результат функции в верхний регистр. Украсьте им
функцию `greet(name)`, возвращающую `hello, {name}`. Считайте имя и выведите результат
`greet(name)`.

Напоминание: декоратором называют функцию, которая принимает функцию и возвращает новую
функцию-обёртку. Применяется так: `@shout` перед `def`.
"""

def shout(func):
    def wrapper(*args):
        return func(*args).upper()
    return wrapper


@shout
def greet(name):
    return f"hello, {name}"


print(greet(input()))
