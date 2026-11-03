"""
Урок 10.2 "Магические методы (__init__, __str__)", шаг 4

Создайте класс `Point`, конструктор которого принимает координаты `x` и `y`. Реализуйте метод
`__str__()`, возвращающий строку `Point(x, y)`. Считайте два целых числа (каждое с новой строки),
создайте объект и выведите его с помощью `print()`.
"""

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"Point({self.x}, {self.y})"


print(Point(int(input()), int(input())))
