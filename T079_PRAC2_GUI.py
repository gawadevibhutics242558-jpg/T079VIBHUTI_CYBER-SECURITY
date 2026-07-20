import tkinter as tk
from tkinter import messagebox

# GCD Function
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Modular Inverse
def mod_inverse(e, phi):
    for d in range(2, phi):
        if (d * e) % phi == 1:
            return d
    return None

# Generate Keys
def generate_keys():
    try:
        p = int(entry_p.get())
        q = int(entry_q.get())

        global public_key, private_key

        n = p * q
        phi = (p - 1) * (q - 1)

        e = 2
        while e < phi:
            if gcd(e, phi) == 1:
                break
            e += 1

        d = mod_inverse(e, phi)

        public_key = (e, n)
        private_key = (d, n)

        lbl_public.config(text="Public Key : " + str(public_key))
        lbl_private.config(text="Private Key : " + str(private_key))

    except:
        messagebox.showerror("Error", "Enter Valid Prime Numbers")

# Encrypt
def encrypt():
    message = entry_message.get()

    e, n = public_key

    cipher = [pow(ord(ch), e, n) for ch in message]

    entry_cipher.delete(0, tk.END)
    entry_cipher.insert(0, str(cipher))

# Decrypt
def decrypt():
    try:
        cipher = eval(entry_cipher.get())

        d, n = private_key

        plain = ''.join(chr(pow(ch, d, n)) for ch in cipher)

        entry_plain.delete(0, tk.END)
        entry_plain.insert(0, plain)

    except:
        messagebox.showerror("Error", "Invalid Cipher")

# GUI
root = tk.Tk()
root.title("RSA Encryption & Decryption")
root.geometry("550x450")

public_key = ()
private_key = ()

tk.Label(root, text="Prime Number p").pack()
entry_p = tk.Entry(root, width=30)
entry_p.pack()

tk.Label(root, text="Prime Number q").pack()
entry_q = tk.Entry(root, width=30)
entry_q.pack()

tk.Button(root, text="Generate Keys", command=generate_keys).pack(pady=10)

lbl_public = tk.Label(root, text="Public Key")
lbl_public.pack()

lbl_private = tk.Label(root, text="Private Key")
lbl_private.pack()

tk.Label(root, text="Enter Message").pack()
entry_message = tk.Entry(root, width=40)
entry_message.pack()

tk.Button(root, text="Encrypt", command=encrypt).pack(pady=5)

tk.Label(root, text="Cipher Text").pack()
entry_cipher = tk.Entry(root, width=50)
entry_cipher.pack()

tk.Button(root, text="Decrypt", command=decrypt).pack(pady=5)

tk.Label(root, text="Decrypted Message").pack()
entry_plain = tk.Entry(root, width=40)
entry_plain.pack()

root.mainloop()