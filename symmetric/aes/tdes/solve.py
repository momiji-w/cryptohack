import requests


BASE_URL = "https://aes.cryptohack.org/triple_des/"


def encrypt(key, plaintext):
    url = BASE_URL + f"encrypt/{key}/{plaintext}/"
    r = requests.get(url)

    content = r.json()
    if "error" in content:
        print(content["error"])
        exit(1)

    return content["ciphertext"]


def encrypt_flag(key):
    url = BASE_URL + f"encrypt_flag/{key}/"
    r = requests.get(url)

    content = r.json()
    if "error" in content:
        print(content["error"])
        exit(1)

    return content["ciphertext"]


def main():
    # TDES has a weakness against weak key
    # key can be construct to cause double encryption, ie encryption function
    # can be use as a decryption function
    # https://en.wikipedia.org/wiki/Weak_key#Weak_keys_in_DES

    key = b"\x01" * 8 + b"\xfe" * 8
    flag_cipher = encrypt_flag(key.hex())
    decrypt = encrypt(key.hex(), flag_cipher)

    print(bytes.fromhex(decrypt))


if __name__ == "__main__":
    main()
