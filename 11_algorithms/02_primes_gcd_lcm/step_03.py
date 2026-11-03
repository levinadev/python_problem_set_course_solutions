"""
Урок 11.2 "Простые числа, НОД и НОК", шаг 3

Решето Эратосфена. Считайте натуральное число `n` (от 2 до 100 000) и выведите через пробел все
простые числа от 2 до `n`.
"""

n = int(input())
sieve = [True] * (n + 1)
primes = []
for i in range(2, n + 1):
    if sieve[i]:
        primes.append(i)
        for j in range(i * i, n + 1, i):
            sieve[j] = False
print(" ".join(map(str, primes)))
