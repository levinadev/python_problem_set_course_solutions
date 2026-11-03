"""
Урок 10.6 "Методы класса и статические методы", шаг 4

Создайте класс `Ticket` с атрибутом класса `count = 0`. При создании каждого билета счётчик
увеличивается, а билет получает атрибут `number` со своим порядковым номером. Считайте натуральное
число `n`, создайте `n` билетов, выведите для каждого `Билет №{number}`, а затем `Всего билетов:
{Ticket.count}`.
"""

class Ticket:
    count = 0

    def __init__(self):
        Ticket.count += 1
        self.number = Ticket.count


tickets = [Ticket() for _ in range(int(input()))]
for t in tickets:
    print(f"Билет №{t.number}")
print(f"Всего билетов: {Ticket.count}")
