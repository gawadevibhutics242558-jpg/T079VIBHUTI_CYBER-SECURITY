import tkinter as tk
from tkinter import messagebox
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa, padding

private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=2048
)

public_key = private_key.public_key()

signature = None

def sign_message():
    global signature

    message = message_entry.get("1.0", tk.END).strip()

    if message == "":
        messagebox.showwarning("Warning", "Please enter a message.")
        return

    signature = private_key.sign(
        message.encode(),
        padding.PSS(
            mgf=padding.MGF1(hashes.SHA256()),
            salt_length=padding.PSS.MAX_LENGTH
        ),
        hashes.SHA256()
    )

    status_label.config(
        text="Digital Signature Generated Successfully!",
        fg="green"
    )

    signature_text.delete("1.0", tk.END)
    signature_text.insert(tk.END, signature.hex())

def verify_message():
    if signature is None:
        messagebox.showwarning(
            "Warning",
            "Please generate the digital signature first."
        )
        return

    message = verify_entry.get("1.0", tk.END).strip()

    if message == "":
        messagebox.showwarning(
            "Warning",
            "Please enter a message to verify."
        )
        return

    try:
        public_key.verify(
            signature,
            message.encode(),
            padding.PSS(
                mgf=padding.MGF1(hashes.SHA256()),
                salt_length=padding.PSS.MAX_LENGTH
            ),
            hashes.SHA256()
        )

        result_label.config(
            text="✓ Signature Verified Successfully!\n"
                 "✓ Message Integrity Maintained\n"
                 "✓ Message Authenticity Verified",
            fg="green"
        )

    except Exception:
        result_label.config(
            text="✗ Signature Verification Failed!\n"
                 "Message has been modified or signature is invalid.",
            fg="red"
        )

def clear_all():
    message_entry.delete("1.0", tk.END)
    verify_entry.delete("1.0", tk.END)
    signature_text.delete("1.0", tk.END)

    status_label.config(text="")
    result_label.config(text="")

root = tk.Tk()
root.title("RSA Digital Signature")
root.geometry("700x700")
root.resizable(False, False)

title = tk.Label(
    root,
    text="RSA DIGITAL SIGNATURE",
    font=("Arial", 20, "bold")
)
title.pack(pady=15)

tk.Label(
    root,
    text="Enter Message:",
    font=("Arial", 12, "bold")
).pack()

message_entry = tk.Text(
    root,
    height=4,
    width=70
)
message_entry.pack(pady=8)

tk.Button(
    root,
    text="Generate Digital Signature",
    command=sign_message,
    font=("Arial", 11, "bold"),
    padx=10,
    pady=5
).pack(pady=5)

status_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
status_label.pack(pady=5)

tk.Label(
    root,
    text="Digital Signature:",
    font=("Arial", 12, "bold")
).pack()

signature_text = tk.Text(
    root,
    height=5,
    width=70
)
signature_text.pack(pady=8)

tk.Label(
    root,
    text="Enter Message to Verify:",
    font=("Arial", 12, "bold")
).pack()

verify_entry = tk.Text(
    root,
    height=4,
    width=70
)
verify_entry.pack(pady=8)

tk.Button(
    root,
    text="Verify Signature",
    command=verify_message,
    font=("Arial", 11, "bold"),
    padx=20,
    pady=5
).pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold"),
    justify="center"
)
result_label.pack(pady=15)

tk.Button(
    root,
    text="Clear",
    command=clear_all,
    font=("Arial", 10),
    padx=20
).pack()

root.mainloop()