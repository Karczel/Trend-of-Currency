import tkinter as tk
from tkinter import ttk
from math import *
from data_handling import get_rating


class Page1(tk.Frame):
    def __init__(self,df, **kwargs):
        super().__init__()
        self.df = df
        self.rating = get_rating('US$', self.df)
        self.init_components()

    def init_components(self):
        self.last_row = self.df.iloc[-1]

        self.a_currency = self.master.a_currency
        self.b_currency = self.master.b_currency

        self.frame1 = tk.Frame(self)
        self.display = list(self.df.columns[1:])
        self.choice, self.chooser = self.load_functions(self.frame1,self.display,self.update_currency)

        #treeview
        self.treeview = ttk.Treeview(self,columns=("exchange rate", "future","rating"))
        self.treeview.column("#0",minwidth=100,anchor="center")
        self.treeview.column("exchange rate", minwidth=100, anchor="center")
        self.treeview.column("future", minwidth=100, anchor="center")
        self.treeview.column("rating", minwidth=100,anchor="center")
        self.treeview.heading("#0", text="Currency")
        self.treeview.heading("exchange rate", text="Exchange Rate")
        self.treeview.heading("future", text="Future")
        self.treeview.heading("rating", text="Rating")

        for i in self.df.columns[1:]:
            if i != self.master.a_currency:
                self.treeview.insert(
                    "",
                    tk.END,
                    text=i,
                    values=(self.last_row[i], "18:30", self.rating.mode().at[0, i])
                )

        # self.treeview.insert(
        #     "",
        #     tk.END,
        #     text=column,
        #     values=(exchange rate, future ,rating)
        # )
        # exchange rate from df
        # future from whether trend in last year (2019) is positive or negative
        # by average get_trend(column_name, df) in year 2019
        # rating from rating of similarity

        # bind
        self.treeview.bind("<<TreeviewSelect>>", self.change_page)

        #layout
        self.chooser.pack()
        self.frame1.pack()
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def load_functions(self, frame,lst,function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, textvariable=selected, font=('Times New Roman', 25, 'normal'), postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def filter_currency(self,list1,list2):
        return list(filter(lambda x: list1[x] in list2, range(len(list1))))

    def update_currency(self,*args):
        self.a_currency = self.choice.get()

    def change_page(self, event):
        self.master.b_currency = self.treeview.selection()[0]
        self.master.p2.show()

    def show(self):
        self.lift()