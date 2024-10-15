from Crypto.Cipher import AES
import hashlib

# /usr/share/dict/words from
# https://gist.githubusercontent.com/wchargin/8927565/raw/d9783627c731268fb2935a731a618aa8e95cf465/words
with open("./words") as f:
    words = [w.strip() for w in f.readlines()]

ciphertext = bytes.fromhex("c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66")

for password in words:
    key = hashlib.md5(password.encode()).digest()

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        continue

    if b"crypto{" in decrypted:
        print(password)
        print(decrypted)
        exit()
