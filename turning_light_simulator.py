import time
# import tkinter as tk
from tkinter import *

# Build the Frame
root = Tk()
root.title('BE-Lab  turn signal')
root.geometry("400x250")

count = 0
prediction = [i % 3 for i in range(50)]

frame = Frame(root)
frame.pack()

but_frame = Frame(root)
but_frame.pack(side=BOTTOM)


button_l = Button(frame,
                   text = 'left <-',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)

button_m = Button(frame,
                   text = 'front',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)

button_r = Button(frame,
                   text = '-> right',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)


time_str = StringVar()
time_str.set('start')

def getTime():
    global count
    global prediction
    time_str.set(time.strftime("%H:%M:%S"))
    button_l.configure(bg="white")
    button_m.configure(bg="white")
    button_r.configure(bg="white")

    if prediction[count] == 0:
        print('left')
        button_l.configure(bg="red")
    elif prediction[count] == 1:
        print('mid')
        button_m.configure(bg="blue")
    elif prediction[count] == 2:
        print('right')
        button_r.configure(bg="green")
    else:
        raise ValueError
    
    root.after(1000, getTime)
    count += 1

def showTime():
    print(time_str.get())


button_l.pack(side=LEFT)
button_m.pack(side=LEFT)
button_r.pack(side=LEFT)

button_time = Button(but_frame,
                   text = 'right',
                   textvariable=time_str,
                   bg = 'white',
                   fg = 'black',
                   font = ('Comic Sans MS', 22),
                   width=7, height=1,
                   command = getTime)

button_time.pack(side=BOTTOM)

root.mainloop()