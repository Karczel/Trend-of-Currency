import threading
import tkinter as tk
from tkinter import ttk
from threading import Thread


class LoadingScreen(tk.Frame):
    def __init__(self, parent,**kwargs):
        super().__init__(parent,**kwargs)
        self.status = threading.Event()
        self.init_components()

    def init_components(self):
        # progress bar
        self.bar = ttk.Progressbar(self, length=500, mode="indeterminate")

        # layout
        self.bar.pack(fill="none", expand=True)

    def loading_animation(self):
        # check if ui finished loading (var is changed)
        if self.status.is_set():
            self.bar.stop()
            self.loading_thread.join()
        # else:
        #     self.master.after(10,self.loading_animation)

    def start_load(self):
        # run loading screen
        self.status.clear()
        self.bar.start()
        self.show()
        self.loading_thread = Thread(target=self.loading_animation)
        self.loading_thread.start()

    def show(self):
        self.lift()
