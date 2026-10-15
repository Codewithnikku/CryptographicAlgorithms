from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad

plain_text = input("Enter plain text: ")

key_input = input("Enter DES key (8 chars): ")

if len(key_input) != 8:
    print("Error: DES key must be exactly 8 characters")
    exit()

key = key_input.encode()

PT_bytes = plain_text.encode()

cipher = DES.new(key, DES.MODE_ECB)

encrypted = cipher.encrypt(
    pad(PT_bytes, DES.block_size)
)

print("\n--- DES Encryption ---")
print("Plain Text :", plain_text)
print("Encrypted  :", encrypted.hex())

decipher = DES.new(key, DES.MODE_ECB)

decrypted = unpad(
    decipher.decrypt(encrypted),
    DES.block_size
)

print("\n--- DES Decryption ---")
print("Decrypted  :", decrypted.decode())