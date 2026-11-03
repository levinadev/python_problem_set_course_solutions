"""
Урок 9.8 "Дата и время: модуль datetime", шаг 5

Считайте дату рождения и текущую дату в формате `ДД.ММ.ГГГГ` (каждую с новой строки; текущая дата не
раньше даты рождения). Выведите полный возраст в годах.
"""

from datetime import datetime

b = datetime.strptime(input(), "%d.%m.%Y")
t = datetime.strptime(input(), "%d.%m.%Y")
age = t.year - b.year
if (t.month, t.day) < (b.month, b.day):
    age -= 1
print(age)
