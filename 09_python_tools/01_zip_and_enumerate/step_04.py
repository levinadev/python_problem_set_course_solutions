"""
Урок 9.1 "zip() и enumerate()", шаг 4

Даны три строки: имена, возрасты и страны (через пробел, в каждой строке одинаковое количество).
Используя `zip`, выведите для каждого человека строку `Имя: {name}, Возраст: {age}, Страна:
{country}`.
"""

names = input().split()
ages = input().split()
countries = input().split()
for name, age, country in zip(names, ages, countries):
    print(f"Имя: {name}, Возраст: {age}, Страна: {country}")
