import tkinter as tk
from tkinter import ttk
import time



def start_timer():

    print(f'"timer_var" : {timer_var.get()}')
    print(f'"input_time_var" : {input_time_var.get()}')
    print(f'"input_time_Hour" : {input_time_Hour.get()}')
    print(f'"input_time_Min" : {input_time_Min.get()}')
    print(f'"input_time_Sec" : {input_time_Sec.get()}')
    timer_var.set( value = input_time_var.get() )


window = tk.Tk()

window.geometry("300x200")


timer_var = tk.StringVar(value="Press Start Button")

timer_label = ttk.Label(window, textvariable= timer_var)

timer_label.pack()

input_time_var = tk.StringVar()

input_time_in_second = ttk.Entry(window,textvariable=input_time_var)

input_time_in_second.pack()


frame = tk.Frame(window)


input_time_Hour = tk.StringVar(value=0)

input_time_Min = tk.StringVar(value=0)

input_time_Sec = tk.StringVar(value=0)

checkbox_Hours = ttk.Checkbutton(frame, text = "Hour", variable=input_time_Hour, onvalue=1, offvalue=0)

checkbox_Hours.pack(side="left")

checkbox_Min = ttk.Checkbutton(frame, text = "Min", variable=input_time_Min, onvalue=1, offvalue=0)

checkbox_Min.pack(side="left")

checkbox_Sec = ttk.Checkbutton(frame, text = "Sec", variable=input_time_Sec, onvalue=1, offvalue=0)

checkbox_Sec.pack(side="left")

frame.pack()



timer_button = ttk.Button(window, text="Press", command= start_timer)

timer_button.pack()



window.mainloop()