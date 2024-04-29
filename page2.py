from PIL import Image
import tkinter as tk
from tkinter import ttk
import customtkinter
from data_handling import *
from chart import *
from graph import *


class Page2(tk.Frame):
    def __init__(self, df, **kwargs):
        super().__init__()
        self.df = self.master.df
        self.rating = self.master.rating
        self.init_components()

    def init_components(self):
        # go_back button image
        self.img = Image.open("asset/arrow_left.png")
        new_size = 50

        self.resized_image = self.img.resize((new_size, new_size))
        self.imgtk = customtkinter.CTkImage(self.resized_image)

        self.big_frame = tk.Frame(self)
        # go back button
        self.frame1 = tk.Frame(self.big_frame)
        self.go_back = customtkinter.CTkButton(self.frame1, image=self.imgtk, text='', width=30, height=30,
                                               compound=customtkinter.LEFT, command=self.go_back)
        # graph space
        self.canvas, self.fig = similarity_bar_graph(self.rating, self.frame1)
        self.canvas_choice = {'bar graph': similarity_bar_graph,
                              'line graph': exchange_rate_line_graph,
                              'Histogram': compare_histogram,
                              'Corr. Heatmap': similarity_heatmap,
                              'Node Graph': draw_graph}
        # *node to be replaced
        self.frame2 = tk.Frame(self.big_frame)
        # choose graph
        self.display = ['bar graph', 'line graph', 'Histogram', 'Corr. Heatmap', 'Node Graph']

        self.frame1_1 = tk.Frame(self.big_frame)

        self.choice, self.chooser = self.load_functions(self.frame1_1, self.display, self.update_currency)
        # choose c currency
        self.c_lst = list(self.df.columns[1:])
        self.c_lst.remove(self.master.a_currency)
        self.c_lst.remove(self.master.b_currency)
        self.c_choice,self.c_chooser = self.load_functions(self.frame1_1,self.c_lst,self.update_currency)

        # exchange
        self.a = tk.StringVar()
        self.b = tk.StringVar()

        self.a_label = tk.Label(self.frame2, text=self.master.a_currency)
        self.a_field = tk.Entry(self.frame2, textvariable=self.a)
        self.equal_label = tk.Label(self.frame2, text="=")
        self.b_label = tk.Label(self.frame2, text=self.master.b_currency)
        self.output = tk.Label(self.frame2, text="Enter value")

        # Enter bind
        self.a_field.bind('<Return>', self.convert_handler)

        # treeview
        self.treeview = self.master.create_treeview(self)

        self.treeview.bind("<<TreeviewSelect>>", self.update_currency)

        self.grid_func()

    def load_functions(self, frame, lst, function):
        """Load units of the requested unittype into the comboboxes."""
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, state='readonly', textvariable=selected, font=('Times New Roman', 25, 'normal'),
                               postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>', function)
        return selected, chooser

    def small_update(self):
        self.a_label.config(text=self.master.a_currency)
        self.b_label.config(text=self.master.b_currency)
        self.c_lst = list(self.df.columns[1:])
        self.c_lst.remove(self.master.a_currency)
        self.c_lst.remove(self.master.b_currency)
        self.c_chooser['values'] = self.c_lst
        self.update_image()

    def update(self):
        self.small_update()
        self.master.update_treeview(self.treeview)

    def convert_handler(self, *args):
        exchange_rate = self.master.last_row[self.master.b_currency] / self.master.last_row[self.master.a_currency]
        try:
            self.b.set(float(self.a.get()) * exchange_rate)
            self.output.config(text="{:.3f}".format(float(self.b.get())), fg='black')
        except ValueError:
            if self.a_field.get() == "":
                self.output.config(text="Enter value", fg='black')
            else:
                self.output.config(text="ERROR", fg='red')
        self.small_update()

    def update_currency(self, *args):
        try:
            self.master.b_currency = self.treeview.item(self.treeview.selection()[0])['text']
        except IndexError:
            pass
        self.convert_handler()

    def update_image(self):
        self.canvas.get_tk_widget().grid_remove()
        if self.choice.get() in ['bar graph', 'Corr. Heatmap']:
            self.canvas, self.fig = self.canvas_choice[self.choice.get()](self.rating, self.frame1)
        if self.choice.get() in ['line graph', 'Histogram']:
            self.canvas, self.fig = self.canvas_choice[self.choice.get()](self.df, self.master.b_currency,
                                                                          self.c_choice.get(), self.frame1)
        if self.choice.get() == 'Node Graph':
            self.canvas, self.fig = self.canvas_choice[self.choice.get()](
                draw_edge(self.rating.mode(), self.master.a_currency), self.master.a_currency, self.frame1)
        self.canvas.get_tk_widget().grid()

    def grid_func(self):
        # frame 1
        for i in range(3):
            self.frame1.rowconfigure(i, weight=1)
        for j in range(3):
            self.frame1.columnconfigure(i, weight=1)

        # frame2
        for i in range(3):
            self.frame2.rowconfigure(i, weight=1)
        for j in range(3):
            self.frame2.columnconfigure(i, weight=1)

        # bigframe
        for i in range(3):
            self.big_frame.rowconfigure(i, weight=1)
        for j in range(3):
            self.big_frame.columnconfigure(i, weight=1)

        # self
        for i in range(3):
            self.rowconfigure(i, weight=1)
        for j in range(3):
            self.columnconfigure(i, weight=1)

        # layout
        padding = {'padx': 10, 'pady': 10}
        self.go_back.grid(row=0, column=0, sticky="nw", **padding)
        self.canvas.get_tk_widget().grid(row=0, column=1, **padding)
        self.frame1.grid(row=0, column=0, sticky="ew", **padding)
        self.frame1_1.grid(row=1, column=0, sticky="w", **padding)
        self.chooser.grid(row=0, column=0, sticky="w", **padding)
        self.c_chooser.grid(row=0, column=1, sticky="w", **padding)
        self.a_field.grid(row=0, column=1, sticky="w", **padding)
        self.a_label.grid(row=0, column=2, sticky="w", **padding)
        self.equal_label.grid(row=1, column=0, sticky="w", **padding)
        self.output.grid(row=1, column=1, sticky="w", **padding)
        self.b_label.grid(row=1, column=2, sticky="w", **padding)
        self.frame2.grid(row=2, column=0, sticky="ew", **padding)
        self.big_frame.grid(row=0, column=0, sticky="ew", **padding)
        self.treeview.grid(row=0, column=1, sticky="nsew")

    def go_back(self):
        self.master.p1.show()

    def show(self):
        self.lift()
