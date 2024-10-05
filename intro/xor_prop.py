from Crypto.Util.number import *

KEY1 = 0xa6c8b6733c9b22de7bc0253266a3867df55acde8635e19c73313
KEY23 = 0xc1545756687e7573db23aa1c3452a098b71a7fbf0fddddde5fc1
FLAG = 0x04ee9855208a2cd59091d04767ae47963170d1660df7f56f5faf

print(bytes.fromhex(hex((KEY1 ^ KEY23) ^ FLAG)[2:]))
