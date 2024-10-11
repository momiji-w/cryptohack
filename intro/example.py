from pwn import * # pip install pwntools
from Crypto.Util.number import *
import base64
import codecs
import json

r = remote('socket.cryptohack.org', 13377)

def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)


def hack(t, e):
    decoded = ""
    if t == "base64":
        decoded = base64.b64decode(e).decode()
    elif t == "hex":
        decoded = long_to_bytes(int(e, 16)).decode()
    elif t == "rot13":
        decoded = codecs.decode(e, 'rot_13')
    elif t == "bigint":
        decoded = long_to_bytes(int(e[2:], 16)).decode()
    elif t == "utf-8":
        decoded = "".join(chr(b) for b in e)

    return decoded

i = 0
while i < 100:
    received = json_recv()

    print("Received type: ")
    print(received["type"])
    print("Received encoded value: ")
    print(received["encoded"])

    decoded = hack(received["type"], received["encoded"])
    to_send = {
        "decoded": decoded
    }

    json_send(to_send)

    i += 1

print(json_recv())
