"""
Урок 10.7 "Перегрузка операторов: __add__, __eq__, __lt__, __len__", шаг 4

Создайте класс `Playlist`, конструктор которого принимает список песен. Реализуйте `__len__()`
(количество песен) и `__getitem__()` (песня по индексу). Считайте строку с названиями песен через
`;`. Выведите `len(playlist)`, затем первую и последнюю песню (каждое на новой строке), обращаясь к
объекту по индексу.
"""

class Playlist:
    def __init__(self, songs):
        self.songs = songs

    def __len__(self):
        return len(self.songs)

    def __getitem__(self, i):
        return self.songs[i]


p = Playlist(input().split(";"))
print(len(p))
print(p[0])
print(p[-1])
