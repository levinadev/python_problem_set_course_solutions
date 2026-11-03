"""
Урок 10.5 "Полиморфизм", шаг 3

Создайте классы `Developer` и `Designer`.

В каждом классе реализуйте метод `work()`:

- класс `Developer` должен выводить:

    Writing code

- класс `Designer` должен выводить:

    Creating design

Создайте список сотрудников и с помощью цикла вызовите метод `work()` для каждого объекта.
"""

class Developer:
    def work(self):
        print("Writing code")


class Designer:
    def work(self):
        print("Creating design")


for worker in [Developer(), Designer()]:
    worker.work()
