n = int(input())
data_base = {}
for i in range(n):
    login = input()
    if login in data_base:
        print(login + str(data_base[login]))
        data_base[login] += 1
    else:
        data_base[login] = 1
        print('OK')

