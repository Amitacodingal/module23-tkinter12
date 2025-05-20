import tkinter as tk

def convert_length():
    try:
        value = float(entry.get())
        if var.get() == "Inch to Cm":
            result = value * 2.54
            output_label.config(text=f"{value} inches = {result:.2f} cm")
        else:
            result = value / 2.54
            output_label.config(text=f"{value} cm = {result:.2f} inches")
    except ValueError:
        output_label.config(text="Please enter a valid number.")

# Create main window
root = tk.Tk()
root.title("Inch ↔ Cm Converter")

# Input label and entry
tk.Label(root, text="Enter value:").grid(row=0, column=0, padx=10, pady=10)
entry = tk.Entry(root, width=20)
entry.grid(row=0, column=1)

# Option menu for conversion type
var = tk.StringVar(value="Inch to Cm")
option_menu = tk.OptionMenu(root, var, "Inch to Cm", "Cm to Inch")
option_menu.grid(row=0, column=2, padx=10)

# Convert button
convert_btn = tk.Button(root, text="Convert", command=convert_length)
convert_btn.grid(row=1, column=1, pady=10)

# Output label
output_label = tk.Label(root, text="", fg="blue")
output_label.grid(row=2, column=0, columnspan=3)

# Run the GUI
root.mainloop()
