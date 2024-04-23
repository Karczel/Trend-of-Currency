import tkinter as tk
from tkinter import ttk
from data_handling import*


class Page2(tk.Frame):
    def __init__(self, df, **kwargs):
        super().__init__()
        self.df = df
        self.rating = get_rating('US$', self.df)
        self.init_components()

    def init_components(self):
        # get last row
        self.big_frame = tk.Frame(self)
        # go back button
        self.frame1 = tk.Frame(self.big_frame)
        self.go_back = tk.Button(self.frame1, text="go back", command=self.go_back)

        # graph space
        self.label1 = tk.Label(self.frame1, text='chart/graph area')
        #choose graph
        self.display = ['bar graph', 'line graph', 'Histogram', 'Corr. Heatmap', 'Node Graph']
        self.choice, self.chooser = self.load_functions(self.frame1, self.display, self.update_currency)

        # exchange
        self.frame2 = tk.Frame(self.big_frame)
        self.a = tk.StringVar()
        self.b = tk.StringVar()

        self.a_label = tk.Label(self.frame2, text=self.master.a_currency)
        self.a_field = tk.Entry(self.frame2, textvariable=self.a)
        self.equal_label = tk.Label(self.frame2, text="=")
        self.b_label = tk.Label(self.frame2, text=self.master.b_currency)
        self.output = tk.Label(self.frame2, text="Enter value")

        # Enter bind
        self.a_field.bind('<Return>', self.convert_handler)

        # lst for different graphs
        self.lst = []

        # treeview
        self.frame3 = tk.Frame(self)
        self.treeview = self.master.create_treeview(self)

        # get df[last] for exchange rate,
        # currency - > column
        # exchange rate other currency =
        # us -> other
        # 1 us = other_rate other
        # other1->other2
        # 1 other1 = other2_rate/other1_rate other2
        # future -> from year: up or down, represent with arrow
        # rating -> from get_rating

        # future = get_trend()
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

        self.treeview.bind("<<TreeviewSelect>>", self.update_currency)

        # layout
        padding = {'padx': 10, 'pady': 10}
        self.go_back.pack(side="left")
        self.label1.pack(side="left")
        self.chooser.pack()
        self.frame1.pack(fill=tk.X, expand=True)
        self.a_field.pack(side="left")
        self.a_label.pack(side="left")
        self.equal_label.pack(side="left")
        self.output.pack(side="left")
        self.b_label.pack(side="left")
        self.frame2.pack(fill=tk.X, expand=True)
        self.big_frame.pack(side="left", fill=tk.X, expand=True)
        self.treeview.pack(anchor="w", fill=tk.Y, side="right")
        self.frame3.pack(anchor="w", fill=tk.Y, side="right")

    def load_functions(self, frame, lst,function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, state='readonly',textvariable=selected, font=('Times New Roman', 25, 'normal'),
                               postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>')
        return selected, chooser

    def small_update(self):
        self.a_label.config(text=self.master.a_currency)
        self.b_label.config(text=self.master.b_currency)
        self.update_image()

    def update(self):
        self.small_update()
        self.master.update_treeview(self.treeview)

    def convert_handler(self, *args):
        self.small_update()
        exchange_rate = self.master.last_row[self.master.b_currency] / self.master.last_row[self.master.a_currency]
        self.b.set(float(self.a.get()) * exchange_rate)
        self.output.config(text="{:.3f}".format(self.b.get()))

    def update_currency(self, *args):
        self.master.b_currency = self.treeview.item(self.treeview.selection()[0])['text']
        self.small_update()
        exchange_rate = self.master.last_row[self.master.b_currency] / self.master.last_row[self.master.a_currency]
        try:
            self.b.set(float(self.a.get()) * exchange_rate)
            self.output.config(text=self.b.get())
        except ValueError:
            pass

    def update_image(self, *args):
        # update chart/graph
        pass

    def go_back(self):
        self.master.p1.show()

    def show(self):
        self.lift()
