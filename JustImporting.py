######### BASE RANDOM COUNT
import tkinter as tk
import random
import tkinter.font as tkfont
from tkinter import ttk

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


header_font = tkfont.Font(family="Helvetica", size=12, weight="bold")
row_font = tkfont.Font(family="Rockwell", size=10, weight= "bold")
# col2_font = tkfont.Font(family="Rockwell", size=10, weight="bold") ######
style = ttk.Style()
style.configure("Custom.Treeview.Heading", font=header_font)
style.configure("Custom.Treeview", font=row_font) 

columns = ("#1", "#2")
history_tree = ttk.Treeview(root, columns=columns, show="headings", style="Custom.Treeview", height = 6)
history_tree.heading("#1", text= "THE NUMBER")
history_tree.heading("#2", text="IS DUPE?")
history_tree.column("#1", width=300, anchor="w")
history_tree.column("#2", width=60, anchor="w")
# history_tree.tag_configure("col2_style", foreground="green", font=col2_font) ######

history_tree.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))

root.rowconfigure(3, weight=1)

btn_font2 = tkfont.Font(family = "Arial Black", size=10)
reset_btn = tk.Button(root, text="RESET", fg="red", font=btn_font2)

def do_reset():
    click_count.set(0)
    history.clear()
    lbl.configure(text = "HERE'S A BUTTON!!\nIt's down there but you can see that.")
    rand_lbl.configure(text = "")
    for item in history_tree.get_children():
        history_tree.delete(item)
    # history_box.delete(0, tk.END)
    reset_btn.grid_forget()

reset_btn.configure(command = do_reset)


def clicked():
    click_count.set(click_count.get() + 1)
    rand = random.randint(1, 100)
    history.append(rand)
    counts = {}
    for n in history:
        counts[n] = counts.get(n, 0) + 1
    
    lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)\n")
    rand_lbl.configure(text=str(rand))

    for item in history_tree.get_children():
        history_tree.delete(item)

    # history_box.delete(0, tk.END)
    # width = 60
    # total = len(history) + 1
    for i, val in enumerate(history, start=1):
        # idx = i - 1
        occ = counts[val]
        val_text = "" if occ==1 else f"\u2461 {occ}"
        history_tree.insert("", tk.END, values=(f"{i}: {val}", val_text))
        # history_tree.insert("", tk.END, values=(f"{i}: {val}", val_text), tags=("col2_style",)) CHANGE THE COLOR OF THE COLOMNS FONT
 
        # if occ == 1:
        #     history_box.insert(tk.END, base)
        # else:
        #     history_box.insert(tk.END, f"{base:<{width}} (\u2461 {occ})")

    if click_count.get() == 1:
        # reset_btn.grid(column = 0, row = 5, columnspan = 2, pady = (0, 10))
        reset_btn.grid(column = 1, row = 4, padx = (0, 10), pady = 10, sticky = "e")

btn.configure(command=clicked)

root.mainloop()

# ######### BASE RANDOM COUNT
# import tkinter as tk
# import random
# import tkinter.font as tkfont

# root = tk.Tk()
# root.title("Welcome to Thundahdome!")
# root.geometry('480x320')

# # allow centering/stretch
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)

# click_count = tk.IntVar(value=0)
# history = []  # recorded numbers

# lbl = tk.Label(root, text="HERE'S A BUTTON!!\nIt's down there but you can see that.")
# lbl.grid(column=0, row=0, columnspan=2, pady=(10,0))

# btn_font = tkfont.Font(family = "Bauhaus 93", size=10)
# btn = tk.Button(root, text="CLICK IT!", fg="purple", font = btn_font)
# btn.grid(column=0, row=4, columnspan=2, pady=10)

# big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
# rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
# rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0,10), sticky="ew", padx=10)

