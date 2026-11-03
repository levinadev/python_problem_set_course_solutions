"""
Урок 9.7 "Итераторы и генераторы (yield)", шаг 7

Создайте класс-итератор `Squares`: конструктор принимает `n`, а объект при переборе выдаёт квадраты
чисел от 1 до `n`. Реализуйте методы `__iter__()` и `__next__()` (в конце вызовите `StopIteration`).
Считайте натуральное `n` и выведите значения через пробел, перебрав объект циклом.
"""

class Squares:
    def __init__(self, n):
        self.n = n
        self.i = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.i >= self.n:
            raise StopIteration
        self.i += 1
        return self.i ** 2


print(" ".join(str(x) for x in Squares(int(input()))))
