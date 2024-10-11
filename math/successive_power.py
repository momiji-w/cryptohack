# https://math.stackexchange.com/questions/1952453/finding-an-integer-x-and-a-3-digit-prime-p-that-solves-the-problem
# since we know x^n = t_n and x^n+1 = t_n+1 so t_n-1 * x = t_n mod p
# x = t_n * inverse(t_n-1) mod p
# bruteforcing is kinda meh but not bad ig

from Crypto.Util.number import inverse

rem = [588,665,216,113,642,4,836,114,851,492,819,237]

def isprime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    
    return True

possible_p = [x for x in range(max(rem) + 1, 999) if isprime(x)]

for p in possible_p:
    x = [(rem[i] * inverse(rem[i-1], p)) % p for i in range(1, len(rem))]

    if len(set(x)) == 1:
        print(f"crypto{{{p},{x[0]}}}")
