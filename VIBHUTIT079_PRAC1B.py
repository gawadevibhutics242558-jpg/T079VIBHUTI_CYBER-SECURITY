def encrypt(text, key):
    rail = [['\n' for i in range(len(text))]
            for j in range(key)]

    row, direction = 0, False

    for i in range(len(text)):
        if row == 0 or row == key - 1:
            direction = not direction

        rail[row][i] = text[i]
        row += 1 if direction else -1

    result = ""

    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != '\n':
                result += rail[i][j]

    return result


def decrypt(cipher, key):
    rail = [['\n' for i in range(len(cipher))]
            for j in range(key)]

    row, direction = 0, None

    for i in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        rail[row][i] = '*'
        row += 1 if direction else -1

    index = 0

    for i in range(key):
        for j in range(len(cipher)):
            if rail[i][j] == '*' and index < len(cipher):
                rail[i][j] = cipher[index]
                index += 1

    result = ""
    row = 0

    for i in range(len(cipher)):
        if row == 0:
            direction = True
        if row == key - 1:
            direction = False

        result += rail[row][i]
        row += 1 if direction else -1

    return result


print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter choice: ")

text = input("Enter message: ")
key = int(input("Enter rails: "))

if choice == '1':
    print("Encrypted:", encrypt(text, key))
else:
    print("Decrypted:", decrypt(text, key))