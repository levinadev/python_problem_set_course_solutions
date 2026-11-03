"""
Урок 11.5 "Итоговые задачи", шаг 6

Считайте натуральное число от 1 до 3999 и выведите его запись римскими цифрами (I, V, X, L, C, D, M;
для 4, 9, 40, 90, 400, 900 используются IV, IX, XL, XC, CD, CM).
"""

ROMAN = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"), (90, "XC"),
         (50, "L"), (40, "XL"), (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")]

n = int(input())
result = ""
for value, symbol in ROMAN:
    while n >= value:
        result += symbol
        n -= value
print(result)
