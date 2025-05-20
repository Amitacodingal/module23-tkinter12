import tkinter as tk
import random
import string

def generate_password():
    length = int(length_entry.get())
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    result_entry.delete(0, tk.END)
    result_entry.insert(0, password)

# Create main window
root = tk.Tk()
root.title("Password Generator")

# Length input
tk.Label(root, text="Password Length:").grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.insert(0, "12")  # default length
length_entry.grid(row=0, column=1)

# Generate button
generate_btn = tk.Button(root, text="Generate", command=generate_password)
generate_btn.grid(row=1, column=0, columnspan=2, pady=10)

# Result field
tk.Label(root, text="Generated Password:").grid(row=2, column=0, padx=10, pady=5)
result_entry = tk.Entry(root, width=30)
result_entry.grid(row=2, column=1)

# Run the GUI
root.mainloop()
