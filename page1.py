import tkinter as tk
from tkinter import ttk
from math import *


class Page1:
    def __init__(self):
        super().__init__()
        self.init_components()

    def init_components(self):
        self.frame1 = tk.Frame(self)
        self.choice, self.chooser = self.load_functions(["a","b","c"],self.frame1,self.do_nothing)

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

    def update_currency(self):
        # get index of list in string list, then change var to that index
    