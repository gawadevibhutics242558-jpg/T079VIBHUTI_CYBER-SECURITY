import tkinter as tk
from tkinter import messagebox

def calculate_keys():
    try:
        p = int(p_entry.get())
        g = int(g_entry.get())
        a = int(vibhu_entry.get())
        b = int(unna_entry.get())

        A = pow(g, a, p)
        B = pow(g, b, p)

        key_Vibhu = pow(B, a, p)
        key_Unna = pow(A, b, p)

        vibhu_public_label.config(
            text="Vibhu's Public Key: " + str(A)
        )

        unna_public_label.config(
            text="Unna's Public Key: " + str(B)
        )

        vibhu_shared_label.config(
            text="Vibhu's Shared Secret Key: " + str(key_Vibhu)
        )

        unna_shared_label.config(
            text="Unna's Shared Secret Key: " + str(key_Unna)
        )

        if key_Vibhu == key_Unna:
            result_label.config(
                text="Key Exchange Successful!\n"
                     "Both Vibhu and Unna have the same secret key.",
                fg="green"
            )
        else:
            result_label.config(
                text="Key Exchange Failed!",
                fg="red"
            )

    except ValueError:
        messagebox.showerror(
            "Error",
            "Please enter valid numbers."
        )

def clear_all():
    p_entry.delete(0, tk.END)
    g_entry.delete(0, tk.END)
    vibhu_entry.delete(0, tk.END)
    unna_entry.delete(0, tk.END)

    vibhu_public_label.config(text="")
    unna_public_label.config(text="")
    vibhu_shared_label.config(text="")
    unna_shared_label.config(text="")
    result_label.config(text="")

root = tk.Tk()
root.title("Diffie-Hellman Key Exchange")
root.geometry("650x650")
root.resizable(False, False)

title = tk.Label(
    root,
    text="DIFFIE-HELLMAN KEY EXCHANGE",
    font=("Arial", 20, "bold")
)
title.pack(pady=20)

tk.Label(
    root,
    text="Enter Prime Number (p):",
    font=("Arial", 12, "bold")
).pack()

p_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
p_entry.pack(pady=5)

tk.Label(
    root,
    text="Enter Primitive Root (g):",
    font=("Arial", 12, "bold")
).pack()

g_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
g_entry.pack(pady=5)

tk.Label(
    root,
    text="Enter Vibhu's Private Key:",
    font=("Arial", 12, "bold")
).pack()

vibhu_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
vibhu_entry.pack(pady=5)

tk.Label(
    root,
    text="Enter Unna's Private Key:",
    font=("Arial", 12, "bold")
).pack()

unna_entry = tk.Entry(
    root,
    width=30,
    font=("Arial", 12)
)
unna_entry.pack(pady=5)

tk.Button(
    root,
    text="Generate Shared Key",
    command=calculate_keys,
    font=("Arial", 11, "bold"),
    padx=20,
    pady=7
).pack(pady=15)

vibhu_public_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
vibhu_public_label.pack(pady=5)

unna_public_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
unna_public_label.pack(pady=5)

vibhu_shared_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
vibhu_shared_label.pack(pady=5)

unna_shared_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold")
)
unna_shared_label.pack(pady=5)

result_label = tk.Label(
    root,
    text="",
    font=("Arial", 11, "bold"),
    justify="center"
)
result_label.pack(pady=20)

tk.Button(
    root,
    text="Clear",
    command=clear_all,
    font=("Arial", 10),
    padx=25
).pack()

root.mainloop()