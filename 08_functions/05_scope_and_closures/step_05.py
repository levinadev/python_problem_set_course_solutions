"""
Урок 8.5 "Области видимости и замыкания", шаг 5

Напишите функцию `make_greeting(greeting)`, которая возвращает функцию от имени, возвращающую строку
`{greeting}, {name}!`. Считайте приветствие и строку с именами через пробел. Выведите приветствие
для каждого имени на отдельной строке.
"""

def make_greeting(greeting):
    def greet(name):
        return f"{greeting}, {name}!"
    return greet


greet = make_greeting(input())
for name in input().split():
    print(greet(name))
