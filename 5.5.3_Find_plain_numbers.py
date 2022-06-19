"""по числу n найти количество простых чисел p из интервала n < p < 2n.

исло называется простым, если оно делится только само на себя и на единицу."""

n = int(input())
count = 0
for i in range(n+1, 2*n):
    if i % 2 == 0 and i != 2 or i ==1:
        continue
    # находим делители
    d = 3
    is_plain = True
    while d * d <= i:
        if i % d == 0:
            is_plain = False
            break
        d += 2
    if is_plain:
        count += 1
print(count)
