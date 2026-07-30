def ceaser_cipher(text, shift, mode):
    result = ""
    
    if mode == "decrypt":
        shift = -shift
        
    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - ord('A') + shift) % 26 + ord('A'))
        elif ch.islower():
            result += chr((ord(ch) - ord('a') + shift) % 26 + ord('a'))
        else:
            result += ch
    return result

print("Select mode: \n1. Encryption\n2. Decryption")

choice = input("Enter mode type: ")
text = input("Enter text: ")
shift = int(input("Shift by: "))

if choice == '1':
    output = ceaser_cipher(text, shift, 'encrypt')
    print("Encrypted text: ", output)
elif choice == '2':
    output = ceaser_cipher(text, shift, 'decrypt')
    print("Decrypted text: ", output)
else:
    print("Invalid choice!")