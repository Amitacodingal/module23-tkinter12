import tkinter as tk

def submit_form():
    name = name_entry.get()
    street = street_entry.get()
    city = city_entry.get()
    state = state_entry.get()
    zip_code = zip_entry.get()
    
    output_label.config(
        text=f"Submitted:\n{name}\n{street}\n{city}, {state} {zip_code}"
    )

# Create main window
root = tk.Tk()
root.title("Address Entry Form")

# Labels and Entry Fields
tk.Label(root, text="Name").grid(row=0, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="Street").grid(row=1, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="City").grid(row=2, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="State").grid(row=3, column=0, padx=10, pady=5, sticky='e')
tk.Label(root, text="ZIP Code").grid(row=4, column=0, padx=10, pady=5, sticky='e')

name_entry = tk.Entry(root, width=30)
street_entry = tk.Entry(root, width=30)
city_entry = tk.Entry(root, width=30)
state_entry = tk.Entry(root, width=30)
zip_entry = tk.Entry(root, width=30)

name_entry.grid(row=0, column=1)
street_entry.grid(row=1, column=1)
city_entry.grid(row=2, column=1)
state_entry.grid(row=3, column=1)
zip_entry.grid(row=4, column=1)

# Submit Button
submit_btn = tk.Button(root, text="Submit", command=submit_form)
submit_btn.grid(row=5, column=1, pady=10)

# Output Label
output_label = tk.Label(root, text="", fg="green", justify='left')
output_label.grid(row=6, column=0, columnspan=2, pady=10)

# Run the GUI
root.mainloop()
