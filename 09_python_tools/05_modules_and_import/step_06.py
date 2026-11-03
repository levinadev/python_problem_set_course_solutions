"""
Урок 9.5 "Модули и импорт", шаг 6

Импортируйте из модуля `math` только функцию `factorial` (`from math import factorial`). Считайте
целое неотрицательное число и выведите его факториал.
"""

from math import factorial

print(factorial(int(input())))
