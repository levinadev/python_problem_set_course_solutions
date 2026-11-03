"""
Урок 10.3 "Инкапсуляция", шаг 6

Создайте класс `User` с приватным атрибутом `__password` и методом `check_password(p)`, который
возвращает `True`, если пароль совпадает, иначе `False`. Считайте пароль и попытку ввода (каждое с
новой строки) и выведите результат проверки.
"""

class User:
    def __init__(self, password):
        self.__password = password

    def check_password(self, p):
        return p == self.__password


user = User(input())
print(user.check_password(input()))
