"""
This module imports the tkinter and ttk modules for creating a graphical user interface.
"""
import tkinter as tk

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Parcial 3 Fisica 3")
        self.master.geometry("1000x1000")
        tk.Label(text = "Selecciona el número de electrodomésticos que vas a conectar").pack()
        self.electrodmoesticos = []
        self.Num_electrodomesticos = tk.StringVar()
        tk.OptionMenu(self.master,self.Num_electrodomesticos, "1", "2", "3", "4", "5", "6", "7", "8", "9", "10").pack()
        tk.Button(self.master, text = "Aceptar", command = self.aceptar).pack()
    
    def aceptar(self):
        self.master.destroy()
        Window2(self.Num_electrodomesticos.get())


class Window2:
    
    def __init__(self, number):
        number = int(number)
        self.master = tk.Tk()
        for i in range(number):
            pass
        print(number)


if __name__ == "__main__":
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

    






