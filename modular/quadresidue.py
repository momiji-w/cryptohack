p = 29
items = (14, 6, 11)
for i in range(1, p):
    a2 = (i ** 2) % p
    if a2 in items:
        print(i, a2)
