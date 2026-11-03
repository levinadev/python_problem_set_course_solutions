"""
Урок 8.6 "Декораторы", шаг 7

Напишите декоратор `non_negative`: если хотя бы один аргумент функции отрицательный, обёртка выводит
`Ошибка: отрицательный аргумент` и возвращает `None`, иначе возвращает результат функции. Украсьте
им функцию `area(a, b)`, возвращающую `a * b`. Считайте два целых числа (каждое с новой строки).
Если результат не `None`, выведите его.
"""

def non_negative(func):
    def wrapper(*args):
        if any(x < 0 for x in args):
            print("Ошибка: отрицательный аргумент")
            return None
        return func(*args)
    return wrapper


@non_negative
def area(a, b):
    return a * b


result = area(int(input()), int(input()))
if result is not None:
    print(result)
