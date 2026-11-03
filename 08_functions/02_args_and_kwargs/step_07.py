"""
Урок 8.2 "Аргументы по умолчанию, *args, **kwargs", шаг 7

Напишите функцию `make_tag(text, tag="p")`, которая возвращает строку `<tag>text</tag>`. Считайте
текст и название тега (каждое с новой строки). Выведите результат функции сначала без второго
аргумента, затем со считанным тегом.
"""

def make_tag(text, tag="p"):
    return f"<{tag}>{text}</{tag}>"


text = input()
tag = input()
print(make_tag(text))
print(make_tag(text, tag))
