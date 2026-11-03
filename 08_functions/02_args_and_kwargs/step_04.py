"""
Урок 8.2 "Аргументы по умолчанию, *args, **kwargs", шаг 4

Напишите функцию `display(**kwargs)`, которая выводит все пары ключ-значение в формате `ключ:
значение`, каждую на новой строке. Считайте название товара и его цену (каждое с новой строки) и
вызовите функцию с аргументами `product=...` и `price=...`.
"""

def display(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")


product = input()
price = int(input())
display(product=product, price=price)
