"""
Урок 10.5 "Полиморфизм", шаг 2

Создайте классы `Dog` и `Cat`.

В каждом классе реализуйте метод `sound()`:

- класс `Dog` должен выводить `Woof!`;
- класс `Cat` должен выводить `Meow!`.

Создайте список из объектов этих классов и с помощью цикла вызовите метод `sound()` для каждого
объекта.
"""

class Dog:
    def sound(self):
        print("Woof!")


class Cat:
    def sound(self):
        print("Meow!")


for animal in [Dog(), Cat()]:
    animal.sound()