# # Listbox to show history of generated numbers
# history_box = tk.Listbox(root, height=6, font=("Helvetica", 14), justify="left")
# history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
# # let the history expand vertically
# root.rowconfigure(3, weight=1)

# btn_font2 = tkfont.Font(family = "Arial Black", size=10)
# reset_btn = tk.Button(root, text="RESET", fg="red", font=btn_font2)

# def do_reset():
#     click_count.set(0)
#     history.clear()
#     lbl.configure(text = "HERE'S A BUTTON!!\nIt's down there but you can see that.")
#     rand_lbl.configure(text = "")
#     history_box.delete(0, tk.END)
#     reset_btn.grid_forget()

# reset_btn.configure(command = do_reset)


# def clicked():
#     click_count.set(click_count.get() + 1)
#     rand = random.randint(1, 100)
#     history.append(rand)
#     counts = {}
#     for n in history:
#         counts[n] = counts.get(n, 0) + 1

#     # history.append(rand)
#     # history_box.insert(0, f"{len(history)}: {rand}")
    
#     lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)")
#     rand_lbl.configure(text=str(rand))
#     # update listbox (most recent at top)
    
#     history_box.delete(0, tk.END)
#     width = 60
#     for i, val in enumerate(history, start=1):
#         occ = counts[val]
#         base = f"{i}: {val}"
#         if occ == 1:
#             history_box.insert(tk.END, base)
#         else:
#             history_box.insert(tk.END, f"{base:<{width}} (\u2461 {occ})")

#     if click_count.get() == 1:
#         # reset_btn.grid(column = 0, row = 5, columnspan = 2, pady = (0, 10))
#         reset_btn.grid(column = 1, row = 4, padx = (0, 10), pady = 10, sticky = "e")

# btn.configure(command=clicked)

# root.mainloop()

# #### History display
# import tkinter as tk
# import random
# import tkinter.font as tkfont

# root = tk.Tk()
# root.title("Welcome to Thundahdome!")
# # root.geometry('480x320')

# root.update_idletasks()
# fixed_width = 480
# h = root.winfo_height()
# w = fixed_width

# x = (root.winfo_screenwidth() // 2) - (w // 2)
# y = (root.winfo_screenheight() // 2) - (h // 2)
# root.geometry(f"{w}x{h}+{x}+{y}")

# root.resizable(False, True)

# # allow centering/stretch
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)

# click_count = tk.IntVar(value=0)
# history = []  # recorded numbers

# lbl = tk.Label(root, text="HERE'S A BUTTON!!\nIt's down there but you can see that.")
# lbl.grid(column=0, row=0, columnspan=2, pady=(10,0))

# btn_font = tkfont.Font(family = "Bauhaus 93", size=10)
# btn = tk.Button(root, text="CLICK IT!", fg="purple", font = btn_font)
# btn.grid(column=0, row=4, columnspan=2, pady=10)

# big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
# rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
# rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0,10), sticky="ew", padx=10)

# # Listbox to show history of generated numbers
# history_box = tk.Listbox(root, height=6, font=("Arial", 14), justify="left")
# # history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
# # let the history expand vertically
# def show_history():
#     history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
#     root.rowconfigure(3, weight=1)
#     apply_window_size(expand_for_history=True, history_entries=len(history))

# def update_history_box():
#     history_box.delete(0, tk.END)
#     counts = {}
#     for n in history:
#         counts[n] = counts.get(n, 0) + 1
#     for i, val in enumerate(history, start=1):
#         occ = counts[val]
#         if occ == 1:
#             history_box.insert(tk.END, f"{i}: {val}")
#         else:
#             history_box.insert(tk.END, f"{i}: {val} (DUPE - {occ})")

