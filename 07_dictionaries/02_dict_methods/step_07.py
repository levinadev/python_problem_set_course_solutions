"""
Урок 7.2 "Методы словарей", шаг 7

Дан словарь `prices = {"apple": 100, "bread": 45, "milk": 80, "cheese": 350, "tea": 120}`. Считайте
сумму, целое число. С помощью метода `items()` выведите через пробел (в порядке словаря) названия
товаров, цена которых не больше этой суммы. Если таких товаров нет, выведите `Нет товаров`.
"""

prices = {"apple": 100, "bread": 45, "milk": 80, "cheese": 350, "tea": 120}
limit = int(input())
result = [name for name, price in prices.items() if price <= limit]
print(" ".join(result) if result else "Нет товаров")
