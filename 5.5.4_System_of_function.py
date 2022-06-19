"""Дано m, n найти кол-во пар a, b которые удоволетворяют
системе a*a + b = n и a + b*b = m"""

n, m = map(int, input().split())
count = 0
for i in range(1001):
    for j in range(1000):
        if i*i + j == n and i + j*j == m:
            count += 1
print(count)


