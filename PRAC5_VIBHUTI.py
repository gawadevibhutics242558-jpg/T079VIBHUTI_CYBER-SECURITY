print("DIFFIE-HELLMAN KEY EXCHANGE")
print("----------------------------")

p = int(input("Enter prime number (p): "))
g = int(input("Enter primitive root (g): "))

a = int(input("Enter Vibhu's private key: "))
b = int(input("Enter Unna's private key: "))

A = pow(g, a, p)

B = pow(g, b, p)

key_Vibhu = pow(B, a, p)
key_Unna = pow(A, b, p)


print("\n--- RESULTS ---")

print("Vibhu's Public Key:", A)
print("Unna's Public Key:", B)

print("Vibhu's Shared Secret Key:", key_Vibhu)
print("Unna's Shared Secret Key:", key_Unna)


if key_Vibhu == key_Unna:
    print("\nKey Exchange Successful!")
    print("Both Vibhu and Unna have the same secret key.")
else:
    print("\nKey Exchange Failed!")