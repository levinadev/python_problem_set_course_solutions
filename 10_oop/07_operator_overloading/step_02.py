"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 2

Создайте класс `Vector` с координатами `x` и `y`. Реализуйте `__add__()` (сложение векторов) и
`__str__()` (строка `Vector(x, y)`). Считайте два вектора из двух строк, в каждой по два целых числа
через пробел. Выведите их сумму.
"""

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __str__(self):
        return f"Vector({self.x}, {self.y})"


a = Vector(*map(int, input().split()))
b = Vector(*map(int, input().split()))
print(a + b)
