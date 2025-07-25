import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
        return hashlib.sha256(content).hexdigest()

file_path = input("Enter file path to check hash: ")

current_hash = calculate_hash(file_path)

with open("stored_hash.txt", "r") as hash_file:
    saved_hash = hash_file.read()

if current_hash == saved_hash:
    print("✅ File is unchanged.")
else:
    print("⚠️ WARNING: File has been modified!")
