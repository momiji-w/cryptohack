def find(a, p):
    x = 0
    while x < 935:
        correct = 0
        for i in range(len(a)):
            if x % p[i] != a[i]:
                continue

            correct += 1

        if correct == len(a):
            break

        x += 1

    return x
        

p = [5, 11, 17]
a = [2, 3, 5]

x = find(a, p)
print(x % (5 * 11 * 17))
