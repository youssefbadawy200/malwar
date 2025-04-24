# server.py (use this if you want to log POST uploads)
from http.server import BaseHTTPRequestHandler, HTTPServer

class SimpleHandler(BaseHTTPRequestHandler):
    def do_POST(self):
        length = int(self.headers['Content-Length'])
        content = self.rfile.read(length)

        with open("uploaded_file", "wb") as f:
            f.write(content)

        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"File received")

httpd = HTTPServer(('0.0.0.0', 8080), SimpleHandler)
print("Listening on port 8080...")
httpd.serve_forever()
