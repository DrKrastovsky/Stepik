n = int(input())
b = []
flag = True
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)
for i in range(n):
    for j in range(n):
        if b[i][j] == b[j][i]:
            continue
        else:
            flag = False
if flag:
    print('YES')
else:
    print('NO')



