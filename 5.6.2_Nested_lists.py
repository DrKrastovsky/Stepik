n = int(input())
b = []
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)

for i in range(n):
    for j in range(n):
        print(b[j][i], end=' ')
    print()

