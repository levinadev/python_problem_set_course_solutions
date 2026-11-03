"""
Урок 11.4 "Стек и очередь", шаг 3

Считайте строку из скобок трёх видов: `()`, `[]`, `{}`. Выведите `True`, если скобочная
последовательность правильная, иначе `False`. Например, `([]{})` правильная, а `([)]` нет.
"""

pairs = {")": "(", "]": "[", "}": "{"}
stack = []
ok = True
for ch in input():
    if ch in "([{":
        stack.append(ch)
    elif not stack or stack.pop() != pairs[ch]:
        ok = False
        break
print(ok and not stack)
