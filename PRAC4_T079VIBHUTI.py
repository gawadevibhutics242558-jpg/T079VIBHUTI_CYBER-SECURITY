from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

message = input("Enter the message: ").encode()

signature = private_key.sign(
    message,
    padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    ),
    hashes.SHA256()
)

print("\nDigital Signature Generated Successfully!")

verify_message = input("\nEnter message to verify: ").encode()

try:
    public_key.verify(
        signature,
        verify_message,
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    print("\nSignature Verified Successfully!")
    print("Message Integrity: Maintained")
    print("Message Authenticity: Verified")

except Exception:
    print("\nSignature Verification Failed!")
    print("Message has been modified or signature is invalid.")