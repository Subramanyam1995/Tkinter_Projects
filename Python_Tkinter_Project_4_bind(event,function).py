import tkinter as tk
from tkinter import ttk
from datetime import datetime

# 
# 

# 
# 

#

"""
T.t.R
Bind
Widget.bind(event,funcation)
Format : Modifier - Type - Detail
Ex: Alt-Keypress-a
Must Add Event Varible to Lambda key_value : function to value_value
<Motion>
<Keypress>
<FocusOut>
<MouseWheel>
https://www.pythontutorial.net/tkinter/tkinter-event-binding/

"""

windows = tk.Tk()

windows.geometry("700x600")

windows.title("EventBinding")


def get_postion_1(event):
    data_var_1.set(f"Text location = x:{event.x}, y:{event.y}")
    #print(f"x:{event.x}, y:{event.y}")

def get_postion_2(event):
    data_var_2.set(f"Entry location = x:{event.x}, y:{event.y}")
    #print(f"x:{event.x}, y:{event.y}")

def get_postion_3(event):
    data_var_3.set(f"Button location = x:{event.x}, y:{event.y}")
    #print(f"x:{event.x}, y:{event.y}")

data_var_1=tk.StringVar(value="God Text")
data_var_2=tk.StringVar(value="God Entry")
data_var_3=tk.StringVar(value="God Button")

frame_1= tk.Frame(windows)

label_1 = ttk.Label(frame_1,text="a",textvariable=data_var_1)
label_2 = ttk.Label(frame_1,text="a",textvariable=data_var_2)
label_3 = ttk.Label(frame_1,text="a",textvariable=data_var_3)

label_1.pack()
label_2.pack()
label_3.pack()
frame_1.pack()
text = tk.Text(windows)

text.pack()

entry = ttk.Entry(windows)

entry.pack()

button = ttk.Button(
                    windows,
                    text="Button",
                )

button.pack()

# Dumpyard_1

# Bind : <Modifier - Type - Detail>
button.bind("<Alt-KeyPress-a>" ,lambda event: print(f"{event} {datetime.now()}"))

# Motion
text.bind("<Motion>", lambda event:get_postion_1(event))
entry.bind("<Motion>", lambda event:get_postion_2(event))
button.bind("<Motion>", lambda event:get_postion_3(event))

entry.bind("<FocusIn>",lambda event: print("entry field was selected"))
entry.bind("<FocusOut>",lambda event: print("entry field was unselected"))
windows.bind('<A>', lambda event: print('Press A'))
windows.bind('<B>', lambda event: print('Press B'))
windows.bind('<C>', lambda event: print('Press C'))
windows.bind('<D>', lambda event: print('Press D'))
windows.bind('<E>', lambda event: print('Press E'))
windows.bind('<F>', lambda event: print('Press F'))
windows.bind('<G>', lambda event: print('Press G'))
windows.bind('<H>', lambda event: print('Press H'))
windows.bind('<I>', lambda event: print('Press I'))
windows.bind('<J>', lambda event: print('Press J'))
windows.bind('<K>', lambda event: print('Press K'))
windows.bind('<L>', lambda event: print('Press L'))
windows.bind('<M>', lambda event: print('Press M'))
windows.bind('<N>', lambda event: print('Press N'))
windows.bind('<O>', lambda event: print('Press O'))
windows.bind('<P>', lambda event: print('Press P'))
windows.bind('<Q>', lambda event: print('Press Q'))
windows.bind('<R>', lambda event: print('Press R'))
windows.bind('<S>', lambda event: print('Press S'))
windows.bind('<T>', lambda event: print('Press T'))
windows.bind('<U>', lambda event: print('Press U'))
windows.bind('<V>', lambda event: print('Press V'))
windows.bind('<W>', lambda event: print('Press W'))
windows.bind('<X>', lambda event: print('Press X'))
windows.bind('<Y>', lambda event: print('Press Y'))
windows.bind('<Z>', lambda event: print('Press Z'))
windows.bind('<a>', lambda event: print('Press a'))
windows.bind('<b>', lambda event: print('Press b'))
windows.bind('<c>', lambda event: print('Press c'))
windows.bind('<d>', lambda event: print('Press d'))
windows.bind('<e>', lambda event: print('Press e'))
windows.bind('<f>', lambda event: print('Press f'))
windows.bind('<g>', lambda event: print('Press g'))
windows.bind('<h>', lambda event: print('Press h'))
windows.bind('<i>', lambda event: print('Press i'))
windows.bind('<j>', lambda event: print('Press j'))
windows.bind('<k>', lambda event: print('Press k'))
windows.bind('<l>', lambda event: print('Press l'))
windows.bind('<m>', lambda event: print('Press m'))
windows.bind('<n>', lambda event: print('Press n'))
windows.bind('<o>', lambda event: print('Press o'))
windows.bind('<p>', lambda event: print('Press p'))
windows.bind('<q>', lambda event: print('Press q'))
windows.bind('<r>', lambda event: print('Press r'))
windows.bind('<s>', lambda event: print('Press s'))
windows.mainloop()


