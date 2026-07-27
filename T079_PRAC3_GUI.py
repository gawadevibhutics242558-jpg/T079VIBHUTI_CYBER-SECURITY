import tkinter as tk
from tkinter import messagebox
import hmac
import hashlib

# Secret Key
SECRET_KEY = b"mysecretkey"

# Generate MAC
def generate_mac():
    message = message_entry.get()

    if message == "":
        messagebox.showerror("Error", "Please enter a message.")
        return

    mac = hmac.new(SECRET_KEY, message.encode(), hashlib.sha256).hexdigest()

    mac_entry.delete(0, tk.END)
    mac_entry.insert(0, mac)

# Verify MAC
def verify_mac():
    received_message = verify_message_entry.get()
    received_mac = verify_mac_entry.get()

    if received_message == "" or received_mac == "":
        messagebox.showerror("Error", "Please fill all verification fields.")
        return

    new_mac = hmac.new(
        SECRET_KEY,
        received_message.encode(),
        hashlib.sha256
    ).hexdigest()

    if hmac.compare_digest(received_mac, new_mac):
        messagebox.showinfo(
            "Verification",
            "Message Verified Successfully!\n\nIntegrity and Authenticity are Maintained."
        )
    else:
        messagebox.showerror(
            "Verification",
            "Verification Failed!\n\nMessage has been Modified or Incorrect MAC."
        )

# Main Window
root = tk.Tk()
root.title("Message Authentication Code (MAC)")
root.geometry("600x400")
root.resizable(False, False)

# Generate Section
tk.Label(root, text="Generate MAC", font=("Arial", 14, "bold")).pack(pady=10)

tk.Label(root, text="Enter Message").pack()

message_entry = tk.Entry(root, width=60)
message_entry.pack()

tk.Button(root, text="Generate MAC", command=generate_mac, bg="green", fg="white").pack(pady=10)

tk.Label(root, text="Generated MAC").pack()

mac_entry = tk.Entry(root, width=70)
mac_entry.pack()

# Separator
tk.Label(root, text="---------------------------------------------").pack(pady=10)

# Verification Section
tk.Label(root, text="Verify MAC", font=("Arial", 14, "bold")).pack()

tk.Label(root, text="Received Message").pack()

verify_message_entry = tk.Entry(root, width=60)
verify_message_entry.pack()

tk.Label(root, text="Received MAC").pack()

verify_mac_entry = tk.Entry(root, width=70)
verify_mac_entry.pack()

tk.Button(root, text="Verify", command=verify_mac, bg="blue", fg="white").pack(pady=15)

root.mainloop()