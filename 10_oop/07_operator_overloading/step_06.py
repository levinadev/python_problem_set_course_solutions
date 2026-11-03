"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 6

Создайте класс `Player` с атрибутами `name` и `score`. Реализуйте `__lt__()` так, чтобы игрок с
большим счётом считался "меньше" (стоял раньше при сортировке), а при равном счёте раньше шло имя,
которое меньше по алфавиту. Считайте строку вида `Anna:30 Tom:45`, отсортируйте список игроков
функцией `sorted()` без параметра `key` и выведите имена через пробел.
"""

class Player:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return (-self.score, self.name) < (-other.score, other.name)


players = []
for item in input().split():
    name, score = item.split(":")
    players.append(Player(name, int(score)))
print(" ".join(p.name for p in sorted(players)))
