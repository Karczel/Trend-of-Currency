import tkinter as tk
from tkinter import ttk
from math import *
from data_handling import get_rating


class Page1(tk.Frame):
    def __init__(self,df, **kwargs):
        super().__init__()
        self.df = df
        self.init_components()

    def init_components(self):

        self.frame1 = tk.Frame(self)
        self.display = list(self.df.columns[1:])
        self.choice, self.chooser = self.load_functions(self.frame1,self.display,self.update_currency)

        self.treeview = self.master.create_treeview(self)
        #treeview

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
        self.chooser.bind('<<Combobox>>',self.update_currency)
        self.treeview.bind("<<TreeviewSelect>>", self.change_page)

        #layout
        self.chooser.pack()
        self.frame1.pack()
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def load_functions(self, frame,lst,function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, state='readonly',textvariable=selected, font=('Times New Roman', 25, 'normal'), postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def filter_currency(self,list1,list2):
        return list(filter(lambda x: list1[x] in list2, range(len(list1))))

    def update_currency(self,*args):
        self.master.a_currency = self.choice.get()
        #update treeview
        self.master.update_treeview()

    def change_page(self, event):
        self.master.b_currency = self.treeview.item(self.treeview.selection()[0])['text']
        self.master.p2.update()
        self.master.p2.show()

    def show(self):
        self.lift()