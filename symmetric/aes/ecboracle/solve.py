import requests

printable = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_-~!?#%&@{}"


def encrypt(plaintext):
    url = f"https://aes.cryptohack.org/ecb_oracle/encrypt/{plaintext}/"
    r = requests.get(url)
    if r.status_code != 200:
        print("Man, What the fuck")

    content = r.json()

    return content["ciphertext"]


def main():
    flag = b"crypto{"
    print(f"CURRENT FLAG = {flag}")

    while flag[-1] != "}":
        for i in printable:
            i = i.encode()

            payload = b"A" * (32 - len(flag) - 1) + flag + i + b"A" * (32 - len(flag) - 1)
            cipher = encrypt(payload.hex())

            if cipher[32:64] == cipher[96:128]:
                flag += i
                print(f"CURRENT FLAG = {flag}")
                break

    print(f"FINAL FLAG = {flag}")

if __name__ == "__main__":
    main()
