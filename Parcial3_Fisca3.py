

import tkinter as tk
from tkinter import messagebox

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
        tk.Checkbutton(text = "Cocina", variable = self.cocina, onvalue = "Cocina", offvalue = "0").pack()
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
        self.datos = self.generateDict(self.electrodomesticos)
        print(self.datos)
        if (len(self.electrodomesticos) == 0 or len(self.electrodomesticos) > 10):
            tk.messagebox.showerror("Error", "Selecciona entre 1 y 10 electrodomésticos")
        elif (self.lenght.get() == "" or self.lenght.get().isdigit() == False or self.lenght.get() == "0"):
            tk.messagebox.showerror("Error", "Ingresa un largo válido")
        else:
            self.final_lenght = self.lenght.get()
            self.master.destroy()
            Window2(self.electrodomesticos, self.final_lenght, self.datos, self.electrodomesticos[0], 0)


    def generateDict(self, list):
        dict = {}
        for i in range (len(list)):
            dict[list[i]] = []

        return dict


class Window2:
    def __init__(self, list, lenght, dict, name, index):
        self.index = index
        self.list = list
        self.lenght = lenght
        self.electrodomesticos = dict
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
        tk.Label(text = "Potencia (kilowatts)").pack()
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
        else:
            self.electrodomesticos[self.name].append(self.Voltaje.get())
            self.electrodomesticos[self.name].append(self.Corriente.get())
            self.electrodomesticos[self.name].append(self.Potencia.get())
            self.electrodomesticos[self.name].append(self.horas.get())

            if (self.index < len(self.list)):
                self.index += 1
                self.name = self.list[self.index]
                self.master.destroy()
                Window2(self.list, self.lenght, self.electrodomesticos, self.name, self.index)
            else:
                self.master.destroy()
                Window3(self.list, self.lenght, self.electrodomesticos)

class Window3:
    def __init__(self, list, lenght, dict):
        self.list = list
        self.lenght = lenght
        self.electrodomesticos = dict
        self.master = tk.Tk()
        self.master.title("Resultados")
        self.master.geometry("1000x1000")
        self.master.mainloop()




if __name__ == "__main__":
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

    






