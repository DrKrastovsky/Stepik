from string import ascii_lowercase

alphabet = {}
count = 1
for i in ascii_lowercase:
    alphabet.setdefault(i, count)
    print(i, count)
    count += 1

