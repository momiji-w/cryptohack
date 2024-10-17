import requests
from pwn import xor

BASE_URL = "https://aes.cryptohack.org/flipping_cookie/"


def get_cookie():
    url = BASE_URL + "get_cookie/"
    r = requests.get(url)

    content = r.json()["cookie"]
    return bytes.fromhex(content[:32]), bytes.fromhex(content[32:])


def check_admin(cookie, iv):
    url = BASE_URL + f"check_admin/{cookie}/{iv}/"
    r = requests.get(url)

    if "flag" not in r.json():
        print(r.json())
        print("Wow, You fucked it up a little bit I think.")
        exit(1)

    return r.json()["flag"]


if __name__ == "__main__":
    iv, cookie = get_cookie()
    known_text = b"admin=False;expiry="
    edit = b"admin=True;expiry="

    keyed_cipher = xor(known_text[:16], iv)
    forged_iv = xor(keyed_cipher, edit[:16])

    flag = check_admin(cookie.hex(), forged_iv.hex())
    print(flag)
