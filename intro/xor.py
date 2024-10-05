from Crypto.Util.number import *

label = b"label"

print("crypto{", end="")
for i in label:
    print(chr(i ^ 13), end="")
print("}")
