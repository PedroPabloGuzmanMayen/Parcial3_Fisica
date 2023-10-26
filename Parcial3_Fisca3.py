"""
This module imports the tkinter and ttk modules for creating a graphical user interface.
"""
import tkinter as tk

class Interface:
    def __init__(self, master):
        self.master = master
        self.master.title("Parcial 3 Fisica 3")
        self.master.geometry("1000x1000")
        



if __name__ == "__main__":
    root = tk.Tk()
    app = Interface(root)
    root.mainloop()