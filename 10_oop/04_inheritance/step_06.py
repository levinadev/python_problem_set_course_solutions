"""
Урок 10.4 "Наследование", шаг 6

Создайте класс `Shape` с методом `area()`, возвращающим 0, и наследников `Rectangle(a, b)` и
`Circle(r)` со своими методами `area()`. Площадь круга считайте как `math.pi * r ** 2`.

На вход подаётся одна строка: `rect a b` или `circle r` (числа целые). Создайте нужную фигуру и
выведите её площадь, округлённую функцией `round()` до двух знаков.
"""

import math


class Shape:
    def area(self):
        return 0


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2


parts = input().split()
if parts[0] == "rect":
    shape = Rectangle(int(parts[1]), int(parts[2]))
else:
    shape = Circle(int(parts[1]))
print(round(shape.area(), 2))
