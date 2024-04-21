import tkinter as tk
from page1 import Page1
from page2 import Page2
from data_handling import get_rating

class UI(tk.Tk):
    def __init__(self,df):
        """initialize ui"""
        super().__init__()
        self.df = df
        self.init_components()

    def init_components(self):
        self.wm_geometry("1000x800")

        self.main_frame = tk.Frame(self)
        self.p1 = Page1(self.df)
        self.p2 = Page2(self.df)

        buttonframe = tk.Frame(self)
        container = tk.Frame(self)
        buttonframe.pack(side="top", fill="x", expand=False)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        #from change page by button, change page by elements in each page
        b1 = tk.Button(buttonframe, text="Page 1", command=self.p1.show)
        b2 = tk.Button(buttonframe, text="Page 2", command=self.p2.show)
        b1.pack(side="left")
        b2.pack(side="left")
        self.p1.show()
        self.main_frame.pack()

    def run(self):
        self.mainloop()