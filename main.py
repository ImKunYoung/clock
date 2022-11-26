# Path: main.py
# GUI clock
# This program displays a digital clock with a GUI

from tkinter import *
from time import strftime

win = Tk()
win.attributes("-topmost", 1)
win.overrideredirect(1)


def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)


label = Label(win, font=("ds-digital", 10), background="black", foreground="white")


def drag_start(event):
    win.x = event.x
    win.y = event.y


def drag_motion(event):
    x = (event.x_root - win.x - win.winfo_rootx() + win.winfo_rootx())
    y = (event.y_root - win.y - win.winfo_rooty() + win.winfo_rooty())
    win.geometry("+%s+%s" % (x, y))


def change_color(event):
    if label.cget("foreground") == "white":
        label.config(foreground="black")
        label.config(background="white")
    else:
        label.config(foreground="white")
        label.config(background="black")


label.bind("<Button-1>", drag_start)
label.bind("<B1-Motion>", drag_motion)
label.bind("<Button-2>", change_color)
label.bind('<Button-3>', lambda e: win.destroy())
label.pack(anchor='center')

time()

mainloop()
