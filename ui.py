import tkinter as tk
from tkinter import ttk

from threading import Thread

from data_handling import *
from page1 import Page1
from page2 import Page2


class UI(tk.Tk):
    def __init__(self, df):
        """initialize ui"""
        super().__init__()
        self.df = df
        self.init_components()

    def init_components(self):
        self.wm_geometry("1500x800")

        self.main_frame = tk.Frame(self)
        #lift loading screen and run animation in thread
        # self.loading_screen(self, self.loading)
        self.loading()
        self.after_load()
        self.pack_func()

    def pack_func(self):
        self.container.pack(side="top", fill="both", expand=True)

        self.p1.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)
        self.p2.place(in_=self.container, x=0, y=0, relwidth=1, relheight=1)

        self.p1.show()
        self.main_frame.pack()

    def is_positive(self, number):
        if number > 0:
            return "> (increase)"
        else:
            return "< (decrease)"

    def create_treeview(self, root):
        treeview = ttk.Treeview(root, columns=("exchange rate", "future", "rating"))
        treeview.column("#0", minwidth=100, anchor="center")
        treeview.column("exchange rate", minwidth=100, anchor="center")
        treeview.column("future", minwidth=100, anchor="center")
        treeview.column("rating", minwidth=100, anchor="center")
        treeview.heading("#0", text="Currency")
        treeview.heading("exchange rate", text="Exchange Rate")
        treeview.heading("future", text="Future")
        treeview.heading("rating", text="Rating")
        self.insert_treeview(treeview)
        return treeview

    def insert_treeview(self, treeview):
        for i in self.df.columns[1:]:
            if i != self.a_currency:
                treeview.insert(
                    "",
                    tk.END,
                    text=i,
                    values=(
                    "{:.3f}".format(self.last_row[i]), self.is_positive(self.future[i]), self.rating.mode().at[0, i])
                )

    def update_treeview(self, treeview):
        if len(treeview.get_children()) > 0:
            for child in treeview.get_children():
                treeview.delete(child)
        # replacement_last_row = self.last_row.div(self.last_row[self.a_currency], axis=0)
        # self.last_row = replacement_last_row
        self.df.iloc[:, 1:] = self.df.iloc[:, 1:].div(self.df[self.a_currency], axis=0)
        self.last_row = self.df[self.df.columns[1:]].iloc[-1]
        self.rating = get_rating(self.a_currency, self.df)
        self.insert_treeview(treeview)

    def loading(self):
        self.a_currency = self.df.columns[1]
        self.b_currency = self.df.columns[2]
        self.last_row = self.df[self.df.columns[1:]].iloc[-1]
        self.future = get_trend(self.a_currency, self.df[self.df["Time Serie"] >= pd.to_datetime("2016")]).mean(axis=0)
        self.rating = get_rating(self.a_currency, self.df)

    def loading_screen(self, root, task):
        # make new thread for loading part
        self.loading_thread = Thread(target=task)
        self.loading_thread.start()

        # make loading screen
        root.bar = ttk.Progressbar(root, length=500, mode="indeterminate")
        root.bar.pack(fill="none", expand=True)
        # run loading screen
        root.bar.start()

        # check if ui finished loading (thread is dead)
        root.after(10, root.check_loading)

    def check_loading(self):
        if self.loading_thread.is_alive():
            self.after(10, self.check_loading())
        else:
            self.bar.stop()
            # clear loading screen (destroy)
            for i in self.pack_slaves():
                i.destroy()
            self.loading_thread.join()

            # matplotlib gui outside main thread fail
            self.after_load()

            # re-pack
            try:
                self.pack_func()
            except AttributeError:
                pass

    def after_load(self):
        # pages
        self.p1 = Page1()
        self.p2 = Page2()

        # Page 1 :combobox selected is a, treeview click is b
        # Page 2: a is fixed, treeview click is b

        self.container = tk.Frame(self)

    def run(self):
        self.mainloop()
