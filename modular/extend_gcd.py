from Crypto.Util.number import *

def gcd(a, b):
    if b == 0:
        return a

    return gcd(b, a % b)

def ext_gcd(a, b):
    r = (a, b)
    s = (1, 0)
    t = (0, 1)

    while r[1] != 0:
        q = r[0] // r[1]

        r = (r[1], r[0] - q * r[1])
        s = (s[1], s[0] - q * s[1])
        t = (t[1], t[0] - q * t[1])

    fs = s[0]
    ft = 0

    if t[1] != 0:
        ft = (r[0] - s[0] * a) // b

    return r[0], fs, ft

print(ext_gcd(26513, 32321))
