import tkinter as tk
from tkinter import messagebox


def encrypt():
    try:
        text = entry.get()
        key = int(key_entry.get())

        result = ""

        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) - 65 + key) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) - 97 + key) % 26 + 97)
            else:
                result += ch

        output.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric key")


def decrypt():
    try:
        text = entry.get()
        key = int(key_entry.get())

        result = ""

        for ch in text:
            if ch.isupper():
                result += chr((ord(ch) - 65 - key) % 26 + 65)
            elif ch.islower():
                result += chr((ord(ch) - 97 - key) % 26 + 97)
            else:
                result += ch

        output.config(text=result)

    except ValueError:
        messagebox.showerror("Error", "Please enter a valid numeric key")



root = tk.Tk()
root.title("Caesar Cipher")
root.geometry("500x400")
root.resizable(False, False)


root.configure(bg="#FFE4EC")


heading = tk.Label(
    root,
    text=" CAESAR CIPHER ",
    font=("Arial", 20, "bold"),
    bg="#FF69B4",
    fg="white",
    pady=10
)
heading.pack(fill="x")


frame = tk.Frame(root, bg="#FFE4EC")
frame.pack(pady=20)


tk.Label(
    frame,
    text="Enter Message",
    font=("Arial", 12, "bold"),
    bg="#FFE4EC",
    fg="#C71585"
).grid(row=0, column=0, padx=10, pady=10)

entry = tk.Entry(
    frame,
    width=30,
    font=("Arial", 12)
)
entry.grid(row=0, column=1)


tk.Label(
    frame,
    text="Enter Key",
    font=("Arial", 12, "bold"),
    bg="#FFE4EC",
    fg="#C71585"
).grid(row=1, column=0, padx=10, pady=10)

key_entry = tk.Entry(
    frame,
    width=10,
    font=("Arial", 12)
)
key_entry.grid(row=1, column=1, sticky="w")


button_frame = tk.Frame(root, bg="#FFE4EC")
button_frame.pack(pady=15)

encrypt_btn = tk.Button(
    button_frame,
    text="Encrypt",
    command=encrypt,
    bg="#FF1493",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised"
)
encrypt_btn.grid(row=0, column=0, padx=15)

decrypt_btn = tk.Button(
    button_frame,
    text="Decrypt",
    command=decrypt,
    bg="#DB7093",
    fg="white",
    font=("Arial", 12, "bold"),
    width=12,
    relief="raised"
)
decrypt_btn.grid(row=0, column=1, padx=15)

tk.Label(
    root,
    text="Result",
    font=("Arial", 13, "bold"),
    bg="#FFE4EC",
    fg="#C71585"
).pack()

output = tk.Label(
    root,
    text="",
    bg="white",
    fg="#C71585",
    font=("Arial", 13, "bold"),
    width=35,
    height=2,
    relief="solid",
    bd=2
)
output.pack(pady=10)


footer = tk.Label(
    root,
    text="Classical Substitution Technique (Caesar Cipher)",
    font=("Arial", 10, "italic"),
    bg="#FFE4EC",
    fg="#8B3A62"
)
footer.pack(side="bottom", pady=10)


root.mainloop()