"""
Урок 10.5 "Полиморфизм", шаг 5

Создайте классы `Card`, `Cash` и `Crypto`. В каждом реализуйте метод `pay(amount)`, который
возвращает итоговую сумму к оплате: для карты это сумма плюс 2% комиссии, для наличных сумма без
изменений, для криптовалюты сумма плюс 5% комиссии.

Считайте способ оплаты (`card`, `cash` или `crypto`) и сумму (целое число), каждое с новой строки.
Вызовите `pay()` у нужного объекта и выведите результат с двумя знаками после точки.
"""

class Card:
    def pay(self, amount):
        return amount * 1.02


class Cash:
    def pay(self, amount):
        return amount


class Crypto:
    def pay(self, amount):
        return amount * 1.05


methods = {"card": Card(), "cash": Cash(), "crypto": Crypto()}
method = methods[input()]
print(f"{method.pay(int(input())):.2f}")
