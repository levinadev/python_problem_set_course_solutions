"""
Урок 10.4 "Наследование", шаг 5

Создайте класс `Employee`, конструктор которого принимает имя и оклад, с методом `salary()`,
возвращающим оклад. Создайте наследника `Manager`, который дополнительно принимает премию, а его
метод `salary()` возвращает оклад плюс премия (вызовите родительский метод через `super()`).

Считайте имя, оклад и премию (каждое с новой строки). Создайте менеджера и выведите `{имя}:
{зарплата}`.
"""

class Employee:
    def __init__(self, name, base):
        self.name = name
        self.base = base

    def salary(self):
        return self.base


class Manager(Employee):
    def __init__(self, name, base, bonus):
        super().__init__(name, base)
        self.bonus = bonus

    def salary(self):
        return super().salary() + self.bonus


m = Manager(input(), int(input()), int(input()))
print(f"{m.name}: {m.salary()}")
