n = int(input())
b = []
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)

for i in range(n-1, -1, -1):
    for j in range(n-1, -1, -1):
        print(b[j][i], end=' ')
    print()