# def apply_window_size(expand_for_history=False, history_entries=0):
#     root.update_idletasks()
#     base_width = 480
#     # compute extra width needed when showing history: one item ~ approx 14 pixels per char; estimate by length of longest entry
#     extra = 0
#     if expand_for_history and history_entries > 0:
#         # cap visible entries considered to 5
#         visible = min(history_entries, 5)
#         # estimate longest text in listbox lines
#         longest = 0
#         for i in range(len(history)-visible, len(history)):
#             if i >= 0:
#                 text = f"{i+1}: {history[i]}"
#                 longest = max(longest, len(text))
#         # estimate per-character pixel width for listbox font
#         avg_char_px = 8  # adjust if font differs
#         extra = max(0, longest * avg_char_px - (base_width - 40))  # 40 for paddings
#     w = base_width + extra
#     h = root.winfo_height()
#     x = (root.winfo_screenwidth() // 2) - (w // 2)
#     y = (root.winfo_screenheight() // 2) - (h // 2)
#     root.geometry(f"{w}x{h}+{x}+{y}")
#     # allow vertical resize only; lock horizontal
#     root.resizable(False, True)
#     root.minsize(w, h)

# btn_font2 = tkfont.Font(family = "Arial Black", size=10)
# reset_btn = tk.Button(root, text="RESET", fg="red", font=btn_font2)

# def do_reset():
#     click_count.set(0)
#     history.clear()
#     lbl.configure(text = "HERE'S A BUTTON!!\nIt's down there but you can see that.")
#     rand_lbl.configure(text = "")
#     history_box.delete(0, tk.END)
#     history_box.grid_forget()
#     reset_btn.grid_forget()
#     apply_window_size(expand_for_history=False, history_entries=0)

# reset_btn.configure(command = do_reset)


# def clicked():
#     click_count.set(click_count.get() + 1)
#     rand = random.randint(1, 100)
#     history.append(rand)

#     if len(history) == 1:
#         show_history()
#     # counts = {}
#     # for n in history:
#     #     counts[n] = counts.get(n, 0) + 1

#     # history.append(rand)
#     # history_box.insert(0, f"{len(history)}: {rand}")
    
#     lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)")
#     rand_lbl.configure(text=str(rand))
#     update_history_box()
#     apply_window_size(expand_for_history=True, history_entries=len(history))
#     # update listbox (most recent at top)
    
#     # history_box.delete(0, tk.END)
#     # for i, val in enumerate(history, start=1):
#     #     occ = counts[val]
#     #     if occ == 1:
#     #         history_box.insert(tk.END, f"{i}: {val}")
#     #     else:
#     #         history_box.insert(tk.END, f"{i}: {val} (DUPE - {occ})")

#     if click_count.get() == 1:
#         # reset_btn.grid(column = 0, row = 5, columnspan = 2, pady = (0, 10))
#         reset_btn.grid(column = 1, row = 4, padx = (0, 10), pady = 10, sticky = "e")

# btn.configure(command=clicked)

# root.mainloop()



# #### History display STILL FLICKERS WHOLE APP.
# import tkinter as tk
# import random
# import tkinter.font as tkfont

# root = tk.Tk()
# root.title("Welcome to Thundahdome!")
# root.update_idletasks()
# fixed_width = 480
# h = root.winfo_height()
# w = fixed_width
# x = (root.winfo_screenwidth() // 2) - (w // 2)
# y = (root.winfo_screenheight() // 2) - (h // 2)
# root.geometry(f"{w}x{h}+{x}+{y}")
# root.resizable(False, True)
# # allow centering/stretch
# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)

# click_count = tk.IntVar(value=0)
# history = []  # recorded numbers

# lbl = tk.Label(root, text="HERE'S A BUTTON!!\nIt's down there but you can see that.")
# lbl.grid(column=0, row=0, columnspan=2, pady=(10,0))

# btn_font = tkfont.Font(family = "Bauhaus 93", size=10)
# btn = tk.Button(root, text="CLICK IT!", fg="purple", font = btn_font)
# btn.grid(column=0, row=4, columnspan=2, pady=10)

