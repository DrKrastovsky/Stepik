"""Напишите программу для построения горизонтальных столбчатых диаграмм с помощью символа звёздочки.
Ввод:
Несколько натуральных чисел на одной строке.
Вывод:
Несколько чисел на одной строке."""

a = map(int, input().split())
for i in a:
    print('*' * i)
