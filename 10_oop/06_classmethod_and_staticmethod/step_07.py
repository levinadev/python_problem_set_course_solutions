"""
Урок 10.6 "Методы класса и статические методы", шаг 7

Создайте класс `Currency` с атрибутом класса `rate = 90` (курс доллара), методом класса
`set_rate(new_rate)`, меняющим курс для всех объектов, и методом `to_rub(self, usd)`. Считайте новый
курс и строку с суммами в долларах (целые числа через пробел). Установите курс через `set_rate` и
выведите через пробел суммы в рублях.
"""

class Currency:
    rate = 90

    @classmethod
    def set_rate(cls, new_rate):
        cls.rate = new_rate

    def to_rub(self, usd):
        return usd * self.rate


Currency.set_rate(int(input()))
c = Currency()
print(" ".join(str(c.to_rub(int(x))) for x in input().split()))
