alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = "QWERTYUIOPASDFGHJKLZXCVBNM"

def encrypt(text):
    res = ""

    for char in text:
        if char.isupper():
            index = alphabet.index(char)
            res += key[index]

        elif char.islower():
            index = alphabet.index(char.upper())
            res += key[index].lower()

        else:
            res += char

    return res

def decrypt(text):
    res = ""
    for ch in text:
        if ch.isupper():
            index = key.index(ch)
            res += alphabet[index]
        elif ch.islower():
            index = key.index(ch.upper())
            res += alphabet[index].lower()
        else:
            res += ch
    return res

text = input("Enter text: ")
cipher_text = encrypt(text)
print("Cipher text: ", cipher_text)
plain_text = decrypt(cipher_text)
print("Plain text: ", plain_text)