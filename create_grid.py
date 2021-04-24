import tkinter as tk

window = tk.Tk()
window.geometry('504x600')

canvas1 = tk.Canvas(window, width=504,
                            height=504,
                            highlightthickness=5,
                            highlightbackground="black",
                            bg='white')

for i in range(1,9):
    if i%3 == 0:
        canvas1.create_line(i*56, 0, i*56, 504, fill='black', width=4)
    else:
        canvas1.create_line(i*56, 0, i*56, 504, fill='grey', width=2)

for i in range(1,9):
    if i%3 == 0:
        canvas1.create_line(0, i*56, 504, i*56, fill='black', width=4)
    else:
        canvas1.create_line(0, i*56, 504, i*56, fill='grey', width=2)


canvas1.pack()
window.resizable(False, False)
window.mainloop()
                            