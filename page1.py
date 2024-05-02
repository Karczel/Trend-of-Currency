import tkinter as tk
from tkinter import ttk


class Page1(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__()
        self.init_components()

    def init_components(self):

        self.frame1 = tk.Frame(self)
        self.display = list(self.master.df.columns[1:])
        self.choice, self.chooser = self.load_functions(self.frame1, self.display, self.update_currency)

        self.treeview = self.master.create_treeview(self)

        # bind
        self.treeview.bind("<<TreeviewSelect>>", self.change_page)

        # layout
        self.chooser.pack()

        self.frame1.pack()
        self.treeview.pack(fill=tk.BOTH, expand=True)

    def load_functions(self, frame, lst, function):
        """Load units of the requested unittype into the comboboxes."""
        # completed loading function
        selected = tk.StringVar()
        # put the unit names (strings) in the comboboxes
        chooser = ttk.Combobox(frame, state='readonly', textvariable=selected, font=('Times New Roman', 25, 'normal'),
                               postcommand=function)
        # and select which unit to display
        chooser['values'] = lst
        chooser.current(newindex=0)
        chooser.bind('<<ComboboxSelected>>', function)
        return selected, chooser

    def filter_currency(self, list1, list2):
        return list(filter(lambda x: list1[x] in list2, range(len(list1))))

    def update_currency(self, *args):
        # update treeview only when different from prev
        if self.choice.get() != self.master.a_currency:
            self.master.a_currency = self.choice.get()
            self.master.update_treeview(self.treeview)
            self.master.p2.update()

    def change_page(self, event):
        try:
            self.master.b_currency = self.treeview.item(self.treeview.selection()[0])['text']
            self.master.p2.small_update()
            self.master.p2.show()
        except IndexError:
            pass

    def show(self):
        self.lift()
