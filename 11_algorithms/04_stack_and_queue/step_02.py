"""
Урок 11.4 "Стек и очередь", шаг 2

Считайте строку из круглых скобок и выведите `True`, если скобки расставлены правильно (каждой
открывающей соответствует закрывающая после неё), иначе `False`.
"""

balance = 0
ok = True
for ch in input():
    balance += 1 if ch == "(" else -1
    if balance < 0:
        ok = False
        break
print(ok and balance == 0)
