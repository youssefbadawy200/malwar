import os as O
import base64 as B

def X(p):
    a = []
    l = B.b64decode(b'ZmlsZXMubG9n').decode()
    with open(l, "w") as f:
        for r, d, F in O.walk(p):
            for n in F:
                if n.endswith((".txt", ".jpg", ".docx")):
                    fp = O.path.join(r, n)
                    a.append(fp)
                    f.write(fp + "\n")
    print(f"{B.b64decode(b'W1wrXSBGaWxlIGxpc3Qgc2F2ZWQgdG8g').decode()}{l}")
    return a

if __name__ == "__main__":
    P = input(B.b64decode(b'U3BlY2lmeSB0aGUgcGF0aCB0byB1c2U6IA==').decode()).strip()
    if O.path.isdir(P):
        X(P)
    else:
        print(B.b64decode(b'W1tdIEludmFsaWQgcGF0aC4gUGxlYXNlIGNoZWNrIGFuZCB0cnkgYWdhaW4u').decode())
