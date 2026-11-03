"""
Урок 10.3 "Инкапсуляция", шаг 5

Создайте класс `Thermostat` с приватным атрибутом `__temp`, свойством `temp` (`@property`) и
сеттером. Сеттер принимает только значения от 10 до 30 включительно; иначе он выводит `Недопустимая
температура` и оставляет старое значение.

Считайте начальную температуру (она всегда допустима) и новую температуру (каждую с новой строки).
Создайте объект, присвойте `temp` новое значение и выведите `temp`.
"""

class Thermostat:
    def __init__(self, temp):
        self.__temp = temp

    @property
    def temp(self):
        return self.__temp

    @temp.setter
    def temp(self, value):
        if 10 <= value <= 30:
            self.__temp = value
        else:
            print("Недопустимая температура")


t = Thermostat(int(input()))
t.temp = int(input())
print(t.temp)
