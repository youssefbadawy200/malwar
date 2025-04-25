from http.server import HTTPServer as H, BaseHTTPRequestHandler as B
import os as O
import base64 as X

class Z(B):
    def do_POST(self):
        f = self.headers.get('Filename')
        if not f:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(X.b64decode(b'Tm8gZmlsZW5hbWUgcHJvdmlkZWQu'))
            return

        c = int(self.headers['Content-Length'])
        d = self.rfile.read(c)

        with open(f, "wb") as w:
            w.write(d)

        print(f"{X.b64decode(b'WytdIFJlY2VpdmVkIGFuZCBzYXZlZDog').decode()}{f}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(X.b64decode(b'RmlsZSByZWNlaXZlZCBzdWNjZXNzZnVsbHku'))

if __name__ == "__main__":
    s = ('', 8080)
    h = H(s, Z)
    print(X.b64decode(b'WypdIFNlcnZlciBydW5uaW5nIG9uIGh0dHA6Ly9sb2NhbGhvc3Q6ODA4MCAuLi4=').decode())
    h.serve_forever()
