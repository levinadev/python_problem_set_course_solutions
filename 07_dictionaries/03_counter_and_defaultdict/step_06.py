"""
Урок 7.3 "Подсчёт и группировка: Counter и defaultdict", шаг 6

В первой строке количество записей `n`, далее `n` строк вида `имя оценка`. Одно имя может
встречаться несколько раз. Для каждого ученика в порядке первого появления выведите `имя: средняя
оценка` с одним знаком после точки.
"""

grades = {}
for _ in range(int(input())):
    name, g = input().split()
    grades.setdefault(name, []).append(int(g))
for name, g in grades.items():
    print(f"{name}: {sum(g) / len(g):.1f}")
