import tkinter as tk
from tkinter import ttk
import datetime

window = tk.Tk()

window.geometry("300x400")
window.title("CheckBox And Radio Button Training")

CheckBox_Var = tk.StringVar()

CheckBox_1 = ttk.Checkbutton(window,
                             text= "CheckBox_1",
                             variable = CheckBox_Var,
                             onvalue = 0,
                             offvalue = 1,
                             command=lambda:print(CheckBox_Var.get(), datetime.datetime.now()),
                             )
CheckBox_1.pack()

CheckBox_2 = ttk.Checkbutton(window,
                             text= "CheckBox_2",
                             variable = CheckBox_Var,
                             onvalue = 1,
                             offvalue = 4,
                             command=lambda:print(CheckBox_Var.get(),datetime.datetime.now()),
                             )
CheckBox_2.pack()

Frame_1 = tk.Frame(window)

Radio_Button_1 = ttk.Radiobutton(Frame_1,
                               text = "Radio Button 1",
                               value = "Radio_Button_1",
                               )

Radio_Button_1.pack()

Radio_Button_2 = ttk.Radiobutton(Frame_1,
                               text= "Radio Button 2",
                               value = "Radio_Button_2",
                               )

Radio_Button_2.pack()

Frame_1.pack()

Frame_2 = tk.Frame(window)
Radio_Button_3 = ttk.Radiobutton(Frame_2,
                               text = "Radio Button 3",
                               value = "Radio_Button_3",
                               )

Radio_Button_3.pack(side="left")

Radio_Button_4 = ttk.Radiobutton(Frame_2,
                               text= "Radio Button 4",
                               value = "Radio_Button_4",
                               )

Radio_Button_4.pack(side="left")

Frame_2.pack()


window.mainloop()
