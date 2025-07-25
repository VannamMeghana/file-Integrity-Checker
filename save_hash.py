import hashlib

def calculate_hash(file_path):
    with open(file_path, "rb") as file:
        content = file.read()
        return hashlib.sha256(content).hexdigest()

file_path = input("Enter file path to save hash: ")

hash_value = calculate_hash(file_path)

with open("stored_hash.txt", "w") as hash_file:
    hash_file.write(hash_value)

print("✅ Hash saved successfully in 'stored_hash.txt'")
