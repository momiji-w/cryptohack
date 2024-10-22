p = 28151
n = p - 1
ecm = ECM()
f = ecm.factor(n)
f = set(f)

for i in range(1, n):
    primitive = True

    for j in f:
        g = pow(i, (p - 1) // j, p)
        if g == 1:
            primitive = False
            break
    
    if primitive:
        print(i)
        break
