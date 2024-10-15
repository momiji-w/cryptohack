import requests
import json
from pwn import *

BASE_URL = "http://aes.cryptohack.org/ecbcbcwtf/"


def get_encrypted_flag():
    url = BASE_URL + "encrypt_flag/"
    r = requests.get(url)
    if r.status_code != 200:
        print("OH NYOO! REQUEST FOR", url, "FAILED, STATUS CODE", r.status_code)
        exit(1)
    
    content = r.json()
    return content["ciphertext"]


def decrypt(ciphertext):
    url = BASE_URL + f"decrypt/{ciphertext}/"
    r = requests.get(url)
    if r.status_code != 200:
        print("OH NYOO! REQUEST FOR", url, "FAILED, STATUS CODE", r.status_code)
        exit(1)

    content = r.json()
    return content["plaintext"]


def main():
    encrypted_flag = get_encrypted_flag()

    iv = encrypted_flag[:32]
    block1 = encrypted_flag[32:64]
    block2 = encrypted_flag[64:]

    log.info(f"IV = {iv}")
    log.info(f"FIRST BLOCK = {block1}")
    log.info(f"SECOND BLOCK = {block2}")

    # get blocks operated with ebc
    block1_dec = decrypt(block1)
    log.info(f"FIRST BLOCK DECRYPTED = {block1_dec}")

    block2_dec = decrypt(block2)
    log.info(f"SECOND BLOCK DECRYPTED = {block2_dec}")

    flag = b""

    flag += xor(bytes.fromhex(iv), bytes.fromhex(block1_dec))
    flag += xor(bytes.fromhex(block1), bytes.fromhex(block2_dec))

    log.info(f"FLAG = {flag}")


if __name__ == "__main__":
    main()

