n = input()
a = {}
for i in n.lower():
    if i.isalpha():
        if i in a:
            a[i] += 1
        else:
            a[i] = 1
print(a)

