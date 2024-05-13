from Python_Tkinter_Project_1_MilesToKiloMeter import *

def converter():
    mile_value = input_value.get()
    if mile_value.isnumeric():
        ConvertToKm=int(mile_value)*1.61
        output_string.set(ConvertToKm)
    else:
        output_string.set("Invaild input")
        input_value.set("")





