import tkinter as tk
from tkinter import ttk
import time
window = tk.Tk()

window.geometry("300x200")

def start_timer():
    time.sleep(1)

timer_var = tk.StringVar(value="Press Start Button")

timer_label = ttk.Label(window, textvariable= timer_var)

timer_label.pack()

input_time_var = tk.StringVar()

input_time_in_second = ttk.Entry(window,textvariable=input_time_var)

input_time_in_second.pack()

input_time_Hour = tk.StringVar()

input_time_Min = tk.StringVar()

input_time_Sec = tk.StringVar()

frame = tk.Frame(window)

checkbox_Hours = ttk.Checkbutton(frame, text = "Hour", variable=input_time_Hour)

checkbox_Hours.pack(side="left")

checkbox_Min = ttk.Checkbutton(frame, text = "Min", variable=input_time_Min)

checkbox_Min.pack(side="left")

checkbox_Sec = ttk.Checkbutton(frame, text = "Sec", variable=input_time_Sec)

checkbox_Sec.pack(side="left")

frame.pack()

timer_button = ttk.Button(window, text="Press", command= start_timer)

timer_button.pack()

window.mainloop()