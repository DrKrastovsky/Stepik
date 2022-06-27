n, m = map(int, input().split())
b = []
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)
for i in range(n):
    s_string = 0
    for j in range(m):
        s_string += b[i][j]
    print(s_string, end=' ')
print()
for j in range(m):
    s_column = 0
    for i in range(n):
        s_column += b[i][j]
    print(s_column, end=' ')


