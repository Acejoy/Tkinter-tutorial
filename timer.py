import tkinter as tk
import time

window = tk.Tk()
w1 = '504x504'
window.geometry('504x600')
canvas2 = tk.Canvas(window,bg='red', width = 504,
                        height = 96)
greeting = tk.Label(text="")
canvas2.create_window(30,30, window=greeting)



canvas2.pack()
window.resizable(False, False)
window.mainloop()