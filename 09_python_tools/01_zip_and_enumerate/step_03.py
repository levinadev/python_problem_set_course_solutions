"""
Урок 9.1 "zip() и enumerate()", шаг 3

В первой строке буквы через пробел, во второй числа через пробел (их может быть другое количество).
Используя `zip`, выведите пары в формате `{letter}: {number}`, пока не закончится более короткий
список.
"""

letters = input().split()
numbers = input().split()
for letter, number in zip(letters, numbers):
    print(f"{letter}: {number}")
