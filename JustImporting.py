import tkinter as tk
import random
from tkinter import font

# from tkinter import *

root = tk.Tk()
root.title("Welcome to Thundahdome!")
root.geometry('350x200')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

click_count = tk.IntVar(value=0)

lbl = tk.Label(root, text = "HERE'S A BUTTON!!")
lbl.grid(column=0, row=0, columnspan=2)

big_font = ("Helvetica", 28, "bold")
rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0, 10))

def clicked():
    click_count.set(click_count.get() + 1)
    rand = random.randint(1, 100)
    lbl.configure(text = f"Clickity click! ({click_count.get()} clicks.)")
    rand_lbl.configure(text = str(rand))

    # lbl.grid(column=0, row=1, columnspan=2)

btn = tk.Button(root, text = "CLICK IT!", fg = "purple", command=clicked)
btn.grid(column=0, row=1, columnspan=2)

root.mainloop()
