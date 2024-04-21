import tkinter as tk
from tkinter import ttk
from math import *


class Page1(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__()
        self.init_components()

    def init_components(self):
        self.frame1 = tk.Frame(self)
        self.currency_list = ["a","b","c"]
        self.choice, self.chooser = self.load_functions(self.currency_list,self.frame1,self.do_nothing)
        self.e_list = [i for i in enumerate(self.currency_list)]

        #normal treeview
        self.treeview = ttk.Treeview(self,columns=("size", "lastmod"))
        self.treeview.heading("#0", text="File")
        self.treeview.heading("size", text="Size")
        self.treeview.heading("lastmod", text="Last modification")
        self.treeview.insert(
            "",
            tk.END,
            text="README.txt",
            values=("850 bytes", "18:30")
        )
        #linked tree view

        #layout
        self.chooser.pack()
        self.frame1.pack()
        self.treeview.pack(fill=tk.X, expand=True)

    def load_functions(self, lst, frame,function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, textvariable=selected, font=('Times New Roman', 25, 'normal'), postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def do_nothing(self):
        pass

    def filter_currency(self,list1,list2):
        return list(filter(lambda x: list1[x] in list2, range(len(list1))))

    def update_currency(self):
        # get index of list in string list, then change var to that index
        #list 1 would be ['a','b','c'] while list 2 reference columns in [a,b,c], ordered by index
        pass

    def show(self):
        self.lift()