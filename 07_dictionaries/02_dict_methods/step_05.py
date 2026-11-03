"""
Урок 7.2 "Методы словарей", шаг 5

Дан словарь `data = {"name": "Alice", "age": 30, "city": "Paris"}`. Считайте ключ (он точно есть в
словаре), удалите его и выведите словарь.
"""

data = {"name": "Alice", "age": 30, "city": "Paris"}
key = input()
del data[key]
print(data)
