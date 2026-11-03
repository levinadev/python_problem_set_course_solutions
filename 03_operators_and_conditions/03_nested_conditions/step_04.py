"""
Урок 3.3 "Вложенные условия", шаг 4

Считайте балл (целое число от 0 до 100). Выведите:

- `Excellent`, если балл не меньше 90;
- `Good`, если балл не меньше 70, но меньше 90;
- `Pass`, если балл не меньше 50, но меньше 70;
- `Fail` во всех остальных случаях.
"""

score = int(input())
if score >= 90:
    print("Excellent")
elif score >= 70:
    print("Good")
elif score >= 50:
    print("Pass")
else:
    print("Fail")
