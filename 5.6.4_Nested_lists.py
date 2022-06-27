n, m = map(int, input().split())
b = []
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)

for i in range(n):
    for j in range(m-1, -1, -1):
        print(b[i][j], end=' ')
    print()

