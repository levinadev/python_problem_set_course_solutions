"""
Урок 10.4 "Наследование", шаг 4

Создайте класс `Animal`, конструктор которого принимает имя, и метод `speak()`, возвращающий `...`.
Создайте наследников `Dog` и `Cat`, в которых `speak()` возвращает `Woof` и `Meow`.

Считайте вид животного (`dog`, `cat` или другое слово) и имя (каждое с новой строки). Создайте
объект нужного класса и выведите `{имя} says {звук}`.
"""

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return "..."


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"


kind = input()
name = input()
classes = {"dog": Dog, "cat": Cat}
animal = classes.get(kind, Animal)(name)
print(f"{animal.name} says {animal.speak()}")
