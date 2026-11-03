"""
Урок 10.2 "Магические методы (__init__, __str__)", шаг 7

Создайте класс `Fraction`, конструктор которого принимает числитель и знаменатель (натуральные
числа) и сразу сокращает дробь. Реализуйте `__str__()`, возвращающий дробь в виде
`числитель/знаменатель`. Считайте два числа (каждое с новой строки) и выведите объект.
"""

import math


class Fraction:
    def __init__(self, num, den):
        g = math.gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __str__(self):
        return f"{self.num}/{self.den}"


print(Fraction(int(input()), int(input())))
