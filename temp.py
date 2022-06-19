"""Bubble sort"""

n = int(input())
a = map(int, input().split())
a = list(a)
count = 0
for i in range(n-1):
    for j in range(n-1):
        if a[j] > a[j+1]:
            a[j], a[j+1] = a[j+1], a[j]
            count += 1
for i in a:
    print(i, end=' ')
print()
print(count)

