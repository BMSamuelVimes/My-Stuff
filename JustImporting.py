import tkinter

from tkinter import *

root = Tk()
root.title("Welcome to Thundahdome!")
root.geometry('350x200')

click_count = IntVar(value=0)

lbl = Label(root, text = "HERE'S A BUTTON!!")
lbl.grid()

def clicked():
    click_count.set(click_count.get() + 1)
    lbl.configure(text = f"Clickity click! ({click_count.get()} clicks.)")
    lbl.grid(column=0, row=1, columnspan=2)

btn = Button(root, text = "CLICK IT!", fg = "purple", command=clicked)
btn.grid(column=1, row=0)

root.mainloop()
