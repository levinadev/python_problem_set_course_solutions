"""
Урок 4.1 "Цикл for", шаг 6

Считайте строку и выведите, сколько в ней латинских гласных букв `a`, `e`, `i`, `o`, `u` (без учёта
регистра).
"""

text = input().lower()
count = 0
for ch in text:
    if ch in "aeiou":
        count += 1
print(count)