# big_font = tkfont.Font(family = "Bauhaus 93", size=55, weight = "bold", slant="italic")
# rand_lbl = tk.Label(root, text="", font=big_font, fg="blue")
# rand_lbl.grid(column=0, row=2, columnspan=2, pady=(0,10), sticky="ew", padx=10)

# # Listbox to show history of generated numbers
# history_box = tk.Listbox(root, height=5, font=("Arial", 14), justify="left")
# # history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
# # let the history expand vertically

# _current_width = None
# _layout_busy = False

# def show_history():
#     history_box.grid(column=0, row=3, columnspan=2, sticky="nsew", padx=10, pady=(0,10))
#     root.rowconfigure(3, weight=1)
#     root.update_idletasks()
#     apply_window_size(expand_for_history=True, history_entries=len(history))

# def update_history_box(expand_for_history=True, history_entries=0):
#     history_box.delete(0, tk.END)
#     counts = {}
#     for n in history:
#         counts[n] = counts.get(n, 0) + 1
#     for i, val in enumerate(reversed(history), start=1):
#         orig_index = len(history) - i + 1
#         occ = counts[val]
#         if occ == 1:
#             line = f"{orig_index}: {val}"
#         else:
#             line = f"{orig_index}: {val} (DUPE - {occ})"
#         history_box.insert(0, line)

# # def apply_window_size(expand_for_history=False, history_entries=0):
# #     root.update_idletasks()
# #     base_width = 480
# #     # compute extra width needed when showing history: one item ~ approx 14 pixels per char; estimate by length of longest entry
# #     extra = 0
# #     if expand_for_history and history_entries > 0:
# #         # cap visible entries considered to 5
# #         visible = min(history_entries, 5)
# #         # estimate longest text in listbox lines
# #         longest = 0
# #         for i in range(len(history)-visible, len(history)):
# #             if i >= 0:
# #                 text = f"{i+1}: {history[i]}"
# #                 longest = max(longest, len(text))
# #         # estimate per-character pixel width for listbox font
# #         avg_char_px = 8  # adjust if font differs
# #         extra = max(0, longest * avg_char_px - (base_width - 40))  # 40 for paddings
# #     w = base_width + extra
# #     geo= root.geometry()
# #     parts = geo.split('+')
# #     size = parts[0]
# #     cur_x = int(parts[1]) if len(parts) > 1 else x
# #     cur_y = int(parts[2]) if len(parts) > 2 else y
# #     cur_h = root.winfo_height()
# #     root.geometry(f"{w}x{cur_h}+{cur_x}+{cur_y}")
# #     # allow vertical resize only; lock horizontal
# #     root.resizable(False, True)
# #     root.minsize(w, cur_h)

# btn_font2 = tkfont.Font(family = "Arial Black", size=10)
# reset_btn = tk.Button(root, text="RESET", fg="red", font=btn_font2)

# def do_reset():
#     click_count.set(0)
#     history.clear()
#     lbl.configure(text = "HERE'S A BUTTON!!\nIt's down there but you can see that.")
#     rand_lbl.configure(text = "")
#     history_box.delete(0, tk.END)
#     history_box.grid_forget()
#     reset_btn.grid_forget()
#     apply_window_size(expand_for_history=False, history_entries=0)

# reset_btn.configure(command = do_reset)

# def clicked():
#     click_count.set(click_count.get() + 1)
#     rand = random.randint(1, 100)
#     history.append(rand)

#     if len(history) == 1:
#         show_history()
    
#     lbl.configure(text=f"Clickity click! ({click_count.get()} clicks.)")
#     rand_lbl.configure(text=str(rand))
#     update_history_box()
#     apply_window_size(expand_for_history=True, history_entries=len(history))

#     if click_count.get() == 1:
#         reset_btn.grid(column = 1, row = 4, padx = (0, 10), pady = 10, sticky = "e")

# btn.configure(command=clicked)

# root.mainloop()
