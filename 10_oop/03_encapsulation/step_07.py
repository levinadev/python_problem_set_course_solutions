"""
Урок 10.3 "Инкапсуляция", шаг 7

Создайте класс `Product` со свойством `price`. Сеттер должен вызывать исключение `ValueError`, если
цена отрицательная. Считайте две цены (каждую с новой строки): создайте товар с первой ценой, затем
попробуйте присвоить вторую. Если возникло исключение, выведите `Цена не может быть отрицательной`.
В конце выведите текущую цену.
"""

class Product:
    def __init__(self, price):
        self.price = price

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("negative price")
        self._price = value


p = Product(int(input()))
try:
    p.price = int(input())
except ValueError:
    print("Цена не может быть отрицательной")
print(p.price)
