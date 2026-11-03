"""
Урок 10.5 "Полиморфизм", шаг 4

Создайте классы `Square` и `Rectangle`.

В каждом классе:

- реализуйте конструктор `__init__()`;
- сохраните переданные значения в атрибутах объекта;
- реализуйте метод `area()`, который возвращает площадь фигуры.

Для класса `Square` конструктор принимает длину стороны.

Для класса `Rectangle` конструктор принимает ширину и высоту.

Используйте следующие формулы:

- площадь квадрата = `сторона × сторона`;
- площадь прямоугольника = `ширина × высота`.

Создайте объекты обоих классов и выведите площади.
"""

class Square:
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height


s = Square(int(input()))
r = Rectangle(int(input()), int(input()))
print(s.area())
print(r.area())
