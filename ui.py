import tkinter as tk
from tkinter import ttk
from data_handling import*
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
        self.a_currency = 'US$'
        self.b_currency = 'US$'
        self.last_row = self.df.iloc[-1]
        self.rating = get_rating('US$', self.df)

        #make treeview
        self.create_treeview()

        #pages
        self.p1 = Page1(self.df)
        self.p2 = Page2(self.df)

        # Page 1 :combobox selected is a, treeview click is b
        # Page 2: a is fixed, treeview click is b

        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=container, x=0, y=0, relwidth=1, relheight=1)

        self.p1.show()
        self.main_frame.pack()

    def create_treeview(self,root):
        self.treeview = ttk.Treeview(root, columns=("exchange rate", "future", "rating"))
        self.treeview.column("#0", minwidth=100, anchor="center")
        self.treeview.column("exchange rate", minwidth=100, anchor="center")
        self.treeview.column("future", minwidth=100, anchor="center")
        self.treeview.column("rating", minwidth=100, anchor="center")
        self.treeview.heading("#0", text="Currency")
        self.treeview.heading("exchange rate", text="Exchange Rate")
        self.treeview.heading("future", text="Future")
        self.treeview.heading("rating", text="Rating")
        self.insert_treeview()

    def insert_treeview(self):
        for i in self.df.columns[1:]:
            if i != self.a_currency:
                self.treeview.insert(
                    "",
                    tk.END,
                    text=i,
                    values=(self.last_row[i], "18:30", self.rating.mode().at[0, i])
                )

    def update_treeview(self):
        if len(self.treeview.get_children()) > 0:
            for child in self.treeview.get_children():
                self.treeview.delete(child)
                self.last_row[1:] = self.last_row[1:].div(self.last_row[self.a_currency])
        self.rating = get_rating(self.a_currency,self.df)
        self.insert_treeview()

    def loading(self):
        pass


    def run(self):
        self.mainloop()