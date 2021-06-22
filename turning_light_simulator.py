from os import stat
import time
# import tkinter as tk
from tkinter import *
from typing import Sized, TextIO

# Build the Frame
root = Tk()
root.title('BE-Lab  turn signal')
root.geometry("800x600")

def turn_light(predict):
    lights = []
    left_lights = [0, 0, -1, 0, 0]
    right_lights = [2, 2, -1, 2, 2]
    radius = 10
    step = len(left_lights)
    j = radius
    while j < len(predict):
        candidate = predict[j-radius : j]
        p = max(set(candidate), key=candidate.count)
        if p == 1:
            lights.extend([1 for _ in range(step)])
        elif p == 0:
            lights.extend(left_lights)
        elif p == 2:
            lights.extend(right_lights)
        else:
            raise ValueError("Illegal predict!!")
        j += step
    return lights


count = 0
# prediction = [i % 3 for i in range(50)]
# prediction = [(i//10)%3 for i in range(50)]
raw_predict = []
with open('predict.txt', 'r') as f:
    line = f.readline().strip('\n').split(',')
    for p in line:
        try:
            raw_predict.append(int(p))
        except:
            pass
print(f"len(raw_predict) = {len(raw_predict)}, total {len(raw_predict)/10} secs")
lights = turn_light(raw_predict)
prediction = [1 for _ in range(2)]
prediction.extend(raw_predict)
print(len(prediction))
print(f"len(turn_lights) = {len(lights)}, total {len(lights)/10} secs")


top_frame = Frame(root)
top_frame.pack(side=TOP, pady=32)


frame = Frame(root)
frame.pack(pady=64)

but_frame = Frame(root)
but_frame.pack(side=BOTTOM, pady=32)


button_l = Button(frame,
                   text = '\U0001f814\nleft ',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)
button_l.grid(row=0, column=0, padx=64)

button_m = Button(frame,
                   text = '\U0001f815\nfront',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)
button_m.grid(row=0, column=1, padx=64)

button_r = Button(frame,
                   text = '\U0001f816\nright',
                   bg = 'white',
                   font = ('Comic Sans MS', 22),
                   width=5, height=2,
                   command = None)

button_r.grid(row=0, column=2, padx=64)

time_str = StringVar()
time_str.set('start')
direction_str = StringVar()
direction_str.set('brain\n\U0001f815')

def getTime():
    global count
    global prediction
    time_str.set(time.strftime("%H:%M:%S"))
    button_l.configure(bg="white")
    button_m.configure(bg="white")
    button_r.configure(bg="white")
    try:
        if prediction[count] == 0:
            direction_str.set('brain\n\U0001f814')
        elif prediction[count] == 1:
            direction_str.set('brain\n\U0001f815')
        elif prediction[count] == 2:
            direction_str.set('brain\n\U0001f816')
        else:
            raise ValueError("Illegal value in prediction {count}")
        if lights[count] == 0:
            print('left')
            button_l.configure(bg="red")
        elif lights[count] == 1:
            print('mid')
            button_m.configure(bg="gray")
        elif lights[count] == 2:
            print('right')
            button_r.configure(bg="green")
        elif lights[count] == -1:
            pass
        else:
            raise ValueError("Illegal value in lights {count}")
        
        root.after(100, getTime)
        count += 1
    except:
        raise RuntimeError("Prediction output done")
        exit()

def showTime():
    print(time_str.get())


button_time = Button(but_frame,
                   text = 'right',
                   textvariable=time_str,
                   bg = 'white',
                   fg = 'black',
                   font = ('Comic Sans MS', 22),
                   width=10, height=1,
                   command = getTime)

button_predict = Button(top_frame,
                   textvariable=direction_str,
                   bg = 'white',
                   fg = 'black',
                   font = ('Comic Sans MS', 30),
                   width=7, height=2)

button_predict.grid(row=0, column=0)
button_time.grid(row=2, column=0)
# button_time.pack(side=BOTTOM)

root.mainloop()