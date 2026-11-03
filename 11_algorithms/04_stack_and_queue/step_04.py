"""
Урок 11.4 "Стек и очередь", шаг 4

Обратная польская запись: операция записывается после своих операндов, например `3 4 + 2 *` означает
`(3 + 4) * 2`. Считайте выражение (целые числа и операции `+`, `-`, `*` через пробел) и выведите его
значение. Вычисляйте с помощью стека.
"""

stack = []
for token in input().split():
    if token in "+-*":
        b = stack.pop()
        a = stack.pop()
        if token == "+":
            stack.append(a + b)
        elif token == "-":
            stack.append(a - b)
        else:
            stack.append(a * b)
    else:
        stack.append(int(token))
print(stack[0])
