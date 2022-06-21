import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class CircularWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=480)
        self.master = master
        self.pack()
        self.create_widget()

    def ayuda(self):
        self.mensaje = """R: Radio de la zapata circular
r': Ubicación de la línea de acción de la fuerza de accionamiento
Padm: Presión máxima admisible ejercida sobre el material de fricción
µ: Coeficiente de friccion
T: Par de torsion del freno o embrague
F: Fuerza de accionamiento
FD: Factor de diseño"""

        messagebox.showinfo(title="Ayuda", message=self.mensaje)

    def tablaMaterial(self):
        if self.list2.get() == self.listaUnds[0]:
            tabla = Toplevel()
            self.table = TablaMaterialesSI(tabla, self)
        if self.list2.get() == self.listaUnds[1]:
            tabla = Toplevel()
            self.table = TablaMaterialesIngles(tabla, self)

    def CalcFD(self):
        if self.list2.get() == self.listaUnds[0]:
            Pa = float(self.txt18.get())*1000
        else:
            Pa = float(self.txt18.get())
        if self.list.get() == self.opciones[2]:
            Fdiseño = Pa/float(self.textos[2].get())
            self.textos2[2].delete(0,"end")
            self.textos2[2].insert(0,Fdiseño)
        else:
            Fdiseño = Pa/float(self.textos2[0].get())
            self.textos2[2].delete(0,"end")
            self.textos2[2].insert(0,Fdiseño)

    def _interpolation(self, string, value):
        self.string = string
        self.value = value
        selected_dropdown_option = string  #  Value to get from the interface
        reference_value = value            #  Value to get from the interface

        database_dict = {
            "alpha": [],
            "beta": [],
            "Rr": [],
            "alpha_diff": [],
            "beta_diff": [],
            "Rr_diff": []
        }

        #  Connect to database to get this
        table_data = [(0.5, 0.938, 1.875), (0.4, 0.947, 1.578), (0.3, 0.957, 1.367), (0.2, 0.969, 1.212), (0.1, 0.983, 1.093), (0, 1, 1)]

        for Rr, alpha, beta in table_data:
            database_dict["alpha"].append(alpha)
            database_dict["beta"].append(beta)
            database_dict["Rr"].append(Rr)
            database_dict["alpha_diff"].append((alpha - reference_value) if (alpha - reference_value) >= 0 else (alpha - reference_value) * (-1))
            database_dict["beta_diff"].append((beta - reference_value) if (beta - reference_value) >= 0 else (beta - reference_value) * (-1))
            database_dict["Rr_diff"].append((Rr - reference_value) if (Rr - reference_value) >= 0 else (Rr - reference_value) * (-1))


        if (reference_value >= min(database_dict[selected_dropdown_option])) and (reference_value <= max(database_dict[selected_dropdown_option])):

            interpolation_indexes = []
            i = 0
            while i <= 1:
                value = min(database_dict[selected_dropdown_option + "_diff"])
                index = database_dict[selected_dropdown_option + "_diff"].index(value)
                interpolation_indexes.append(index)
                database_dict[selected_dropdown_option + "_diff"][index] += 100
                i += 1

            parameters_for_interpolation = [key for key in database_dict.keys() if ((selected_dropdown_option not in key) and ("diff" not in key))]

            interpolation_results = {}
            i0, i1 = interpolation_indexes
            for parameter in parameters_for_interpolation:

                #  Interpolation Equation: y = y0 + (x-x0)*((y1-y0)/(x1-x0))
                interpolation_results[parameter] = database_dict[parameter][i0] + (
                    reference_value - database_dict[selected_dropdown_option][i0]) * (
                        (database_dict[parameter][i1] - database_dict[parameter][i0]) / (
                            database_dict[selected_dropdown_option][i1] - database_dict[selected_dropdown_option][i0]))
            
            self.interpolation_results = interpolation_results
            return interpolation_results

    def operacionesPadm(self):
        R = float(self.textos[0].get())
        r = float(self.textos[1].get())
        Padm = float(self.textos[2].get())
        µ = float(self.textos[3].get())

        Interpolation_string = "Rr"
        Rr = R/r
        self._interpolation(Interpolation_string,Rr)
        alpha = self.interpolation_results["alpha"]
        beta = self.interpolation_results["beta"]

        Pprom = alpha*Padm
        F = pi*(R**2)*Pprom
        T = µ*F*beta*r        


        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,F)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)


    def operacionesT(self):
        D = float(self.textos[0].get())
        d = float(self.textos[1].get())
        α = float(self.textos[2].get())
        µ = float(self.textos[3].get())
        T = float(self.textos[4].get())

        if self.seleccion.get() == 1:

            Padm = (12*T*sin(radians(α)))/(pi*µ*((D**3)-(d**3)))
            F = (pi/4)*Padm*((D**2)-(d**2))          

        if self.seleccion.get() == 2:

            Padm = (8*T*sin(radians(α)))/(pi*d*µ*((D**2)-(d**2)))
            F = (pi/2)*d*Padm*(D-d)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,F)

    def operacionesF(self):
        D = float(self.textos[0].get())
        d = float(self.textos[1].get())
        α = float(self.textos[2].get())
        µ = float(self.textos[3].get())
        F = float(self.textos[4].get())

        if self.seleccion.get() == 1:

            Padm = (4*F)/(pi*((D**2)-(d**2)))
            T = ((pi*µ*Padm)/(12*sin(radians(α))))*(((D**3)-(d**3)))

        if self.seleccion.get() == 2:

            Padm = (2*F)/(pi*d*(D-d))
            T = ((pi*d*µ*Padm)/(8*sin(radians(α))))*(((D**2)-(d**2)))
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)
        

    def create_widget(self):

        self.labels = []
        textoslbl = ["R","r'","Padm","µ"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=70
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30
        
        self.textos = []
        for texto in range(0,4):
            self.textos.append(Entry(self))
        i=70
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds = []
        unds = ["m","m","Pa",""]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=70
        for unidades in self.listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["F","T","FD"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=270
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self))
        i=270
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds2 = []
        unds2 = ["N","N.m",""]
        for unidades in unds2:
            self.listunds2.append(Label(self))
        i=270
        for unidades in self.listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename ='images\\Freno Zapata Circular.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((300,250), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=390, y=10, height=250, width=300)

        self.boton1 = Button(self, text="Solve", command=self.operacionesPadm)
        self.boton1.place(x=450, y=300, width=100, height=80)

        self.lblSU = Label(self, text="Sistema de unidades")
        self.lblSU.place(x=215, y=15, width=120, height=20)

        Internacional = ["m","m","Pa","","N","N.m",""]
        Ingles = ["in","in","PSI","","lb","lb.in",""]

        self.listaUnds = ["Sistema Internacional","Sistema Ingles"]
        self.list2 = Combobox(self, width=20, values=self.listaUnds, state="readonly")
        def cambioUnds(event):
            if self.list2.get() == self.listaUnds[0]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Internacional[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Internacional[i])
                    i += 1
                self.list["state"]="readonly"
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Ingles[i])
                    i += 1
                self.list["state"]="readonly"
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)

        self.list2.place(x=215, y=35)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[4].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[4].config(text="N")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N.m")
                    self.boton1.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[4].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[4].config(text="lb")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[4].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[4].config(text="N.m")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[4].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[4].config(text="lb.in")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[4].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[4].config(text="Pa")
                    self.listunds2[0].config(text="N.m")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[4].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[4].config(text="PSI")
                    self.listunds2[0].config(text="lb.in")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(2)

        self.list.place(x=215, y=70)

        self.lbl18 = Label(self,text='Pa')
        self.lbl18.place(x=200, y=305, width=40, height=20)
        self.txt18 = Entry(self)
        self.txt18.place(x=240, y=300, width=70, height=20)
        self.lbl36 = Label(self)
        self.lbl36.place(x=200, y=270, width=150, height=20)

        self.btnayuda = Button(self, text='?', command = self.ayuda)
        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn4 = Button(self, text='calc', command=self.CalcFD)
        self.btnayuda.place(x=215, y=130, width=30, height=30)
        self.btn3.place(x=320, y=300, width=40, height=40)
        self.btn4.place(x=320, y=350, width=40, height=40)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    CircularWindow(root).mainloop()