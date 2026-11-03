"""
Урок 10.2 "Магические методы (__init__, __str__)", шаг 5

Создайте класс `Student`, конструктор которого принимает имя и список оценок. Реализуйте
`__str__()`, возвращающий строку `{имя}: средний балл {среднее}`, где среднее выведено с одним
знаком после точки. Считайте имя и оценки (во второй строке, через пробел) и выведите объект.
"""

class Student:
    def __init__(self, name, grades):
        self.name = name
        self.grades = grades

    def __str__(self):
        return f"{self.name}: средний балл {sum(self.grades) / len(self.grades):.1f}"


name = input()
grades = [int(x) for x in input().split()]
print(Student(name, grades))
