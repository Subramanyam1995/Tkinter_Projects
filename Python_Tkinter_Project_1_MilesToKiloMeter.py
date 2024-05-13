import tkinter as tk
from tkinter import ttk
from Python_Tkinter_Project_1_MilesToKilometer_Class import *


def converter():
    mile_value = input_value.get()
    if mile_value.isnumeric():
        ConvertToKm=int(mile_value)*1.61
        output_string.set(ConvertToKm)
    else:
        output_string.set("Invaild input")
        input_value.set("")

window = tk.Tk()
window.geometry("350x150")
window.title("MileToKilometer")

MileToConverter_label = ttk.Label(window, text="Miles   To    Kilometer", font="bebas 15")
MileToConverter_label.pack()

Frames = tk.Frame(window)

input_value = tk.StringVar()

Input_value = ttk.Entry(Frames, textvariable=input_value)
Input_value.pack(side ="left",)

Convert_Botton = ttk.Button(Frames, text="Convert", command=converter)
Convert_Botton.pack(side ="left")

Frames.pack()

output_string = tk.StringVar(value="Output11")

KiloMeter_Output = ttk.Label(window,text="output", textvariable=output_string)
KiloMeter_Output.pack()


window.mainloop()