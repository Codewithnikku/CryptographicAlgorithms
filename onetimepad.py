import random
import string

def one_time_pad_encrypt(plaintext, key):
    if len(plaintext) != len(key):
        raise ValueError("Plaintext and key must be of the same length")

    ciphertext_chars = []
    for i in range(len(plaintext)):
        p_val = ord(plaintext[i])
        k_val = ord(key[i])
        c_val = (p_val + k_val) % 256
        ciphertext_chars.append(chr(c_val))
    return ''.join(ciphertext_chars)

def one_time_pad_decrypt(ciphertext, key):
    if len(ciphertext) != len(key):
        raise ValueError("Ciphertext and key must be of the same length")

    decrypted_chars = []
    for i in range(len(ciphertext)):
        c_val = ord(ciphertext[i])
        k_val = ord(key[i])
        p_val = (c_val - k_val) % 256
        decrypted_chars.append(chr(p_val))
    return ''.join(decrypted_chars)

def generate_random_key(length):
    characters = string.printable
    return ''.join(random.choice(characters) for _ in range(length))

plain_text = input("Enter plain text: ")
encryption_key = generate_random_key(len(plain_text)) 
cipher_text = one_time_pad_encrypt(plain_text, encryption_key)
print(f"Cipher text: {cipher_text}")

decrypted_text = one_time_pad_decrypt(cipher_text, encryption_key)
print(f"Decrypted text: {decrypted_text}")