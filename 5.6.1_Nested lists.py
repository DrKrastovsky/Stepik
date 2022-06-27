n = int(input())
my_sum = 0
b = []
for i in range(n):
    c = list(map(int, input().split()))
    b.append(c)
for i in range(n):
    for j in range(n):
        if i == j:
            my_sum += b[i][j]
print(my_sum)
