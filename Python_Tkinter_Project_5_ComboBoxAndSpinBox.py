import tkinter as tk
from tkinter import ttk
from datetime import datetime

"""
ComboBox -Bind event "<<ComboBoxSelected>>"

"""
window = tk.Tk()

window.geometry("400x300")

window.title("ComboBoxAndSpainBox")

combo_var = tk.StringVar(value="Selected_None")

ComboBoxs = ttk.Combobox(window, 
                         values=["Dileep","Sudeep","Subramanyam"],
                         textvariable=combo_var ,
                          state="Disable"
                        )

ComboBoxs.pack()

SpainBoxs_var = tk.StringVar(value="Selected_None")

SpainBoxs = ttk.Spinbox(window, 
                        values=["Dileep","Sudeep","Subramanyam"],
                        textvariable=SpainBoxs_var,
                        state="Disable"
                        )

SpainBoxs.pack()

window.mainloop()