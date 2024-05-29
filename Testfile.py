from tkinter import * 
from tkinter.ttk import *
from tkinterweb import HtmlFrame




#Create an instance of tkinter frame
win = Tk()

win.title("NEw")


p1 = PhotoImage(file = 'Photos\pngtree-om-trishul-tattoo-logo-design-png-image_6452847.png')  

win.iconphoto(False, p1) 

b = Button(win, text = 'Press Me!') 
b.pack(side = TOP)
win.title('iconphoto() method')
#win.wm_attributes('-toolwindow', 'True')
win.mainloop()

