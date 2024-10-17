import requests


def xor(a, b):
    return bytes([x ^ y for x, y in zip(a, b)])


r = requests.get("https://aes.cryptohack.org/bean_counter/encrypt/")
data = r.json()["encrypted"]

byteitems = [bytes.fromhex(data[i * 32 : (i + 1) * 32]) for i in range(len(data) // 32 + 1)]

png_ihdr_header = b"\x89\x50\x4e\x47\x0d\x0a\x1a\x0a\x00\x00\x00\x0d\x49\x48\x44\x52" 

keystream = xor(png_ihdr_header, byteitems[0])

img = b""
for i in byteitems:
    img += xor(keystream, i)

save = open("flag.png", "wb")
save.write(img)
save.close()
