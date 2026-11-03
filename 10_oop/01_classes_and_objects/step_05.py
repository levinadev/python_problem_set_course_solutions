"""
Урок 10.1 "Классы, объекты, атрибуты и методы", шаг 5

Создайте класс `Rectangle`.

После создания объекта присвойте ему атрибуты `width` и `height`.

Добавьте метод `area()`, который выводит площадь прямоугольника.
"""

class Rectangle:
    def area(self):
        print(self.width * self.height)


r = Rectangle()
r.width = int(input())
r.height = int(input())
r.area()
