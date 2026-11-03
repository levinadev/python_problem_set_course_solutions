"""
Урок 7.3 "Подсчёт и группировка: Counter и defaultdict", шаг 3

На вход подаётся строка из слов через пробел. Выведите слово, которое встречается чаще всего. Если
таких слов несколько, выведите то, что встретилось в строке раньше.
"""

words = input().split()
best = words[0]
for w in words:
    if words.count(w) > words.count(best):
        best = w
print(best)
