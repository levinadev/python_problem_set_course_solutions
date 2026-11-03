"""
Урок 10.6 "Методы класса и статические методы", шаг 6

Создайте класс `Validator` со статическим методом `is_email(s)`. Он возвращает `True`, если в строке
ровно один символ `@`, перед ним есть хотя бы один символ, а после него есть точка, которая не стоит
сразу после `@` и не является последним символом. Иначе возвращает `False`. Считайте строку и
выведите результат.
"""

class Validator:
    @staticmethod
    def is_email(s):
        if s.count("@") != 1:
            return False
        user, domain = s.split("@")
        dot = domain.rfind(".")
        return len(user) > 0 and dot > 0 and dot < len(domain) - 1


print(Validator.is_email(input()))
