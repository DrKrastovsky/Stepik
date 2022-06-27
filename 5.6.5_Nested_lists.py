n, m = map(int, input().split())
b = []
for i in range(n-1):
    c = list(map(int, input().split()))
    b.append(c)
for i in range(n):
    for j in range(m):
        print(b[i][j])
# for i in range(n-1, -1, -1):
#     for j in range(m):
#         print(b[i][j], end=' ')
#     print()

