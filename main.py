import tkinter as tk
window = tk.Tk()
w1 = '504x504'
window.geometry('504x600')
bg = tk.PhotoImage(file='grid.png')

canvas1 = tk.Canvas(window, width = 504,
                        height = 504,
                            highlightthickness=5,
                             highlightbackground="grey")
canvas1.pack()
canvas1.create_image(0,0, image=bg,
                        anchor='nw')

# greeting = tk.Label(canvas1, text="Hello, Tkinter")
# greeting.pack()
# canvas1.create_window(300, 100, window=greeting)
canvas2 = tk.Canvas(window,bg='red', width = 504,
                        height = 96)
canvas2.pack()
greeting = tk.Label(canvas2, text="Hello, Tkinter")
greeting.pack()
canvas2.create_window(300, 10, window=greeting)

window.resizable(False, False)
window.mainloop()