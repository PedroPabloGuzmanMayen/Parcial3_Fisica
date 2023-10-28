

import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from mpl_interactions import ioff, panhandler, zoom_factory
import matplotlib.patches as patches
import numpy as np
import math

class Window1:
    def __init__(self, master):
        self.master = master
        self.master.title("Parcial 3 Fisica 3")
        self.master.geometry("1000x1000")
        self.lavadora = tk.StringVar(value = "0") #1
        self.refrigeradora = tk.StringVar(value = "0") #2
        self.estufa = tk.StringVar(value = "0") #3
        self.televisor = tk.StringVar(value = "0") #4
        self.computadora = tk.StringVar(value = "0") #5
        self.lampara = tk.StringVar(value = "0") #6
        self.secadora = tk.StringVar(value = "0") #7
        self.microondas = tk.StringVar(value = "0") #8
        self.cafetera = tk.StringVar(value = "0") #9
        self.tostadora = tk.StringVar(value = "0") #10
        self.ventilador = tk.StringVar(value = "0") #11
        self.aspiradora = tk.StringVar(value = "0") #12
        self.plancha = tk.StringVar(value = "0") #13
        self.batidora = tk.StringVar(value = "0") #14
        self.radio = tk.StringVar(value = "0") #15
        self.consola = tk.StringVar(value = "0") #16
        self.calentador = tk.StringVar(value = "0") #17
        self.cocina = tk.StringVar(value = "0") #18
        self.licuadora = tk.StringVar(value = "0") #19
        self.horno = tk.StringVar(value = "0") #20
        tk.Label(text = "Selecciona los electrodomésticos que vas a concectar").pack()
        tk.Checkbutton(text = "Lavadora", variable = self.lavadora, onvalue = "Lavadora", offvalue = "0").pack()
        tk.Checkbutton(text = "Refrigeradora", variable = self.refrigeradora, onvalue = "Refrigeradora", offvalue = "0").pack()
        tk.Checkbutton(text = "Estufa", variable = self.estufa, onvalue = "Estufa", offvalue = "0").pack()
        tk.Checkbutton(text = "Televisor", variable = self.televisor, onvalue = "Televisor", offvalue = "0").pack()
        tk.Checkbutton(text = "Computadora", variable = self.computadora, onvalue = "Computadora", offvalue = "0").pack()
        tk.Checkbutton(text = "Lampara", variable = self.lampara, onvalue = "Lampara", offvalue = "0").pack()
        tk.Checkbutton(text = "Secadora", variable = self.secadora, onvalue = "Secadora", offvalue = "0").pack()
        tk.Checkbutton(text = "Microondas", variable = self.microondas, onvalue = "Microondas", offvalue = "0").pack()
        tk.Checkbutton(text = "Cafetera", variable = self.cafetera, onvalue = "Cafetera", offvalue = "0").pack()
        tk.Checkbutton(text = "Tostadora", variable = self.tostadora, onvalue = "Tostadora", offvalue = "0").pack()
        tk.Checkbutton(text = "Ventilador", variable = self.ventilador, onvalue = "Ventilador", offvalue = "0").pack()
        tk.Checkbutton(text = "Aspiradora", variable = self.aspiradora, onvalue = "Aspiradora", offvalue = "0").pack()
        tk.Checkbutton(text = "Plancha", variable = self.plancha, onvalue = "Plancha", offvalue = "0").pack()
        tk.Checkbutton(text = "Batidora", variable = self.batidora, onvalue = "Batidora", offvalue = "0").pack()
        tk.Checkbutton(text = "Radio", variable = self.radio, onvalue = "Radio", offvalue = "0").pack()
        tk.Checkbutton(text = "Consola", variable = self.consola, onvalue = "Consola", offvalue = "0").pack()
        tk.Checkbutton(text = "Calentador", variable = self.calentador, onvalue = "Calentador", offvalue = "0").pack()
        tk.Checkbutton(text = "Freidora", variable = self.cocina, onvalue = "Freidora", offvalue = "0").pack()
        tk.Checkbutton(text = "Licuadora", variable = self.licuadora, onvalue = "Licuadora", offvalue = "0").pack()
        tk.Checkbutton(text = "Horno", variable = self.horno, onvalue = "Horno", offvalue = "0").pack()
        tk.Label(text= "Selecciona el largo del cable (en metros)").pack()
        self.lenght = tk.Entry()
        self.lenght.pack()



        tk.Button(text = "Siguiente", command = self.next).pack()

    def next(self):
        self.list = []
        self.list.append(self.lavadora.get())
        self.list.append(self.refrigeradora.get())
        self.list.append(self.estufa.get())
        self.list.append(self.televisor.get())
        self.list.append(self.computadora.get())
        self.list.append(self.lampara.get())
        self.list.append(self.secadora.get())
        self.list.append(self.microondas.get())
        self.list.append(self.cafetera.get())
        self.list.append(self.tostadora.get())
        self.list.append(self.ventilador.get())
        self.list.append(self.aspiradora.get())
        self.list.append(self.plancha.get())
        self.list.append(self.batidora.get())
        self.list.append(self.radio.get())
        self.list.append(self.consola.get())
        self.list.append(self.calentador.get())
        self.list.append(self.cocina.get())
        self.list.append(self.licuadora.get())
        self.electrodomesticos = list(filter(lambda x: x != "0", self.list))

        if (len(self.electrodomesticos) == 0 or len(self.electrodomesticos) > 10):
            tk.messagebox.showerror("Error", "Selecciona entre 1 y 10 electrodomésticos")
        elif (self.lenght.get() == "" or self.lenght.get().isdigit() == False or self.lenght.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa un largo válido")
        else:
            self.final_lenght = self.lenght.get()
            self.potencias = []
            self.voltajes = []
            self.corrientes = []
            self.horas = []
            self.master.destroy()
            Window2(self.electrodomesticos, self.final_lenght, self.electrodomesticos[0], 0, self.voltajes, self.corrientes, self.potencias, self.horas)





class Window2:
    def __init__(self, list, lenght, name, index, voltajes, corrientes, potencias, horas):
        self.Corrientes = corrientes
        self.Voltajes = voltajes
        self.Potencias = potencias
        self.Horas = horas
        self.index = index
        self.list = list
        self.lenght = lenght
        self.name = name
        self.master = tk.Tk()
        self.master.title("Selección de datos")
        self.master.geometry("1000x1000")
        tk.Label(text = "Selecciona los datos de este electrodoméstico: " + self.name).pack()
        tk.Label(text = "Voltaje (voltios)").pack()
        self.Voltaje = tk.Entry()
        self.Voltaje.pack()
        tk.Label(text = "Corriente (amperios)").pack()
        self.Corriente = tk.Entry()
        self.Corriente.pack()
        tk.Label(text = "Potencia (watts)").pack()
        self.Potencia = tk.Entry()
        self.Potencia.pack()
        tk.Label(text = "Horas de uso").pack()
        self.horas = tk.Entry()
        self.horas.pack()
        tk.Button(text = "Siguiente", command= self.next).pack()
        self.master.mainloop()

    def next(self):
        pass
        if (self.Voltaje.get() == "" or self.Voltaje.get().isdigit() == False or self.Voltaje.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa un voltaje válido")
        elif (self.Corriente.get() == "" or self.Corriente.get().isdigit() == False or self.Corriente.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa una corriente válida")
        elif (self.Potencia.get() == "" or self.Potencia.get().isdigit() == False or self.Potencia.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa una potencia válida")
        elif (self.horas.get() == "" or self.horas.get().isdigit() == False or self.horas.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa una cantidad de horas válida")
        elif(float(self.Corriente.get())*float(self.Voltaje.get()) != float(self.Potencia.get())):
            tk.messagebox.showerror("Error", "La potencia no coincide con el voltaje y la corriente")
        else:
            self.Corrientes.append(float(self.Corriente.get()))
            self.Voltajes.append(float(self.Voltaje.get()))
            self.Potencias.append(float(self.Potencia.get()))
            self.Horas.append(float(self.horas.get()))

            if (self.index < (len(self.list)-1)):
                self.index += 1
                self.name = self.list[self.index]
                self.master.destroy()
                Window2(self.list, self.lenght, self.name, self.index, self.Voltajes, self.Corrientes, self.Potencias, self.Horas)
            else:
                self.master.destroy()
                Window3(self.list, self.lenght, self.Voltajes, self.Corrientes, self.Potencias, self.Horas)

class Window3:
    def __init__(self, list, lenght, voltajes, corrientes, potencias, horas):
  
        self.list = list
        self.lenght = lenght
        self.master = tk.Tk()
        self.master.title("Resultados")
        self.master.geometry("1000x1000")
        self.fig = Figure(figsize=(10, 4), dpi=100)
        self.ax = self.fig.add_subplot()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.get_tk_widget().pack()
        zoom_factory(self.ax, base_scale=1.1)
        toolbar = NavigationToolbar2Tk(self.canvas, self.master, pack_toolbar=False)
        toolbar.update()
        toolbar.pack()
        toolbar.pan()
        self.draw()
        tk.Label(text ="La tarifa a pagar es de: " + str(self.calculatePrice(potencias, horas)) + " quetzales").pack()
        tk.Label(text ="El diámetro del cable es de: " + str(self.calculateDiameter(potencias, corrientes, float(self.lenght))) + " metros").pack()
        tk.Label(text ="Se recomienda usar un calibre de: ")
        self.master.mainloop()
    def draw(self):
        self.ax.arrow(0, 0, 100000, 0, linewidth=50, linestyle='-', head_width=0, head_length=0, color = "#B87333")
        self.canvas.draw()
    def calculatePrice(self, potencias, horas):
        totalenergy = 0
        price = 0
        for i in range(len(potencias)):
            totalenergy += (potencias[i]/1000)*horas[i]*30
        price = totalenergy*1.47
        
        return price
    def calculateDiameter(self, potencias, corrientes, length):
        
        maxVal = max(potencias)
        maxIndex = potencias.index(maxVal)
        current = corrientes[maxIndex]
        diameter = 2*current*math.sqrt((1.72e-8*length)/(np.pi*maxVal))
        return diameter
    
    def calibre(self, diameter):
        if diameter < 0.163:
            return "14"
        elif 0.163 < diameter < 0.205:
            return "12"
        elif 0.205 < diameter < 0.259:
            return "10"
        elif 0.259 < diameter < 0.326:
            return "8"
        elif 0.326 < diameter < 0.412:
            return "6"
        elif 0.412 < diameter < 0.462:
            return "5"
        elif 0.462 < diameter < 0.519:
            return "4"
        
        def factura(self, potencias, horas):
            self.calculatePrice(potencias, horas)



if __name__ == "__main__":
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

    






