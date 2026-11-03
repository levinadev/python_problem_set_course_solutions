"""
Урок 10.4 "Наследование", шаг 3

Создайте класс `Person`, конструктор которого принимает имя. Создайте класс `Employee`,
наследующийся от `Person`. В конструкторе `Employee` вызовите конструктор родителя через `super()`,
чтобы сохранить имя, и сохраните должность. Считайте имя и должность (каждое с новой строки),
создайте объект `Employee` и выведите `{имя}: {должность}`.
"""

class Person:
    def __init__(self, name):
        self.name = name


class Employee(Person):
    def __init__(self, name, position):
        super().__init__(name)
        self.position = position


e = Employee(input(), input())
print(f"{e.name}: {e.position}")
