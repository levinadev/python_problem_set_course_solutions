"""
Урок 10.5 "Полиморфизм", шаг 6

Создайте классы `EnglishGreeter`, `RussianGreeter` и `SpanishGreeter` с методом `greet(name)`,
который возвращает `Hello, {name}!`, `Привет, {name}!` и `¡Hola, {name}!` соответственно.

Считайте код языка (`en`, `ru` или `es`) и строку с именами через пробел. Для каждого имени выведите
приветствие на выбранном языке на отдельной строке.
"""

class EnglishGreeter:
    def greet(self, name):
        return f"Hello, {name}!"


class RussianGreeter:
    def greet(self, name):
        return f"Привет, {name}!"


class SpanishGreeter:
    def greet(self, name):
        return f"¡Hola, {name}!"


greeter = {"en": EnglishGreeter(), "ru": RussianGreeter(), "es": SpanishGreeter()}[input()]
for name in input().split():
    print(greeter.greet(name))
