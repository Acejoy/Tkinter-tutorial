import tkinter as tk
import copy

def possible(grid, row, col, val):
    # valid in the sub-grid
    sub_grid_index = (row//3, col//3)

    for i in range(3):
        for j in range(3):
            if grid[sub_grid_index[0]*3 +i][sub_grid_index[1]*3 +j] == val :
                #print('1!')
                return False

    # valid in the row
    for i in range(9):
        if grid[row][i] == val:
            #print('2@')
            return False

    # valid in the col
    for i in range(9):
        if grid[i][col] == val:
            #print('3#')
            return False

    return True

def is_valid(x):
    print(type(x))
    print(x)

    return_val = False

    if x=='':
        validLabel.config(text='')
        return_val = True
    elif x.isdigit() and possible(query_puzzle, ):                        
        return_val = False
    else:
        validLabel.config(text='')
        return_val = True

    return return_val

def invalid(wid, root):
    req_widget = root.nametowidget(wid)
    req_widget.delete(0, tk.END)
    validLabel.config(text='Not Valid')
    return 

puzzle =    [[7,9,4,0,8,0,0,3,2],
             [0,2,1,4,0,0,5,9,0],
             [3,0,5,0,0,0,0,0,4],
             [1,3,9,0,6,5,0,2,0],
             [0,0,0,2,4,3,0,0,0],
             [0,4,0,7,0,1,0,0,0],
             [4,5,3,0,0,0,8,0,0],
             [0,6,7,0,5,0,3,0,9],
             [0,0,8,3,0,0,0,5,0]]

query_puzzle = copy.deepcopy(puzzle)

window = tk.Tk()
window.geometry('504x600')

sv = tk.StringVar()

canvas1 = tk.Canvas(window, width=504,
                            height=504,
                            bg='white')

canvas2 = tk.Canvas(window, width=504,
                            height=96,
                            bg='white')

validatefunction = canvas1.register(is_valid)
invalidatefunction = canvas1.register(invalid)

validLabel = tk.Label(text='')
canvas2.create_window(30,30, window=validLabel)

# for i in range(1,9):
#     if i%3 == 0:
#         canvas1.create_line(0, i*56, 504, i*56, fill='black', width=10)



for i in range(9):
    for j in range(9):
        if puzzle[i][j]!=0:
            req_widget = tk.Label(text = puzzle[i][j], bg ='white', relief='solid',
                                    borderwidth=1)    
        else:
            req_widget = tk.Entry(validate='key' ,
                    validatecommand=(validatefunction, '%P'), 
                    highlightthickness=1,
                    highlightbackground="black")

            req_widget.config(invalidcommand=(invalidatefunction,req_widget, window))
            

        #entry.place(x=100,y=100, width=200, height = 100)        
        canvas1.create_window(i*56+29,j*56+29, height = 56, width=56, window=req_widget)



canvas1.pack()
canvas2.pack()
window.resizable(False, False)
window.mainloop()