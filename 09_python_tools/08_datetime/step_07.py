"""
Урок 9.8 "Дата и время: модуль datetime", шаг 7

Считайте номер месяца и год (каждое с новой строки) и выведите, сколько дней в этом месяце.
"""

import calendar

month = int(input())
year = int(input())
print(calendar.monthrange(year, month)[1])
