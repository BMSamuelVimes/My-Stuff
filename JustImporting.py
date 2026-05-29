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

lbl = tk.Label(root, text="HERE'S A BUTTON!!\nIt's down there but you can see that.")
lbl.grid(column=0, row=0, columnspan=2, pady=(10,0))

btn_font = tkfont.Font(family = "Bauhaus 93", size=10)
btn = tk.Button(root, text="CLICK IT!", fg="purple", font = btn_font)
btn.grid(column=0, row=4, columnspan=2, pady=10)

big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0,10), sticky="ew", padx=10)

# Listbox to show history of generated numbers
history_box = tk.Listbox(root, height=6, font=("Helvetica", 14), justify="left")
history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
# let the history expand vertically
root.rowconfigure(3, weight=1)

btn_font2 = tkfont.Font(family = "Arial Black", size=10)
reset_btn = tk.Button(root, text="RESET", fg="red", font=btn_font2)

def do_reset():
    click_count.set(0)
    history.clear()
    lbl.configure(text = "HERE'S A BUTTON!!\nIt's down there but you can see that.")
    rand_lbl.configure(text = "")
    history_box.delete(0, tk.END)
    reset_btn.grid_forget()

reset_btn.configure(command = do_reset)


def clicked():
    click_count.set(click_count.get() + 1)
    rand = random.randint(1, 100)
    history.append(rand)
    counts = {}
    for n in history:
        counts[n] = counts.get(n, 0) + 1

    # history.append(rand)
    # history_box.insert(0, f"{len(history)}: {rand}")
    
    lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)")
    rand_lbl.configure(text=str(rand))
    # update listbox (most recent at top)
    
    history_box.delete(0, tk.END)
    for i, val in enumerate(history, start=1):
        occ = counts[val]
        if occ == 1:
            history_box.insert(tk.END, f"{i}: {val}")
        else:
            history_box.insert(tk.END, f"{i}: {val} (DUPE - {occ})")

    if click_count.get() == 1:
        # reset_btn.grid(column = 0, row = 5, columnspan = 2, pady = (0, 10))
        reset_btn.grid(column = 1, row = 4, padx = (0, 10), pady = 10, sticky = "e")

btn.configure(command=clicked)

root.mainloop()
