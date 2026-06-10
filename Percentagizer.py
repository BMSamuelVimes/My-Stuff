# import math
# import tkinter as tk
# import random
# import tkinter.font as tkfont

# root = tk.Tk()
# root.title("Welcome to Thundahdome!")
# root.geometry('480x320')

# amount = float(input("Enter a number you want a percentage of: "))
# dblNum = int(input("What percentage of the previously entered number? "))

##############
# import tkinter as tk
# from tkinter import ttk, messagebox

# def calculate():
#     try:
#         value = float(value_var.get())
#         percent = float(percent_var.get())
#     except ValueError:
#         messagebox.showerror("Invalid input", "Please enter numeric values.")
#         return
#     result = value * (percent / 100)
#     result_var.set(f"{result:.6g}")  # compact formatting

# root = tk.Tk()
# root.title("Percentage Calculator")
# root.geometry('300x250')
# root.resizable(1, 1,)
# frm = ttk.Frame(root, padding=12)
# frm.grid()

# root.columnconfigure(0, weight=1)
# root.columnconfigure(1, weight=1)

# value_var = tk.StringVar()
# percent_var = tk.StringVar()
# result_var = tk.StringVar()

# ttk.Label(frm, text="Value:").grid(column=0, row=0, sticky="w")
# ttk.Entry(frm, textvariable=value_var, width=20).grid(column=1, row=0)

# ttk.Label(frm, text="Percent (%):").grid(column=0, row=1, sticky="w")
# ttk.Entry(frm, textvariable=percent_var, width=20).grid(column=1, row=1)

# ttk.Button(frm, text="Calculate", command=calculate).grid(column=0, row=2, columnspan=2, pady=(8,0))
# ttk.Label(frm, text="Result:").grid(column=0, row=3, sticky="w", pady=(8,0))
# ttk.Entry(frm, textvariable=result_var, state="readonly", width=20).grid(column=1, row=3, pady=(8,0))

# # Optional: bind Enter to calculate
# root.bind("<Return>", lambda e: calculate())

# root.mainloop()

############### PERCENTAGE CALCULATOR
# import tkinter as tk
# from tkinter import ttk, font, StringVar, messagebox

# class PercentApp(tk.Tk):
#     def __init__(self):
#         super().__init__()
#         self.title("PERCENTAGE CALCULATOR")
#         self.minsize(320, 180)

#         self.value_var = StringVar()
#         self.percent_var = StringVar()
#         self.result_var = StringVar()

#         # base font sizes; will be scaled
#         self.base_size = 12
#         self.app_font = font.Font(family="Segoe UI", size=self.base_size)
#         self.label_font = font.Font(family="Segoe UI", size=self.base_size)
#         self.entry_font = font.Font(family="Segoe UI", size=self.base_size)

#         self.style = ttk.Style(self)
#         self.style.configure("TLabel", font=self.label_font)
#         self.style.configure("TButton", font=self.app_font)
#         self.style.configure("TEntry", font=self.entry_font)

#         frm = ttk.Frame(self, padding=12)
#         frm.grid(sticky="nsew")
#         # make the frame expand
#         self.grid_rowconfigure(0, weight=1)
#         self.grid_columnconfigure(0, weight=1)

#         frm.grid_columnconfigure(0, weight=0)
#         frm.grid_columnconfigure(1, weight=1)
#         for r in range(4):
#             frm.grid_rowconfigure(r, weight=1)

#         ttk.Label(frm, text="VALUE:").grid(column=0, row=0, sticky="w", padx=(0,8))
#         self.value_entry = ttk.Entry(frm, textvariable=self.value_var)
#         self.value_entry.grid(column=1, row=0, sticky="ew")

#         ttk.Label(frm, text="PERCENTAGE (%):").grid(column=0, row=1, sticky="w", padx=(0,8))
#         self.percent_entry = ttk.Entry(frm, textvariable=self.percent_var)
#         self.percent_entry.grid(column=1, row=1, sticky="ew")

#         self.calc_btn = ttk.Button(frm, text="CALCULATE", command=self.calculate)
#         self.calc_btn.grid(column=0, row=2, columnspan=2, pady=(6,0))
#         # self.calc_btn.configure(anchor='center')
#         self.calc_btn.grid_configure(padx=(80,80))

#         ttk.Label(frm, text="PERCENTAGE CALC:").grid(column=0, row=3, sticky="w", padx=(0,8))
#         self.result_entry = ttk.Entry(frm, textvariable=self.result_var, state="readonly")
#         self.result_entry.grid(column=1, row=3, sticky="ew")

#         self.bind("<Configure>", self._on_resize)
#         self.bind("<Return>", lambda e: self.calculate())

#     def calculate(self):
#         try:
#             value = float(self.value_var.get())
#             percent = float(self.percent_var.get())
#         except ValueError:
#             messagebox.showerror("Invalid input", "Please enter numeric values.")
#             return
#         result = value * (percent / 100)
#         self.result_var.set(f"{result:.6g}")

#     # def _on_resize(self, event):
#     #     # scale fonts based on window height (you can tweak the divisor)
#     #     new_size = max(8, int(self.winfo_height() / 18))
#     #     if new_size != self.base_size:
#     #         self.base_size = new_size
#     #         self.app_font.configure(size=new_size)
#     #         self.label_font.configure(size=new_size)
#     #         self.entry_font.configure(size=new_size)
#     #         # also adjust internal padding for buttons if desired
#     #         self.style.configure("TButton", padding=(6, new_size//3))
    
