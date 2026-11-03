"""
Урок 10.1 "Классы, объекты, атрибуты и методы", шаг 4

Создайте класс `Laptop`. Считайте бренд и модель (каждое с новой строки), сохраните их в атрибутах
объекта и реализуйте метод `show()`, который выводит `Laptop: {бренд} {модель}`. Создайте объект и
вызовите метод.
"""

class Laptop:
    def show(self):
        print(f"Laptop: {self.brand} {self.model}")


laptop = Laptop()
laptop.brand = input()
laptop.model = input()
laptop.show()
