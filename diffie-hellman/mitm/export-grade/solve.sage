from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import isPrime
import hashlib
import json


def is_pkcs7_padded(message):
    padding = message[-message[-1]:]
    return all(padding[i] == len(padding) for i in range(0, len(padding)))


def decrypt_flag(shared_secret: int, iv: str, ciphertext: str):
    # Derive AES key from shared secret
    sha1 = hashlib.sha1()
    sha1.update(str(shared_secret).encode('ascii'))
    key = sha1.digest()[:16]
    # Decrypt flag
    ciphertext = bytes.fromhex(ciphertext)
    iv = bytes.fromhex(iv)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    plaintext = cipher.decrypt(ciphertext)

    if is_pkcs7_padded(plaintext):
        return unpad(plaintext, 16).decode('ascii')
    else:
        return plaintext.decode('ascii')


alice = {"p": "0xde26ab651b92a129", "g": "0x2", "A": "0xa9c46df8a21ea9f8"}
bob = {"B": "0x51f919656f8f0469"}
enc_flag = {"iv": "0107cba784f2fe4b6efc1d061ffadab1", "encrypted_flag": "fd9e0f30e777309cb7f2acd49da1788158e699bbef0cbc8c54717b5b2bb08de4"}

p, R = int(alice["p"][2:], 16), GF(alice["p"])
g = R(alice["g"])
B = R(bob["B"])
A = int(alice["A"][2:], 16)
b = discrete_log(B, g)

iv, ct = enc_flag["iv"], enc_flag["encrypted_flag"]

flag = decrypt_flag(pow(A, b, p), iv, ct)
print(flag)
