"""
Урок 9.1 "zip() и enumerate()", шаг 2

В первой строке имена через пробел, во второй возрасты через пробел (столько же). Используя `zip`,
выведите для каждой пары строку `{name} is {age} years old`.
"""

names = input().split()
ages = input().split()
for name, age in zip(names, ages):
    print(f"{name} is {age} years old")
