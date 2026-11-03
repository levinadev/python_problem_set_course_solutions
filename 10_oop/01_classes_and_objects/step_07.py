"""
Урок 10.1 "Классы, объекты, атрибуты и методы", шаг 7

Создайте класс `BankAccount` с атрибутом `balance` и методами `deposit(amount)` и
`withdraw(amount)`. Если на счёте недостаточно денег, `withdraw` выводит `Недостаточно средств` и не
меняет баланс.

В первой строке начальный баланс, во второй количество операций `k`, далее `k` строк вида `deposit
100` или `withdraw 50`. Выполните операции и в конце выведите `Баланс: {balance}`.
"""

class BankAccount:
    def __init__(self, balance):
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Недостаточно средств")
        else:
            self.balance -= amount


account = BankAccount(int(input()))
for _ in range(int(input())):
    action, amount = input().split()
    if action == "deposit":
        account.deposit(int(amount))
    else:
        account.withdraw(int(amount))
print(f"Баланс: {account.balance}")
