n, m = map(int, input().split())
l = []
max_item = 0
line = 0
column = 0
for i in range(n):
    c = list(map(int, input().split()))
    l.append(c)

for i in range(n):
    for j in range(m):
        if l[i][j] > max_item:
            max_item = l[i][j]
print(max_item)

for i in range(n):
    for j in range(m):
        if l[i][j] == max_item:
            line = i
            column = j
            break
            break
print(line, column)










# for i in range(n):
#     c = list(map(int, input().split()))
#     b.append(c)
# for i in range(n):
#     for j in range(n):
#         if b[i][j] == b[j][i]:
#             continue
#         else:
#             flag = False
# if flag:
#     print('YES')
# else:
#     print('NO')
#
#
#
