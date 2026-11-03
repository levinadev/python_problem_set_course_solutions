"""
Урок 10.3 "Инкапсуляция", шаг 2

Создайте класс `Secret` с приватным атрибутом `__key`.

После создания объекта попробуйте обратиться к этому атрибуту напрямую.

Обработайте возникшее исключение и выведите сообщение:

    Ошибка: 'Secret' object has no attribute '__key'
"""

class Secret:
    def __init__(self):
        self.__key = 42


s = Secret()
try:
    print(s.__key)
except AttributeError as e:
    print(f"Ошибка: {e}")
