"""
Урок 7.1 "Создание и доступ к словарям", шаг 2

Даны имя студента, его оценка и предмет, каждое с новой строки. Создайте словарь `student` с ключами
`"name"`, `"grade"` и `"subject"` и выведите значение ключа `"subject"`.
"""

student = {"name": input(), "grade": input(), "subject": input()}
print(student["subject"])
