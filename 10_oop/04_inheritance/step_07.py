"""
Урок 10.4 "Наследование", шаг 7

Создайте классы `A`, `B(A)` и `C(B)` (тела классов могут быть пустыми, с одним `pass`). Считайте имя
класса (`A`, `B` или `C`), создайте объект этого класса и выведите в одну строку через пробел
результаты проверок `isinstance(obj, A)`, `isinstance(obj, B)` и `isinstance(obj, C)`.
"""

class A:
    pass


class B(A):
    pass


class C(B):
    pass


obj = {"A": A, "B": B, "C": C}[input()]()
print(isinstance(obj, A), isinstance(obj, B), isinstance(obj, C))
