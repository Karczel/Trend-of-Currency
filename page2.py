import tkinter as tk


class Page2(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__()
        self.init_components()

    def init_components(self):
        self.label = tk.Label(self, text='page2')
        self.label.pack()

    def show(self):
        self.lift()
