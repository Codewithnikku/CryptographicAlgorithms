import random
import string

def generate_homophonic_table(key):
    random.seed(key) 

    letters = list(string.ascii_uppercase)
    symbols = [f"{i:02}" for i in range(1, 79)]
    random.shuffle(symbols)

    table = {}
    reverse_table = {}
    index = 0

    for letter in letters:
        table[letter] = symbols[index:index + 3]
        for code in table[letter]:
            reverse_table[code] = letter
        index += 3

    return table, reverse_table


def encrypt(text, table):
    cipher = []

    for ch in text.upper():
        if ch.isalpha():
            cipher.append(random.choice(table[ch]))
        elif ch == ' ':
            cipher.append("00")

    return " ".join(cipher)


def decrypt(cipher, reverse_table):
    plain = []

    for code in cipher.split():
        if code == "00":
            plain.append(" ")
        else:
            plain.append(reverse_table.get(code, "?"))

    return "".join(plain)

key = input("Enter key: ")
table, reverse_table = generate_homophonic_table(key)

while True:
    print("\n1. Encrypt")
    print("2. Decrypt")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        plaintext = input("Enter plaintext: ")
        ciphertext = encrypt(plaintext, table)
        print("Ciphertext:", ciphertext)

    elif choice == "2":
        ciphertext = input("Enter ciphertext: ")
        plaintext = decrypt(ciphertext, reverse_table)
        print("Plaintext:", plaintext)

    elif choice == "3":
        break

    else:
        print("Invalid choice!")