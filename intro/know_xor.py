from Crypto.Util.number import *
from pwn import *

secret = 0x0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104
print(xor(long_to_bytes(secret), b"myXORkey"))
