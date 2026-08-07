# Caesar Cipher

## Aim

Implement the Caesar Cipher to encrypt and decrypt text.

## Algorithm

### Encryption

1.  Read the plaintext and shift value.
2.  For each character:
    -   If it is an uppercase letter:
        -   Convert it to a value from 0--25 using
            `ord(char) - ord('A')`.
        -   Add the shift.
        -   Use `% 26` to wrap around the alphabet.
        -   Convert back to a letter using `chr(...)`.
    -   If it is a lowercase letter, perform the same steps using `'a'`.
    -   Otherwise, leave the character unchanged.
3.  Join the processed characters and display the encrypted text.

### Decryption

1.  Read the ciphertext and shift value.
2.  Reverse the shift by subtracting it (or using a negative shift).
3.  Process each character using the same logic as encryption.
4.  Display the decrypted text.

## Flow

``` text
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

## Time Complexity

-   **Time:** O(n), where n is the number of characters.
-   **Space:** O(n), for the output string.

## Example

-   Plaintext: `HELLO`
-   Shift: `3`
-   Encrypted: `KHOOR`
-   Decrypted: `HELLO`

# Homophonic Substitution Cipher

## Aim

Implement homophonic substitution encryption and decryption using a keyed table of symbol values.

## Algorithm

### Encryption

1.  Read the plaintext and key.
    -   This loads the user message and the key used to create the homophonic mapping table.
2.  Generate a homophonic table from the key using a seeded random shuffle.
    -   This produces a stable mapping of each letter to multiple symbol codes for the given key.
3.  For each character in the plaintext, convert letters to uppercase and replace them with a random code from the table.
    -   This creates ciphertext by substituting each alphabetic character with one of its homophones.
4.  Use `00` for spaces and join all codes with spaces.
    -   This preserves word boundaries while ensuring the ciphertext is a sequence of codes.

### Decryption

1.  Read the ciphertext and the reverse lookup table.
    -   This loads the encoded message and the table needed to map codes back to letters.
2.  Split the ciphertext into individual codes.
    -   This separates the encoded stream into discrete homophonic symbols.
3.  For each code, convert `00` back to a space or use the reverse table to recover the original letter.
    -   This rebuilds the plaintext by reversing the homophonic substitution.
4.  Join the recovered characters into the decrypted text.
    -   This returns the original message format with letters and spaces restored.

# Message Authentication Code (HMAC-SHA256)

## Aim

Generate and verify a message authentication code for message integrity and authenticity.

## Algorithm

1.  Read the shared secret key and the original message.
    -   This obtains the common secret and the message to protect using HMAC.
2.  Encode both the key and the message into bytes.
    -   This converts the inputs into the byte form required by the HMAC algorithm.
3.  Compute the HMAC-SHA256 digest over the message using the secret key.
    -   This produces a fixed-length authentication code that depends on both the message and the key.
4.  Compare the received MAC with a newly calculated MAC using a constant-time comparison.
    -   This checks whether the message is authentic and unchanged without leaking timing information.
5.  Report whether the message is authentic or tampered.
    -   This gives the user a clear verification result based on the MAC comparison.

# Monoalphabetic Substitution Cipher

## Aim

Encrypt and decrypt text using a fixed monoalphabetic substitution key.

## Algorithm

### Encryption

1.  Read the plaintext.
    -   This captures the input message that should be transformed using the substitution key.
2.  For each character, if it is uppercase, find its index in the standard alphabet and replace it from the substitution key.
    -   This maps each letter to its corresponding cipher letter using the fixed substitution alphabet.
3.  If the character is lowercase, perform the same mapping while preserving lowercase.
    -   This ensures the original case of letters is preserved in the ciphertext.
4.  Leave non-letter characters unchanged.
    -   This keeps digits, punctuation, and spaces intact.
5.  Join the substituted characters and output the cipher text.
    -   This produces the final encrypted string.

### Decryption

1.  Read the ciphertext.
    -   This loads the encrypted message to reverse the substitution.
2.  For each uppercase character, find its position in the substitution key and replace it from the standard alphabet.
    -   This recovers the original plaintext letter by reversing the fixed mapping.
3.  For lowercase characters, perform the same reverse mapping while preserving lowercase.
    -   This restores the original casing for decrypted letters.
4.  Keep non-letter characters unchanged.
    -   This preserves the ciphertext formatting outside letters.
5.  Join the recovered characters and output the plaintext.
    -   This produces the decrypted original message.

# One-Time Pad Cipher

## Aim

Encrypt and decrypt text using a randomly generated key that is as long as the message.

## Algorithm

### Encryption

1.  Read the plaintext and generate a random key of equal length.
    -   This creates a one-time pad with the same number of characters as the message.
2.  For each position, convert the plaintext and key characters to numeric values and add them modulo 256.
    -   This combines the plaintext and key into a ciphertext byte value using modular arithmetic.
3.  Convert the result back to characters and join them into the ciphertext.
    -   This produces the encrypted output string.

### Decryption

1.  Read the ciphertext and the same key used for encryption.
    -   This ensures the decryption uses the exact one-time pad that was used to encrypt.
2.  For each position, convert the ciphertext and key characters to numeric values and subtract the key value modulo 256.
    -   This reverses the encryption operation and recovers the original byte values.
3.  Convert the recovered values back to characters and join them into the plaintext.
    -   This restores the original message text from the ciphertext.
