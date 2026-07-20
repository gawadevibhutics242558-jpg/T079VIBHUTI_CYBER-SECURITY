import math

# Function to find GCD
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Function to find Modular Inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# RSA Key Generation
def generate_keys():
    p = int(input("Enter prime number p: "))
    q = int(input("Enter prime number q: "))

    n = p * q
    phi = (p - 1) * (q - 1)

    e = 2
    while e < phi:
        if gcd(e, phi) == 1:
            break
        e += 1

    d = mod_inverse(e, phi)

    return ((e, n), (d, n))

# Encryption
def encrypt(public_key, plaintext):
    e, n = public_key
    cipher = [pow(ord(char), e, n) for char in plaintext]
    return cipher

# Decryption
def decrypt(private_key, ciphertext):
    d, n = private_key
    plain = ''.join([chr(pow(char, d, n)) for char in ciphertext])
    return plain

# Main Program
public_key, private_key = generate_keys()

print("\nPublic Key:", public_key)
print("Private Key:", private_key)

message = input("\nEnter Message: ")

cipher = encrypt(public_key, message)

print("\nEncrypted Message:")
print(cipher)

plain = decrypt(private_key, cipher)

print("\nDecrypted Message:")
print(plain)