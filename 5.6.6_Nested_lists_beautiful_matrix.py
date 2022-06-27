a = []
for i in range(5):
    c = list(map(int, input().split()))
    a.append(c)
count = 0
for i in range(5):
    for j in range(5):
        if a[i][j] == 1:
            column = j
            string = i

if string != 2 or column != 2:
    count = abs(string - 2) + abs(column - 2)
    print(count)
else:
    print(count)




