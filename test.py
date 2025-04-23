import os

def collect_files(directory):
    log_path = "files.log"
    with open(log_path, "w") as log_file:
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.endswith((".txt", ".jpg", ".docx")):
                    full_path = os.path.join(root, file)
                    log_file.write(full_path + "\n")
    print(f"[+] File list saved to {log_path}")

if __name__ == "__main__":
    path = input("Specify the path to use: ").strip()
    if os.path.isdir(path):
        collect_files(path)
    else:
        print("[-] Invalid path. Please check and try again.")
