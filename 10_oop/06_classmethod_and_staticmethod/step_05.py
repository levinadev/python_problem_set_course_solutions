"""
Урок 10.6 "Методы класса и статические методы", шаг 5

Создайте класс `Date` с атрибутами `day`, `month`, `year`, методом класса `from_iso(s)`, создающим
дату из строки `ГГГГ-ММ-ДД`, и методом `__str__()`, возвращающим дату в формате `ДД.ММ.ГГГГ` (день и
месяц двумя цифрами). Считайте строку, создайте объект и выведите его.
"""

class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_iso(cls, s):
        year, month, day = map(int, s.split("-"))
        return cls(day, month, year)

    def __str__(self):
        return f"{self.day:02d}.{self.month:02d}.{self.year}"


print(Date.from_iso(input()))
