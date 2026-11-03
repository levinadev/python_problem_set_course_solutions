"""
Урок 7.3 "Подсчёт и группировка: Counter и defaultdict", шаг 4

На вход подаётся строка из различных слов через пробел. Сгруппируйте слова по первой букве. Для
каждой буквы в алфавитном порядке выведите строку `буква: слова`, где слова перечислены через пробел
в исходном порядке.
"""

from collections import defaultdict

groups = defaultdict(list)
for w in input().split():
    groups[w[0]].append(w)
for letter in sorted(groups):
    print(f"{letter}: {' '.join(groups[letter])}")
