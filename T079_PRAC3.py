import hmac
import hashlib

# Secret key (shared between sender and receiver)
secret_key = b"mysecretkey"

# Input message
message = input("Enter the message: ").encode()

# Generate MAC
mac = hmac.new(secret_key, message, hashlib.sha256).hexdigest()

print("\nGenerated MAC (HMAC-SHA256):")
print(mac)

# ---------------- Verification ----------------

print("\n----- Verify Message -----")
received_message = input("Enter the received message: ").encode()
received_mac = input("Enter the received MAC: ")

# Generate MAC again for received message
new_mac = hmac.new(secret_key, received_message, hashlib.sha256).hexdigest()

# Compare MACs securely
if hmac.compare_digest(received_mac, new_mac):
    print("\nMessage Verified Successfully!")
    print("Integrity and Authenticity are Maintained.")
else:
    print("\nVerification Failed!")
    print("Message has been Modified or Incorrect MAC.")