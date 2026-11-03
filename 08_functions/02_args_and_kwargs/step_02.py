"""
Урок 8.2 "Аргументы по умолчанию, *args, **kwargs", шаг 2

Напишите функцию `greet_user(name="User")`, которая выводит `Hello, {name}!`. Считайте имя. Вызовите
функцию сначала без аргумента, затем со считанным именем.
"""

def greet_user(name="User"):
    print(f"Hello, {name}!")


name = input()
greet_user()
greet_user(name)
