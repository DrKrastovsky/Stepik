#Программа получает на вход две строки S1 и S2.
# Если строка S1 является анаграммой строки S2 нужно вывести YES, в противном случае - NO
s1 = input()
s2 = input()
s1_dict = {}
s2_dict = {}
for i in s1:
    s1_dict[i] = s1_dict.get(i, 0) + 1
for j in s2:
    s2_dict[j] = s2_dict.get(j, 0) + 1
if s1_dict == s2_dict:
    print('YES')
else:
    print('NO')

