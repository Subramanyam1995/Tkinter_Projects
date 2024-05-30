# Import the required libraries
from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

# Create an instance of tkinter frame or window
win = Tk()

# Set the size of the window
win.geometry("700x350")

def on_click():
   Buttons.after(1000,Buttons.destroy())

# Create a Label widget
label = Label(win, text=" Deleting a Label in Python Tkinter", font=('Helvetica 15'))
label.pack(pady=20)

# Add a Button to Show/Hide Canvas Items
Buttons=ttk.Button(win, text="Delete", command=on_click)
Buttons.pack()

win.mainloop()