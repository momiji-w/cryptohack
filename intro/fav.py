from Crypto.Util.number import *

secret = 0x73626960647f6b206821204f21254f7d694f7624662065622127234f726927756d

tries = 0
found = False
while tries < 0xff and found == False:
    secretByte = long_to_bytes(secret)
    if tries ^ secretByte[0] == ord("c"):
        found = True
        for i in secretByte:
            print(chr(tries ^ i), end="")

    tries += 1
