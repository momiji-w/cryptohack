p = 991
g = 209
d = pow(g, -1, p)

assert (g * d) % p == 1

print(f"d = {d}")
