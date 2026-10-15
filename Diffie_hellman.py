print("----- Diffie-Hellman Key Exchange -----")

p = 29
g = 2

print("\nPublic Parameters:")
print("Prime (p):", p)
print("Generator (g):", g)

alice_private = 9
bob_private = 14

print("\nPrivate Keys:")
print("Alice:", alice_private)
print("Bob:", bob_private)

alice_public = pow(g, alice_private, p)
bob_public = pow(g, bob_private, p)

print("\nPublic Keys:")
print("Alice:", alice_public)
print("Bob:", bob_public)

alice_shared = pow(bob_public, alice_private, p)
bob_shared = pow(alice_public, bob_private, p)

print("\nShared Secret:")
print("Alice:", alice_shared)
print("Bob:", bob_shared)

print("\nResult:")

if alice_shared == bob_shared:
    print("Key exchange successful!")
    print("Both users have the same secret key.")
else:
    print("Key exchange failed!")