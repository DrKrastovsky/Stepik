'''Insertion sort'''


n = int(input())
a = map(int, input().split())
a = list(a)

for i in range(1, n):
    for j in range(i, 0, -1):
        if a[j] < a[j-1]:
            a[j], a[j-1] = a[j-1], a[j]
        else:
            break
for i in a:
    print(i, end=' ')
