import requests
import math
from pwn import xor

BASE_URL = "https://aes.cryptohack.org/symmetry/"


def encrypt_flag():
    url = BASE_URL + "encrypt_flag/"
    r = requests.get(url)

    return r.json()["ciphertext"]


def encrypt(plaintext, iv):
    url = BASE_URL + f"encrypt/{plaintext}/{iv}/"
    r = requests.get(url)

    return r.json()["ciphertext"]


def main():
    enc_flag = encrypt_flag()
    iv = enc_flag[:32]
    enc_flag = enc_flag[32:]

    block_count = math.ceil(len(enc_flag) / 32)
    payload = b"A" * (block_count * 16)

    enc_payload = encrypt(payload.hex(), iv)
    flag = b""
    for i in range(block_count):
        keyed_block = xor(b"A" * 16, bytes.fromhex(enc_payload[i * 32 : (i + 1) * 32])) 
        flag += xor(keyed_block, bytes.fromhex(enc_flag[i * 32 : (i + 1) * 32]))

    print(flag)


def easier():
    enc_flag = encrypt_flag()
    iv = enc_flag[:32]
    ciphertext = enc_flag[32:]

    # OFB perform symmetrical operation on both encryption and decryption
    # encryption: keyed_iv ^ plaintext
    # decryption: keyed_iv ^ ciphertext
    # we can abuse this by providing same iv as the one we got from encrypt_flag()
    # and the ciphertext so we performed decryption on encrypt operation
    flag = encrypt(ciphertext, iv)
    print(bytes.fromhex(flag))

if __name__ == "__main__":
    # main()
    easier()
