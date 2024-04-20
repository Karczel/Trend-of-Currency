import tkinter as tk
from ui import UI

def main():
    root = tk.Tk()
    app = UI(root)
    app.mainloop()

if __name__ == "__main__":
    main()