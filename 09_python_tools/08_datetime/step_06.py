"""
Урок 9.8 "Дата и время: модуль datetime", шаг 6

Считайте время в формате `ЧЧ:ММ` и целое неотрицательное число минут (каждое с новой строки).
Выведите, какое время будет через это количество минут, в формате `ЧЧ:ММ`.
"""

from datetime import datetime, timedelta

t = datetime.strptime(input(), "%H:%M")
print((t + timedelta(minutes=int(input()))).strftime("%H:%M"))
