import os
from cryptography.hazmat.primitives.ciphers.aead import AESGCM


def generate_aes_key():
    return AESGCM.generate_key(bit_length=256)


def encrypt_message(message, key):
    aes = AESGCM(key)

    nonce = os.urandom(12)

    ciphertext = aes.encrypt(
        nonce,
        message.encode(),
        None
    )

    return nonce, ciphertext


def decrypt_message(nonce, ciphertext, key):
    aes = AESGCM(key)

    plaintext = aes.decrypt(
        nonce,
        ciphertext,
        None
    )

    return plaintext.decode()