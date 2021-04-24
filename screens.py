import tkinter as tk

class Screen:

    def __init__(self, image_num, win=None):
        
        if win is None:
            self.window = tk.Toplevel()
        else:
            self.window = win

        self.window.geometry('400x225')
        self.window.resizable(False, False)

        image_name  = None
        if image_num == 1:
            image_name = 'images/img1.png'

        elif image_num == 2:
            image_name = 'images/img2.png'

        elif image_num == 3:
            image_name = 'images/img3.png'

        bg = tk.PhotoImage(file=image_name)
        self.bg_label = tk.Label(self.window, image=bg)
        #self.bg_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.bg_label.pack()
        #self.display()
        self.window.mainloop()

            

if __name__ == '__main__':
    win = tk.Tk()
    imgscreen = Screen(1, win)   