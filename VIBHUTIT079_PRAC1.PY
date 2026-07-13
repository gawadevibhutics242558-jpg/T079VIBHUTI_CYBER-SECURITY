def encrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 + key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 + key) % 26 + 97)
        else:
            result += ch

    return result


def decrypt(text, key):
    result = ""

    for ch in text:
        if ch.isupper():
            result += chr((ord(ch) - 65 - key) % 26 + 65)
        elif ch.islower():
            result += chr((ord(ch) - 97 - key) % 26 + 97)
        else:
            result += ch

    return result


print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

text = input("Enter message: ")
key = int(input("Enter key: "))

if choice == '1':
    print("Encrypted:", encrypt(text, key))
elif choice == '2':
    print("Decrypted:", decrypt(text, key))
else:
    print("Invalid choice")