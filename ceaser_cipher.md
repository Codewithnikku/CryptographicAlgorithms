# Caesar Cipher

## Aim

Implement the Caesar Cipher to encrypt and decrypt text.

## Algorithm

### Encryption

1. Read the plaintext and shift value.
2. For each character:
   - If it is an uppercase letter:
     - Convert it to a value from 0--25 using
       `ord(char) - ord('A')`.
     - Add the shift.
     - Use `% 26` to wrap around the alphabet.
     - Convert back to a letter using `chr(...)`.
   - If it is a lowercase letter, perform the same steps using `'a'`.
   - Otherwise, leave the character unchanged.
3. Join the processed characters and display the encrypted text.

### Decryption

1. Read the ciphertext and shift value.
2. Reverse the shift by subtracting it (or using a negative shift).
3. Process each character using the same logic as encryption.
4. Display the decrypted text.

## Flow

```text
Start
  │
  ▼
Read message and shift
  │
  ▼
Choose Encrypt or Decrypt
  │
  ▼
Process each character
  │
  ├── Letter? ── Yes ─► Shift letter (wrap using % 26)
  │
  └── No ───────► Keep unchanged
  │
  ▼
Display result
  │
  ▼
End
```

## Example

- Plaintext: `HELLO`
- Shift: `3`
- Encrypted: `KHOOR`
- Decrypted: `HELLO`
