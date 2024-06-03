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


    def loading_animation(self, root, task):
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

    def change_page(self, event):
        try:
            self.master.b_currency = self.treeview.item(self.treeview.selection()[0])['text']
            self.master.p2.small_update()
            self.master.p2.show()
        except IndexError:
            pass

    def show(self):
        self.lift()
