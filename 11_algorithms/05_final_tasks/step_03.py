"""
Урок 11.5 "Итоговые задачи", шаг 3

Считайте строку текста. Уберите из неё знаки препинания `.,!?;:`, переведите в нижний регистр и
выведите самое частое слово и сколько раз оно встретилось (через пробел). Если таких слов несколько,
выведите то, что встретилось раньше.
"""

text = input()
for ch in ".,!?;:":
    text = text.replace(ch, "")
words = text.lower().split()
best = words[0]
for w in words:
    if words.count(w) > words.count(best):
        best = w
print(best, words.count(best))
