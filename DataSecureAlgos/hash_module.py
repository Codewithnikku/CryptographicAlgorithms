import hashlib


def generate_hash(message):

    hash_object = hashlib.sha256()

    hash_object.update(message.encode())

    return hash_object.hexdigest()


def verify_hash(message, original_hash):

    new_hash = generate_hash(message)

    return new_hash == original_hash