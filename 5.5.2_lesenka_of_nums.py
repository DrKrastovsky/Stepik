"""Лесенка из чисел.
Программа принимает на вход целое положительное число n (n<=15) -
количество уровней, ваша задача вывести n уровней,
в каждом из которых стоят числа от 1 до значения уровня."""

n = int(input())
for i in range(n+2):
    print()
    for j in range(1, i):
        print(j, end=' ')