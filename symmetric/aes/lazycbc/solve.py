import requests
from pwn import xor

BASE_URL = "https://aes.cryptohack.org/lazy_cbc/"


def encrypt(plaintext):
    url = BASE_URL + f"encrypt/{plaintext}/"
    r = requests.get(url)

    if r.status_code != 200:
        print("GOD PLEASE HELP ME")
        exit(1)

    return r.json()["ciphertext"]


def receive(ciphertext):
    url = BASE_URL + f"receive/{ciphertext}/"
    r = requests.get(url)

    if r.status_code != 200:
        print("GOD PLEASE HELP ME 2")
        exit(1)

    content = r.json()
    if "error" in content:
        return content["error"][len("Invalid plaintext: "):]

    return content["success"]


def get_flag(key):
    url = BASE_URL + f"get_flag/{key}/"
    r = requests.get(url)

    if r.status_code != 200:
        print("GOD PLEASE HELP ME 3")
        exit(1)

    content = r.json()
    if "error" in content:
        print("NAH BRO WTF")
        exit(1)

    return content["plaintext"]


def main():
    first_block = b"A" * 16
    second_block = b"B" * 16
    payload = first_block + second_block

    ciphertext = encrypt(payload.hex())
    keyed_second_block = xor(bytes.fromhex(ciphertext[:32]), second_block)
    plaintext = receive(ciphertext[32:64])
    key = xor(keyed_second_block, bytes.fromhex(plaintext))
    flag = get_flag(key.hex())
    print(bytes.fromhex(flag))


def easier():
    payload = b"\x00" * 32
    plaintext = bytes.fromhex(receive(payload.hex()))
    key = xor(plaintext[:16], plaintext[16:32])
    flag = get_flag(key.hex())
    print(bytes.fromhex(flag))

if __name__ == "__main__":
    easier()
    #main()
