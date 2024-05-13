import tkinter as tk
from tkinter import ttk
from Python_Tkinter_Project_1_MilesToKilometer_Class import *

window = tk.Tk()
window.geometry("350x150")
window.title("MileToKilometer")

MileToConverter_label = ttk.Label(window, text="Miles   To    Kilometer", font="bebas 15")
MileToConverter_label.pack()

Input_value = ttk.Entry(window)
Input_value.pack()

Convert_Botton = ttk.Button(window, text="Convert")
Convert_Botton.pack()

KiloMeter_Output = ttk.Label(window,text="output")



window.mainloop()