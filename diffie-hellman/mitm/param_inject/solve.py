from pwn import *
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
from Crypto.Util.number import isPrime
import hashlib
import json
import random


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


def genSecret(p):
    a = random.getrandbits(p.bit_length())
    while True:
        if a < p:
            break
        a = random.getrandbits(p.bit_length())

    return a


def main():
    # Idea:
    # create new B so when alice sends the flag
    # we can decrypt it because alice uses our public B
    # to create her shared secret

    io = remote("socket.cryptohack.org", 13371)
    alice = b"Alice: "
    bob = b"Bob: "
    g = 2

    io.recvuntil(alice)
    aliceInt1 = json.loads(io.recvuntil(b"}").decode())

    p, A = int(aliceInt1["p"][2:], 16), int(aliceInt1["A"][2:], 16)

    io.recvuntil(bob)
    io.sendline(json.dumps(aliceInt1).encode())

    io.recvuntil(bob)
    bobInt1 = json.loads(io.recvuntil(b"}").decode())
    b = genSecret(p)
    newB = pow(g, b, p)
    bobInt1["B"] = hex(newB)
    io.recvuntil(alice)
    io.sendline(json.dumps(bobInt1).encode())

    io.recvuntil(alice)
    aliceInt2 = json.loads(io.recvuntil(b"}").decode())
    iv, enc_flag = aliceInt2["iv"], aliceInt2["encrypted_flag"]
    flag = decrypt_flag(pow(A, b, p), iv, enc_flag)
    print(flag)


def something():
    p = 2410312426921032588552076022197566074856950548502459942654116941958108831682612228890093858261341614673227141477904012196503648957050582631942730706805009223062734745341073406696246014589361659774041027169249453200378729434170325843778659198143763193776859869524088940195577346119843545301547043747207749969763750084308926339295559968882457872412993810129130294592999947926365264059284647209730384947211681434464714438488520940127459844288859336526896320919633919
    a = genSecret(p)

if __name__ == "__main__":
    something()
    #main()
