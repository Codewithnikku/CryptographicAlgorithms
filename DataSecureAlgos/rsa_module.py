from cryptography.hazmat.primitives.asymmetric import rsa, padding
from cryptography.hazmat.primitives import hashes


def generate_rsa_keys():
    """
    Generate RSA private and public keys.
    """

    private_key = rsa.generate_private_key(
        public_exponent=65537,
        key_size=2048
    )

    public_key = private_key.public_key()

    return private_key, public_key


def encrypt_with_rsa(message, public_key):
    """
    Encrypt a message using RSA-OAEP.
    """

    # Convert string message into bytes
    message_bytes = message.encode("utf-8")

    encrypted_message = public_key.encrypt(
        message_bytes,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    return encrypted_message


def decrypt_with_rsa(encrypted_message, private_key):
    """
    Decrypt an RSA encrypted message.
    """

    decrypted_message = private_key.decrypt(
        encrypted_message,
        padding.OAEP(
            mgf=padding.MGF1(
                algorithm=hashes.SHA256()
            ),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    # Convert bytes back into string
    return decrypted_message.decode("utf-8")