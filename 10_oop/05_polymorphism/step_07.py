"""
Урок 10.5 "Полиморфизм", шаг 7

Создайте классы `Square(a)`, `Rectangle(a, b)` и `Triangle(a, h)` (основание и высота) с методом
`area()`. В первой строке количество фигур `n`, далее `n` строк вида `square 3`, `rect 2 5` или
`triangle 4 3`.

Создайте список фигур и выведите их суммарную площадь (полученное число выведите как есть, функцией
`print()`).
"""

class Square:
    def __init__(self, a):
        self.a = a

    def area(self):
        return self.a * self.a


class Rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle:
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h / 2


kinds = {"square": Square, "rect": Rectangle, "triangle": Triangle}
shapes = []
for _ in range(int(input())):
    name, *sizes = input().split()
    shapes.append(kinds[name](*map(int, sizes)))
print(sum(s.area() for s in shapes))
