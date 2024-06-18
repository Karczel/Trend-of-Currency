import tkinter as tk
from tkinter import ttk


class LoadingScreen(tk.Frame):
    def __init__(self, **kwargs):
        super().__init__()
        self.init_components()

    def init_components(self):
        pass

        # bind


        # layout


    def loading_animation(self):
        # make loading screen
        self.master.bar = ttk.Progressbar(self.master, length=500, mode="indeterminate")
        self.master.bar.pack(fill="none", expand=True)
        # run loading screen
        self.master.bar.start()

        # check if ui finished loading (thread is dead)
        self.master.after(10, self.master.check_loading)

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

    def show(self):
        self.lift()
