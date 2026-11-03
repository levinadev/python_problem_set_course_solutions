"""
Урок 9.8 "Дата и время: модуль datetime", шаг 3

Считайте две даты в формате `ДД.ММ.ГГГГ` (каждую с новой строки) и выведите, сколько дней между ними
(неотрицательное число).
"""

from datetime import datetime

a = datetime.strptime(input(), "%d.%m.%Y")
b = datetime.strptime(input(), "%d.%m.%Y")
print(abs((b - a).days))
