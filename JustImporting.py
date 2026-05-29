# import tkinter as tk
# import random
# import tkinter.font as tkfont

# # from tkinter import *

# root = tk.Tk()
# root.title("Welcome to Thundahdome!")
# root.geometry('480x320')

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)
# root.rowconfigure(4, weight=1)

# click_count = tk.IntVar(value=0)
# history = []

# lbl = tk.Label(root, text = "HERE'S A BUTTON!!")
# lbl.grid(column=0, row=0, columnspan=2, pady=(10, 0))

# btn = tk.Button(root, text = "CLICK IT!", fg = "purple")
# btn.grid(column=0, row=1, columnspan=2, pady=10)

# # big_font = tkfont.Font("Bauhaus 93", 55, "bold") # (font type, font size, bold)
# big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
# rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
# rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0, 10), sticky="ew", padx = 10)

# # this is the list and scrollbar box
# frame = tk.Frame(root)
# frame.grid(column=0, row=3, columnspan=2, sticky="nsew", padx = 10, pady = (0, 10))
# frame.columnconfigure(0, weight = 1)
# frame.rowconfigure(0, weight = 1)

# history_box = tk.Listbox(root, height=6, font=("Helvetica", 14), justify = "left")
# # history_box.grid(column = 0, row = 3, columnspan = 2, sticky = "nsew", padx = 10, pady =(0, 10))
# history_box.grid(column = 0, row = 0, sticky = "snew")

# scrollbar = tk.Scrollbar(frame, orient = "vertical", command = history_box.yview)
# scrollbar.grid(column = 1, row = 0, sticky = "ns")
# history_box.config(yscrollcommand = scrollbar.set)

# # root.rowconfigure(3, weight = 1)

# def clicked():
#     click_count.set(click_count.get() + 1)
#     rand = random.randint(1, 10000)
#     history.append(rand)
#     lbl.configure(text = f"Clickity click! This many clicks: {click_count.get()}")
#     rand_lbl.configure(text = str(rand))
#     history_box.insert(0, f"{len(history)}: {rand}")

#     # history_box.delete(0, tk.END)
#     # for i, val in enumerate(history, start = 1):
#     #     history_box.insert(tk.END, f"{i}. {val}")
#     # lbl.grid(column=0, row=1, columnspan=2)

# btn.configure(command=clicked)

# root.mainloop()


import tkinter as tk
import random
import tkinter.font as tkfont

root = tk.Tk()
root.title("Welcome to Thundahdome!")
root.geometry('480x320')

# allow centering/stretch
root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=1)

click_count = tk.IntVar(value=0)
history = []  # recorded numbers

lbl = tk.Label(root, text="HERE'S A BUTTON!!")
lbl.grid(column=0, row=0, columnspan=2, pady=(10,0))

btn = tk.Button(root, text="CLICK IT!", fg="purple")
btn.grid(column=0, row=1, columnspan=2, pady=10)

big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0,10), sticky="ew", padx=10)

# Listbox to show history of generated numbers
history_box = tk.Listbox(root, height=6, font=("Helvetica", 14), justify="left")
history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))

# let the history expand vertically
root.rowconfigure(3, weight=1)

def clicked():
    click_count.set(click_count.get() + 1)
    rand = random.randint(1, 10000)
    history.append(rand)
    lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)")
    rand_lbl.configure(text=str(rand))
    # update listbox (most recent at top)
    history_box.delete(0, tk.END)
    for i, val in enumerate(history, start=1):
        history_box.insert(tk.END, f"{i}: {val}")

btn.configure(command=clicked)

root.mainloop()
