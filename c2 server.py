from http.server import HTTPServer, BaseHTTPRequestHandler
import os

class SimpleC2Handler(BaseHTTPRequestHandler):
    def do_POST(self):
        filename = self.headers.get('Filename')
        if not filename:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b"No filename provided.")
            return

        content_length = int(self.headers['Content-Length'])
        file_data = self.rfile.read(content_length)

        # Save the file
        with open(filename, "wb") as f:
            f.write(file_data)

        print(f"[+] Received and saved: {filename}")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"File received successfully.")

if __name__ == "__main__":
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, SimpleC2Handler)
    print("[*] Server running on http://localhost:8080 ...")
    httpd.serve_forever()
