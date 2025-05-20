# Import necessary libraries
# pip install tk 
from tkinter import *

# Create Window
window = Tk()

# Set the window Title and Geometry
window.title('Demo Window')
window.geometry('400x300')

# Create a label widget
label = Label(window, text="Hello, Tkinter!")
label.pack()

# Run the application
window.mainloop()


'''
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Tkinter Example")

# Create a label widget
label = tk.Label(root, text="Hello, Tkinter!")
label.pack()

# Run the application
root.mainloop()
'''