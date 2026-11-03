"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 3

Создайте класс `Money`, конструктор которого принимает рубли и копейки. Реализуйте `__eq__()` и
`__lt__()`, сравнивающие суммы. Считайте две суммы из двух строк вида `рубли копейки`. Выведите
через пробел результаты `a == b`, `a < b` и `a > b`.
"""

class Money:
    def __init__(self, rub, kop):
        self.total = rub * 100 + kop

    def __eq__(self, other):
        return self.total == other.total

    def __lt__(self, other):
        return self.total < other.total


a = Money(*map(int, input().split()))
b = Money(*map(int, input().split()))
print(a == b, a < b, a > b)
