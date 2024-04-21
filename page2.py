import tkinter as tk
from tkinter import ttk

class Page2(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__()
        self.init_components()

    def init_components(self):
        self.big_frame = tk.Frame(self)
        #go back button
        self.frame1 = tk.Frame(self.big_frame)
        self.go_back = tk.Button(self.frame1,text="go back")

        #graph space
        self.label1 = tk.Label(self.frame1,text='chart/graph area')

        # exchange
        self.frame2 = tk.Frame(self.big_frame)
        self.a = tk.StringVar()
        self.b = tk.StringVar()

        self.a_label = tk.Label(self.frame2,text='a')
        self.a_field = tk.Entry(self.frame2,textvariable=self.a)
        self.equal_label = tk.Label(self.frame2,text="=")
        self.b_label = tk.Label(self.frame2, text='b')
        self.b_field = tk.Entry(self.frame2,textvariable=self.b)

        #Enter bind
        self.a_field.bind('<Return>', self.convert_handler)
        self.b_field.bind('<Return>', self.convert_handler)

        #treeview
        self.frame3 = tk.Frame(self)
        self.treeview = ttk.Treeview(self.frame3,columns=("size", "lastmod"))
        self.treeview.column("#0",minwidth=100,stretch=0)
        self.treeview.column("size", minwidth=100, stretch=0)
        self.treeview.column("lastmod", minwidth=100, stretch=0)
        self.treeview.heading("#0", text="File")
        self.treeview.heading("size", text="Size")
        self.treeview.heading("lastmod", text="Last modification")
        self.treeview.insert(
            "",
            tk.END,
            text="README.txt",
            values=("850 bytes", "18:30")
        )

        #layout
        padding = {'padx': 10, 'pady': 10}
        self.go_back.pack(side="left")
        self.label1.pack(side="left")
        self.frame1.pack(fill=tk.X,expand=True)
        self.a_label.pack(side="left")
        self.a_field.pack(side="left")
        self.equal_label.pack(side="left")
        self.b_label.pack(side="left")
        self.b_field.pack(side="left")
        self.frame2.pack(fill=tk.X,expand=True)
        self.big_frame.pack(side="left",fill=tk.X,expand=True)
        self.treeview.pack(anchor="w",fill=tk.Y, side="right")
        self.frame3.pack(anchor="w",fill=tk.Y, side="right")

    def load_units(self, function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(self, textvariable=selected, postcommand=function)
        # and select which unit to display
        chooser['values'] = ['a','b','c']
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>', function)
        return selected, chooser

    def convert_handler(self):
        pass

    def show(self):
        self.lift()
