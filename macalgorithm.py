import hmac
import hashlib

secret_key = input("Enter the shared secret key: ").encode('utf-8')

original_message_str = input("Enter the original message: ")
original_message = original_message_str.encode('utf-8')

h = hmac.new(secret_key, original_message, hashlib.sha256)

sender_mac = h.hexdigest()

print("Sender's original message:", original_message.decode())
print("Sender's MAC:", sender_mac)

received_message_good = original_message
received_mac_good = sender_mac

h_receiver_good = hmac.new(secret_key, received_message_good, hashlib.sha256)
calculated_mac_good = h_receiver_good.hexdigest()

print("\nReceiver's received message (good):", received_message_good.decode())
print("Receiver's received MAC (good):", received_mac_good)
print("Receiver's calculated MAC (good):", calculated_mac_good)

if hmac.compare_digest(received_mac_good, calculated_mac_good):
    print("Message is authentic and untampered (good)!")
else:
    print("Message authentication failed (good)!")

tampered_message = b'Hello, this is a TAMPERED message.'
received_mac_bad = sender_mac

h_receiver_bad = hmac.new(secret_key, tampered_message, hashlib.sha256)
calculated_mac_bad = h_receiver_bad.hexdigest()

print("\nReceiver's received message (bad):", tampered_message.decode())
print("Receiver's received MAC (bad):", received_mac_bad)
print("Receiver's calculated MAC (bad):", calculated_mac_bad)

if hmac.compare_digest(received_mac_bad, calculated_mac_bad):
    print("Message is authentic and untampered (bad)!")
else:
    print("Message authentication failed (bad)! Message has been tampered with or is not authentic.")