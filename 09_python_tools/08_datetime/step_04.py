"""
Урок 9.8 "Дата и время: модуль datetime", шаг 4

Считайте дату в формате `ДД.ММ.ГГГГ` и целое число `n` (каждое с новой строки). Выведите дату,
которая наступит через `n` дней, в том же формате. Число `n` может быть отрицательным.
"""

from datetime import datetime, timedelta

d = datetime.strptime(input(), "%d.%m.%Y")
n = int(input())
print((d + timedelta(days=n)).strftime("%d.%m.%Y"))
