# ############ PERCENT CALCULATOR AND NUMBER PERCENTAGE OF NUMBER CALCULATOR 
# ############ PERCENT CALCULATOR AND NUMBER PERCENTAGE OF NUMBER CALCULATOR RESULTS CENTERED XXXXXHAS ISSUES!!!!!XXXXXX
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
        self.formula_var = StringVar()

        self.mode_var = StringVar(value="part_of")  # "part_of" or "percent_of"

        # base font sizes; will be scaled
        self.base_size = 12
        self.app_font = font.Font(family="Segoe UI", size=self.base_size)
        self.label_font = font.Font(family="Segoe UI", size=self.base_size)
        self.entry_font = font.Font(family="Segoe UI", size=self.base_size)

        # enlarged/bold font ONLY for the result
        self.result_base_size = int(self.base_size * 3)
        self.result_font = font.Font(family="Segoe UI", size=self.result_base_size, weight="bold")

        # Button styles (color differs for CALCULATE vs CLEAR)
        self.style = ttk.Style(self)

        self.style.configure("Calc.TButton", font=self.app_font)
        self.style.configure("Clear.TButton", font=self.app_font, foreground="red", background="#d32f2f")

        # ttk on some platforms ignores background for default themes;
        # still, configure works where supported.
        try:
            self.style.map("Calc.TButton", background=[("active", "#e3e3e3")])
            self.style.map("Clear.TButton", background=[("active", "#b71c1c")])
        except tk.TclError:
            pass

        frm = ttk.Frame(self, padding=12)
        frm.grid(sticky="nsew")

        # make the frame expand
        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # labels column stays tight, inputs column expands
        frm.grid_columnconfigure(0, weight=0)
        frm.grid_columnconfigure(1, weight=1)

        # We now have 7 rows (0..6)
        for r in range(7):
            frm.grid_rowconfigure(r, weight=1)

        ttk.Label(frm, text="VALUE (A):").grid(column=0, row=0, sticky="w", padx=(0, 8))
        self.value_entry = ttk.Entry(frm, textvariable=self.value_var)
        self.value_entry.grid(column=1, row=0, sticky="ew")

        ttk.Label(
            frm,
            text="\u0332".join("PERCENT % (B)") + "\nTOTAL # (C):"
        ).grid(column=0, row=1, sticky="w", padx=(0, 8))

        self.percent_entry = ttk.Entry(frm, textvariable=self.percent_var)
        self.percent_entry.grid(column=1, row=1, sticky="ew")

        # Mode selection
        modes_frm = ttk.Frame(frm)
        modes_frm.grid(column=0, row=2, columnspan=2, pady=(6, 0), sticky="ew")

        rb1 = ttk.Radiobutton(
            modes_frm,
            text="WHAT IS (B)% OF (A)",
            variable=self.mode_var,
            value="part_of"
        )
        rb2 = ttk.Radiobutton(
            modes_frm,
            text="VALUE (A) is what % of TOTAL # (C)",
            variable=self.mode_var,
            value="percent_of"
        )
        rb1.grid(column=0, row=0, padx=(0, 8))
        rb2.grid(column=1, row=0)

        # Button switches between Calculate and Clear (style changes too)
        self.calc_btn = ttk.Button(
            frm,
            text="CALCULATE",
            command=self.calculate_or_clear,
            style="Calc.TButton"
        )
        self.calc_btn.grid(column=0, row=3, columnspan=2, pady=(8, 0))
        self.calc_btn.grid_configure(padx=(80, 80))

        # Output area
        self.formula_label = ttk.Label(
            frm,
            textvariable=self.formula_var,
            anchor="center",
            justify="center",
            wraplength=0
        )
        self.formula_label.grid(column=0, row=4, columnspan=2, sticky="nsew", pady=(4, 0))

        self.result_label = ttk.Label(
            frm,
            textvariable=self.result_var,
            anchor="center",
            justify="center",
            font=self.result_font
        )
        self.result_label.grid(column=0, row=5, columnspan=2, sticky="nsew", pady=(6, 0))

        self.bind("<Configure>", self._on_resize)
        self.bind("<Return>", lambda e: self.calculate_or_clear())

        # Initialize output
        self.formula_var.set(" ")
        self.result_var.set(" ")

    def calculate_or_clear(self):
        if self.calc_btn.cget("text") == "CLEAR":
            self.clear()
        else:
            self.calculate()

    def clear(self):
        self.value_var.set("")
        self.percent_var.set("")
        self.formula_var.set(" ")
        self.result_var.set(" ")

        # back to CALCULATE style/color
        self.calc_btn.configure(text="CALCULATE", command=self.calculate_or_clear, style="Calc.TButton")
        self.value_entry.focus_set()

    def calculate(self):
        mode = self.mode_var.get()

        try:
            a = float(self.value_var.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a numeric VALUE.")
            return

        if mode == "part_of":
            try:
                percent = float(self.percent_var.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a numeric PERCENT (%).")
                return

            result = a * (percent / 100)
            self.formula_var.set(f"{a} × ({percent}/100)")
            self.result_var.set(f"Result: {result:.6g}")

        elif mode == "percent_of":
            try:
                b = float(self.percent_var.get())
            except ValueError:
                messagebox.showerror("Invalid input", "Please enter a numeric BASE (B).")
                return

            if b == 0:
                messagebox.showerror("Math error", "BASE (B) cannot be zero.")
                return

            percent = (a / b) * 100
            self.formula_var.set(f"({a}/{b}) × 100")
            self.result_var.set(f"Result: {percent:.6g} %")

        # results shown -> switch to CLEAR and update button color
        self.calc_btn.configure(text="CLEAR", command=self.clear, style="Clear.TButton")

    def _on_resize(self, event):
        new_size = max(8, int(self.winfo_height() / 18))
        if new_size != self.base_size:
            self.base_size = new_size

            self.app_font.configure(size=new_size)
            self.label_font.configure(size=new_size)
            self.entry_font.configure(size=new_size)

            # update ttk styles
            self.style.configure("Calc.TButton", font=self.app_font)
            self.style.configure("Clear.TButton", font=self.app_font)

            self.style.configure("TEntry", font=self.entry_font)
            self.style.configure("TLabel", font=self.label_font)
            self.style.configure("TRadiobutton", font=self.app_font)

            ipady = max(2, new_size // 4)
            self.value_entry.grid_configure(ipady=ipady)
            self.percent_entry.grid_configure(ipady=ipady)

            self.calc_btn.grid_configure(padx=(max(10, new_size * 4), max(10, new_size * 4)))

if __name__ == "__main__":
    PercentApp().mainloop()


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

############### JUST PERCENT CALCULATOR
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
