import time
import random
import tkinter as tk
from tkinter import ttk
from threading import Thread




class App(ttk.Frame):


    def __init__(self, parent):
        super().__init__(parent, padding="3 3 12 12")
        self.style = ttk.Style()
        self.style.theme_use("alt")
        parent.rowconfigure(0, weight=1)
        parent.columnconfigure(0, weight=1)
        self.grid(row=0, column=0, sticky="NEWS")
        self.create_widgets()


    def create_widgets(self):
        self.rowconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(0, weight=1)


        # subframe for Task 1
        self.frame1 = ttk.LabelFrame(self, text="Task 1")
        self.frame1.grid(row=0, column=0, sticky="news", padx=5, pady=5)
        self.frame1.rowconfigure(0, weight=1)
        self.frame1.rowconfigure(1, weight=1)
        self.frame1.columnconfigure(0, weight=1)
        self.bar1 = ttk.Progressbar(self.frame1, length=500, mode="determinate")
        self.status1 = ttk.Label(self.frame1, text="Stopped")
        self.start1 = ttk.Button(self.frame1, text="Start",
                                 command=self.run_task1)
        self.bar1.grid(row=0, column=0, sticky="sew", padx=10)
        self.status1.grid(row=1, column=0, sticky="wn", padx=10)
        self.start1.grid(row=0, column=1, rowspan=2, padx=10, pady=10)


        # subframe for Task 2
        self.frame2 = ttk.LabelFrame(self, text="Task 2")
        self.frame2.grid(row=1, column=0, sticky="news", padx=5, pady=5)
        self.frame2.rowconfigure(0, weight=1)
        self.frame2.rowconfigure(1, weight=1)
        self.frame2.columnconfigure(0, weight=1)
        self.bar2 = ttk.Progressbar(self.frame2, length=500, mode="indeterminate")
        self.status2 = ttk.Label(self.frame2, text="Stopped")
        self.start2 = ttk.Button(self.frame2, text="Start",
                                 command=self.run_task2)
        self.bar2.grid(row=0, column=0, sticky="sew", padx=10)
        self.status2.grid(row=1, column=0, sticky="wn", padx=10)
        self.start2.grid(row=0, column=1, rowspan=2, padx=10, pady=10)


        self.quit = ttk.Button(self, text="Quit", command=root.destroy)
        self.quit.grid(row=2, column=0, padx=5, pady=5, sticky="s")


    def run_task1(self):
        print("Running task 1...")
        self.task1()


    def task1(self):
        self.start1.config(state="disabled")  # disable Start button
        self.status1.config(text="Running...")
        self.after(10, lambda: self.task1_step(0))


    def task1_step(self, step):   # simulate determinate long-running task
        time.sleep(0.1)
        self.bar1.config(value=step)
        if step < 100:
            self.after(10, lambda: self.task1_step(step+1))
        else:
            self.task1_done()


    def task1_done(self):
        self.status1.config(text="Done.")
        self.start1.config(state="enabled")  # re-enable Start button


    def run_task2(self):
        print("Running task 2...")
        self.task2_thread = Thread(target=self.task2)
        self.task2_thread.start()
        self.status2.config(text="Running...")
        self.start2.config(state="disabled")
        self.bar2.start()
        self.after(10, self.check_task2)


    def check_task2(self):   # check task 2 regularly whether it has completed
        if self.task2_thread.is_alive():
            self.after(10, self.check_task2)
        else:
            self.status2.config(text="Done.")
            self.start2.config(state="enabled")
            self.bar2.stop()


    def task2(self):   # simulate indeterminate long-running task
        time.sleep(random.randrange(2, 5))


if __name__ == "__main__":
    root = tk.Tk()
    root.title("Long-Running Tasks")
    app = App(root)
    root.mainloop()
