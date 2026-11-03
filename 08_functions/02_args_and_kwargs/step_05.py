"""
Урок 8.2 "Аргументы по умолчанию, *args, **kwargs", шаг 5

Напишите функцию `welcome(title, name="Guest")`, которая выводит `{title}, {name}!`. Считайте звание
и имя (каждое с новой строки). Вызовите функцию сначала с обоими аргументами, затем только со
званием.
"""

def welcome(title, name="Guest"):
    print(f"{title}, {name}!")


title = input()
name = input()
welcome(title, name)
welcome(title)
