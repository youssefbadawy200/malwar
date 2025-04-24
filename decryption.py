from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
import os

def decrypt_files(file_paths, key):
    for file_path in file_paths:
        with open(file_path, 'rb') as f:
            data = f.read()

        # Extract the IV (first 16 bytes) and the ciphertext
        iv = data[:16]
        ciphertext = data[16:]

        # Decrypt the data
        cipher = AES.new(key, AES.MODE_CBC, iv)
        try:
            decrypted_data = unpad(cipher.decrypt(ciphertext), AES.block_size)
            with open(file_path, 'wb') as f:
                f.write(decrypted_data)
            print(f"[+] Successfully decrypted: {file_path}")
        except ValueError as e:
            print(f"[!] Failed to decrypt {file_path}: {e}")

def load_key(filename):
    with open(filename, 'rb') as f:
        return f.read()

if __name__ == "__main__":
    # Input directory containing encrypted files
    dir_path = input("📁 Enter the directory containing encrypted files: ").strip()

    # Load the decryption key
    key = load_key("key.bin")

    encrypted_files = [os.path.join(dir_path, file) for file in os.listdir(dir_path) if file.endswith(('.txt', '.docx', '.jpg'))]

    if not encrypted_files:
        print("[-] No encrypted files found.")
    else:
        print(f"[*] Decrypting {len(encrypted_files)} files...")
        decrypt_files(encrypted_files, key)