"""Dumpyard_1
windows.bind('<A>', lambda event: print('Press A'))
windows.bind('<B>', lambda event: print('Press B'))
windows.bind('<C>', lambda event: print('Press C'))
windows.bind('<D>', lambda event: print('Press D'))
windows.bind('<E>', lambda event: print('Press E'))
windows.bind('<F>', lambda event: print('Press F'))
windows.bind('<G>', lambda event: print('Press G'))
windows.bind('<H>', lambda event: print('Press H'))
windows.bind('<I>', lambda event: print('Press I'))
windows.bind('<J>', lambda event: print('Press J'))
windows.bind('<K>', lambda event: print('Press K'))
windows.bind('<L>', lambda event: print('Press L'))
windows.bind('<M>', lambda event: print('Press M'))
windows.bind('<N>', lambda event: print('Press N'))
windows.bind('<O>', lambda event: print('Press O'))
windows.bind('<P>', lambda event: print('Press P'))
windows.bind('<Q>', lambda event: print('Press Q'))
windows.bind('<R>', lambda event: print('Press R'))
windows.bind('<S>', lambda event: print('Press S'))
windows.bind('<T>', lambda event: print('Press T'))
windows.bind('<U>', lambda event: print('Press U'))
windows.bind('<V>', lambda event: print('Press V'))
windows.bind('<W>', lambda event: print('Press W'))
windows.bind('<X>', lambda event: print('Press X'))
windows.bind('<Y>', lambda event: print('Press Y'))
windows.bind('<Z>', lambda event: print('Press Z'))
windows.bind('<a>', lambda event: print('Press a'))
windows.bind('<b>', lambda event: print('Press b'))
windows.bind('<c>', lambda event: print('Press c'))
windows.bind('<d>', lambda event: print('Press d'))
windows.bind('<e>', lambda event: print('Press e'))
windows.bind('<f>', lambda event: print('Press f'))
windows.bind('<g>', lambda event: print('Press g'))
windows.bind('<h>', lambda event: print('Press h'))
windows.bind('<i>', lambda event: print('Press i'))
windows.bind('<j>', lambda event: print('Press j'))
windows.bind('<k>', lambda event: print('Press k'))
windows.bind('<l>', lambda event: print('Press l'))
windows.bind('<m>', lambda event: print('Press m'))
windows.bind('<n>', lambda event: print('Press n'))
windows.bind('<o>', lambda event: print('Press o'))
windows.bind('<p>', lambda event: print('Press p'))
windows.bind('<q>', lambda event: print('Press q'))
windows.bind('<r>', lambda event: print('Press r'))
windows.bind('<s>', lambda event: print('Press s'))
windows.bind('<t>', lambda event: print('Press t'))
windows.bind('<u>', lambda event: print('Press u'))
windows.bind('<v>', lambda event: print('Press v'))
windows.bind('<w>', lambda event: print('Press w'))
windows.bind('<x>', lambda event: print('Press x'))
windows.bind('<y>', lambda event: print('Press y'))
windows.bind('<z>', lambda event: print('Press z'))

"""