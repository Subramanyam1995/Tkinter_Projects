from tkinter import *
from tkinter.ttk import *
from PIL import Image,ImageTk

win = Tk()

def Demo():
        fonts = ['Times', 'Courier', 'Helvetica', 'Didot']
        for x in fonts:
            Label(win,text=x, font=x+' 36').pack()

Button(win,text="Hello",command=Demo).pack()
win.mainloop()