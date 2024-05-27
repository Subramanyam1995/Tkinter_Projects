import tkinter as tk
from tkinter import ttk
from tkinter import messagebox 

window = tk.Tk()

window.geometry("600x400")

canvass = tk.Canvas(window, bg="white")

canvass.pack()

canvass.create_rectangle((50,20,100,200), fill="red")

button_1 = ttk.Button(window, text= "Just Click Me")

button_1.pack()

button_1 = ttk.Button(window, text= "Just Click Me")

button_1.pack()

button_1 = ttk.Button(window, text= "Just Click Me")

button_1.pack()




ww = tk.Message(window)

ww.pack()

window.mainloop()