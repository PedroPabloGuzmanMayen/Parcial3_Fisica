

import tkinter as tk

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
        tk.Label(text = "Selecciona el voltaje ").pack()


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
        print(len(self.list))
        

        print(self.lavadora.get())
    def isZero(self, list):
        for i in range(len(list)):
            if list[i] == "0":
                list.pop(i)



if __name__ == "__main__":
    root = tk.Tk()
    app = Window1(root)
    root.mainloop()

    






