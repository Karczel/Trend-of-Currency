import tkinter as tk
from page1 import Page1
from page2 import Page2


class UI(tk.Tk):
    def __init__(self,df):
        """initialize ui"""
        super().__init__()
        self.df = df
        # self.loading()
        self.init_components()

    def init_components(self):
        self.wm_geometry("1500x800")

        self.main_frame = tk.Frame(self)
        self.p1 = Page1(self.df)
        self.p2 = Page2(self.df)

        self.a_currency = None
        self.b_currency = None
        # Page 1 :combobox selected is a, treeview click is b
        # Page 2: a is fixed, treeview click is b

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.p1.show()
        self.main_frame.pack()

    def loading(self):
        pass

    def run(self):
        self.mainloop()