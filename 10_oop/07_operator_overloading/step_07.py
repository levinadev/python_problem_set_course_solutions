"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 7

Создайте класс `Fraction` (числитель и знаменатель являются натуральными числами, дробь хранится в
сокращённом виде). Реализуйте `__add__()` и `__str__()` (строка `a/b`). Считайте две дроби в виде
`a/b` (каждую с новой строки) и выведите их сумму.
"""

import math


class Fraction:
    def __init__(self, num, den):
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __add__(self, other):
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __str__(self):
        return f"{self.num}/{self.den}"


a = Fraction(*map(int, input().split("/")))
b = Fraction(*map(int, input().split("/")))
print(a + b)
