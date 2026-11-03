"""
Урок 9.6 "Полезные функции Python (min, max, sum, abs, round, len)", шаг 6

Даны три слова.

Выведите самое длинное из них.

Если несколько слов имеют одинаковую максимальную длину, выведите первое из них.

Используйте функцию `len()`.
"""

words = [input() for _ in range(3)]
longest = words[0]
for w in words:
    if len(w) > len(longest):
        longest = w
print(longest)
