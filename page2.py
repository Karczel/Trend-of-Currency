import tkinter as tk
from tkinter import ttk
from data_handling import get_rating

class Page2(tk.Frame):
    def __init__(self,df, **kwargs):
        super().__init__()
        self.df = df
        self.rating = get_rating('US$', self.df)
        self.init_components()

    def init_components(self):
        self.big_frame = tk.Frame(self)
        #go back button
        self.frame1 = tk.Frame(self.big_frame)
        self.go_back = tk.Button(self.frame1,text="go back",command=self.go_back)

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
        self.output = tk.Label(self.frame2, text="Enter value")

        #Enter bind
        self.a_field.bind('<Return>', self.convert_handler)

        #treeview
        self.frame3 = tk.Frame(self)
        self.treeview = ttk.Treeview(self.frame3,columns=("exchange rate", "future","rating"))
        self.treeview.column("#0",minwidth=1,stretch=0,anchor="center")
        self.treeview.column("exchange rate", minwidth=1, stretch=0,anchor="center")
        self.treeview.column("future", minwidth=1, stretch=0,anchor="center")
        self.treeview.column("rating", minwidth=1, stretch=0,anchor="center")
        self.treeview.heading("#0", text="Currency")
        self.treeview.heading("exchange rate", text="Exchange Rate")
        self.treeview.heading("future", text="Future")
        self.treeview.heading("rating", text="Rating")

        #get df[last] for exchange rate,
        #currency - > column
        #exchange rate other currency =
        #us -> other
        #1 us = other_rate other
        # other1->other2
        # 1 other1 = other2_rate/other1_rate other2
        #future -> from year: up or down, represent with arrow
        #rating -> from get_rating

        for i in self.df.columns[1:]:
            self.treeview.insert(
                "",
                tk.END,
                text=i,
                values=(self.df[i].iat[-1], "18:30", self.rating.mode().at[0, i])
            )
        # self.treeview.insert(
        #     "",
        #     tk.END,
        #     text=column,
        #     values=(exchange rate, future ,rating)
        # )
        # exchange rate from df
        # future from whether trend in last year (2019) is positive or negative
        #by average get_trend(column_name, df) in year 2019
        # rating from rating of similarity

        self.treeview.bind("<1>", self.update_currency())

        #layout
        padding = {'padx': 10, 'pady': 10}
        self.go_back.pack(side="left")
        self.label1.pack(side="left")
        self.frame1.pack(fill=tk.X,expand=True)
        self.a_field.pack(side="left")
        self.a_label.pack(side="left")
        self.equal_label.pack(side="left")
        self.output.pack(side="left")
        self.b_label.pack(side="left")
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

    def convert_handler(self, *args):
        self.b.set(float(self.a.get())*2)
        # 2 = exchange rate from a -> b
        self.output.config(text=self.b.get())

    def update_currency(self, *args):
        # get index of list in string list, then change var to that index
        #list 1 would be ['a','b','c'] while list 2 reference columns in [a,b,c], ordered by index
        self.update_image()
        pass

    def update_image(self, *args):
        #update chart/graph
        pass

    def go_back(self):
        self.master.p1.show()

    def change_page(self, *args):
        pass

    def show(self):
        self.lift()
