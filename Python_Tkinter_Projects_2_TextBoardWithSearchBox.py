import tkinter as tk
from tkinter import ttk

window = tk.Tk()

window.geometry("800x600")
window.title("Search Board")

main_file_date = tk.StringVar()
white_board = tk.Text(window)
white_board.pack()

search_bar = tk.Entry(window)
search_bar.pack()

final_button = tk.Button(window, text="Check Button")
final_button.pack()

window.mainloop()