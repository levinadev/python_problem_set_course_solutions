"""
Урок 10.4 "Наследование", шаг 2

Создайте класс `Vehicle` с методом `move()`, который выводит:

    Vehicle is moving

Создайте класс `Bike`, наследующийся от класса `Vehicle`.

Переопределите в нем метод `move()`, чтобы он выводил:

    Bike is moving

Создайте объект класса `Bike` и вызовите метод `move()`.
"""

class Vehicle:
    def move(self):
        print("Vehicle is moving")


class Bike(Vehicle):
    def move(self):
        print("Bike is moving")


Bike().move()
