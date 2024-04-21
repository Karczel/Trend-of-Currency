import tkinter as tk
from page1 import Page_1
from page2 import Page_2

class UI(tk.Tk):
    def __init__(self):
        """initialize ui"""
        super().__init__()
        self.init_components()

    def init_components(self):
        self.main_frame = self.Frame()

    def run(self):
        self.mainloop()