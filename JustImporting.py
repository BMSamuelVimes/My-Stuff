import tkinter

from tkinter import *

root = Tk()
root.title("Welcome to Thundahdome!")
root.geometry('350x200')

lbl = Label(root, text = "HERE'S A BUTTON!!")
lbl.grid()

def clicked():
    lbl.configure(text = "Clickity click!")

btn = Button(root, text = "CLICK IT!", fg = "purple", command=clicked)
btn.grid(column=1, row=0)

root.mainloop()
