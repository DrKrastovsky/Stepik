"""Найдите сумму всех четырехзначных чисел, сумма цифр каждого из которых равна 20"""

my_sum = 0
for i1 in range(1, 10):
    for i2 in range(10):
        for i3 in range(10):
            for i4 in range(10):
                if i1 + i2 + i3 + i4 == 20:
                    print(i1, i2, i3, i4)
                    my_sum += int(str(i1)+str(i2)+str(i3)+str(i4))
                    print(my_sum)