#     def _on_resize(self, event):
#         new_size = max(8, int(self.winfo_height() / 18))
#         if new_size != self.base_size:
#             self.base_size = new_size
#             self.app_font.configure(size=new_size)
#             self.label_font.configure(size=new_size)
#             self.entry_font.configure(size=new_size)
#             # update ttk styles so entries pick up the new font
#             self.style.configure("TButton", padding=(6, max(2, new_size//3)))
#             self.style.configure("TEntry", font=self.entry_font)
#             self.style.configure("TLabel", font=self.label_font)
#             # adjust entry internal padding (vertical) so the widget height scales
#             ipady = max(2, new_size // 4)
#             # apply ipady by re-gridding entries (grid_configure accepts ipady)
#             self.value_entry.grid_configure(ipady=ipady)
#             self.percent_entry.grid_configure(ipady=ipady)
#             self.result_entry.grid_configure(ipady=ipady)
#             # optional: limit button width with padx to keep it visually centered
#             self.calc_btn.grid_configure(padx=(max(10, new_size*3), max(10, new_size*3)))

# if __name__ == "__main__":
#     PercentApp().mainloop()


import tkinter as tk
from tkinter import ttk, font, StringVar, messagebox

class PercentApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PERCENTAGE CALCULATOR")
        self.minsize(360, 220)

        self.value_var = StringVar()
        self.percent_var = StringVar()
        self.result_var = StringVar()
        self.mode_var = StringVar(value="part_of")  # "part_of" or "percent_of"

        # base font sizes; will be scaled
        self.base_size = 12
        self.app_font = font.Font(family="Segoe UI", size=self.base_size)
        self.label_font = font.Font(family="Segoe UI", size=self.base_size)
        self.entry_font = font.Font(family="Segoe UI", size=self.base_size)

        self.style = ttk.Style(self)
        self.style.configure("TLabel", font=self.label_font)
        self.style.configure("TButton", font=self.app_font)
        self.style.configure("TEntry", font=self.entry_font)
        self.style.configure("TRadiobutton", font=self.app_font)

        frm = ttk.Frame(self, padding=12)
        frm.grid(sticky="nsew")
        # make the frame expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # labels column stays tight, inputs column expands
        frm.grid_columnconfigure(0, weight=0)
        frm.grid_columnconfigure(1, weight=1)
        for r in range(6):
            frm.grid_rowconfigure(r, weight=1)

        ttk.Label(frm, text="VALUE (A):").grid(column=0, row=0, sticky="w", padx=(0,8))
        self.value_entry = ttk.Entry(frm, textvariable=self.value_var)
        self.value_entry.grid(column=1, row=0, sticky="ew")

        ttk.Label(frm, text="BASE (B):").grid(column=0, row=1, sticky="w", padx=(0,8))
        self.percent_entry = ttk.Entry(frm, textvariable=self.percent_var)
        self.percent_entry.grid(column=1, row=1, sticky="ew")

        # Mode selection
        modes_frm = ttk.Frame(frm)
        modes_frm.grid(column=0, row=2, columnspan=2, pady=(6,0))
        rb1 = ttk.Radiobutton(modes_frm, text="Calculate A × (percent/100)", variable=self.mode_var, value="part_of")
        rb2 = ttk.Radiobutton(modes_frm, text="Calculate percent: A is what % of B", variable=self.mode_var, value="percent_of")
        rb1.grid(column=0, row=0, padx=(0,8))
        rb2.grid(column=1, row=0)

        # Centered button spanning both columns
        self.calc_btn = ttk.Button(frm, text="CALCULATE", command=self.calculate)
        self.calc_btn.grid(column=0, row=3, columnspan=2, pady=(8,0))
        self.calc_btn.grid_configure(padx=(80,80))

        ttk.Label(frm, text="RESULT:").grid(column=0, row=4, sticky="w", padx=(0,8), pady=(8,0))
        self.result_entry = ttk.Entry(frm, textvariable=self.result_var, state="readonly")
        self.result_entry.grid(column=1, row=4, sticky="ew", pady=(8,0))

        self.bind("<Configure>", self._on_resize)
        self.bind("<Return>", lambda e: self.calculate())

    def calculate(self):
        mode = self.mode_var.get()
        try:
            a = float(self.value_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a numeric VALUE (A).")
            return

        # Mode: part_of => result = A * (percent/100) where percent is entered in percent_var
        if mode == "part_of":
            try:
                percent = float(self.percent_var.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a numeric PERCENT.")
                return
            result = a * (percent / 100)
            self.result_var.set(f"{result:.6g}")
            return

        # Mode: percent_of => percent = (A / B) * 100
        if mode == "percent_of":
            try:
                b = float(self.percent_var.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a numeric BASE (B).")
                return
            if b == 0:
                messagebox.showerror("Math error", "BASE (B) cannot be zero.")
                return
            percent = (a / b) * 100
            self.result_var.set(f"{percent:.6g} %")
            return

    def _on_resize(self, event):
        new_size = max(8, int(self.winfo_height() / 18))
        if new_size != self.base_size:
            self.base_size = new_size
            self.app_font.configure(size=new_size)
            self.label_font.configure(size=new_size)
            self.entry_font.configure(size=new_size)
            # update ttk styles
            self.style.configure("TButton", padding=(6, max(2, new_size//3)))
            self.style.configure("TEntry", font=self.entry_font)
            self.style.configure("TLabel", font=self.label_font)
            self.style.configure("TRadiobutton", font=self.app_font)
            # adjust entry internal padding (vertical) so the widget height scales
            ipady = max(2, new_size // 4)
            self.value_entry.grid_configure(ipady=ipady)
            self.percent_entry.grid_configure(ipady=ipady)
            self.result_entry.grid_configure(ipady=ipady)
            # adjust button padding to keep visual centering
            self.calc_btn.grid_configure(padx=(max(10, new_size*4), max(10, new_size*4)))

if __name__ == "__main__":
    PercentApp().mainloop()