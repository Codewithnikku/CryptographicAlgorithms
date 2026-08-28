import hashlib

message = input("Enter message: ")
hash_value = hashlib.sha256(message.encode()).hexdigest()
print(f"Orignal Message: {message}")
print(f"Hash Value: {hash_value}\n")

rec_msg = message
rec_hash_value = hashlib.sha256(rec_msg.encode()).hexdigest()
print("Data Integrity verification: ")

if hash_value == rec_hash_value:
    print("Data intact.")
else:
    print("Data has been modified.")

modified_message = message
modified_hash_value = hashlib.sha256(modified_message.encode()).hexdigest()
print(f"Orignal Message: {modified_message}")
print(f"Hash Value: {modified_hash_value}")