n = int(input())
a = {}
for i in range(n+1):
    a.setdefault(i, i*i)
print(a)
