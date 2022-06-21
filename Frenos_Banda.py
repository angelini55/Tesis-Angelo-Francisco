import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class BandaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=530)
        self.master = master
        self.pack()
        self.create_widget()

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
            Fdiseño = Pa/float(self.textos[0].get())
            self.textos2[3].delete(0,"end")
            self.textos2[3].insert(0,Fdiseño)
        else:
            Fdiseño = Pa/float(self.textos2[1].get())
            self.textos2[3].delete(0,"end")
            self.textos2[3].insert(0,Fdiseño)

    def operacionesF1(self):
        F1 = float(self.textos[0].get())
        D = float(self.textos[1].get())
        b = float(self.textos[2].get())
        µ = float(self.textos[3].get())
        Ø = float(self.textos[4].get())

        pedacito = µ*(Ø*(pi/180))

        Padm = F1/(b*(D/2))
        Padm = round(Padm,3)

        F2 = F1/(e**pedacito)
        F2 = round(F2,3)

        T = (F1-F2)*(D/2)
        T = round(T,3)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,F2)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,Padm)

        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,T)

    def operacionesF2(self):
        F2 = float(self.textos[0].get())
        D = float(self.textos[1].get())
        b = float(self.textos[2].get())
        µ = float(self.textos[3].get())
        Ø = float(self.textos[4].get())

        pedacito = µ*(Ø*(pi/180))

        F1 = (e**pedacito)*F2
        F1 = round(F1,3)

        T = (F1-F2)*(D/2)
        T = round(T,3)

        Padm = F1/(b*(D/2))
        Padm = round(Padm,3)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,F1)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,Padm)

        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,T)


    def operacionesPadm(self):
        Padm = float(self.textos[0].get())
        D = float(self.textos[1].get())
        b = float(self.textos[2].get())
        µ = float(self.textos[3].get())
        Ø = float(self.textos[4].get())

        P1 = Padm*b*(D/2)
        pedacito = µ*(Ø*(pi/180))

        P2 = P1/(e**pedacito)

        T = (P1-P2)*(D/2)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,P1)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,P2)

        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,T)

    def ayuda(self):
        self.mensaje = """Padm: Presion maxima admisible ejercida sobre el material de friccion
D: Diametro externo del tambor
b: Ancho de la banda
µ: Coeficiente de friccion
Ø: Angulo de contacto entre la banda y el tambor
F1: Fuerza en el pasador
F2: Fuerza de accionamiento 
T: Par de torsion del freno o embrague
FD: Factor de diseño"""
        messagebox.showinfo(title="Ayuda", message=self.mensaje)

    def create_widget(self):

        self.labels = []
        textoslbl = ["Padm","D","b","µ","Ø"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=10
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos = []
        for texto in range(0,5):
            self.textos.append(Entry(self))
        i=10
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30


        self.listunds = []
        unds = ["PSI","in","in","","°"]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=10
        for unidades in self.listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["F1","F2","T","FD"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=200
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos2 = []
        for texto in range(0,4):
            self.textos2.append(Entry(self))
        i=200
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds2 = []
        unds2 = ["lb","lb","lb.in",""]
        for unidades in unds2:
            self.listunds2.append(Label(self))
        i=200
        for unidades in self.listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'images\\Freno Banda.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((250,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=400, y=10, height=350, width=250)

        self.boton1 = Button(self, text="Solve", command=self.operacionesPadm)
        self.boton1.place(x=400, y=400, width=100, height=80)

        self.lblSU = Label(self, text="Sistema de unidades")
        self.lblSU.place(x=215, y=15, width=120, height=20)

        Internacional = ["Pa","m","m","","°","N","N","N.m",""]
        Ingles = ["PSI","in","in","","°","lb","lb","lb.in",""]

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

        self.opciones = ["Dada F2, hallar F1, T y Padm", "Dada F1, hallar F2, T y Padm", "Dada Padm, hallar F1, F2 y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="F2")
                    self.labels2[0].config(text="F1")
                    self.labels2[1].config(text="Padm")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="N")
                    self.listunds2[0].config(text="N")
                    self.listunds2[1].config(text="Pa")
                    self.listunds2[2].config(text="N.m")
                    self.boton1.config(command=self.operacionesF2)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="F2")
                    self.labels2[0].config(text="F1")
                    self.labels2[1].config(text="Padm")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="lb")
                    self.listunds2[0].config(text="lb")
                    self.listunds2[1].config(text="PSI")
                    self.listunds2[2].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF2)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="F1")
                    self.labels2[0].config(text="F2")
                    self.labels2[1].config(text="Padm")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="N")
                    self.listunds2[0].config(text="N")
                    self.listunds2[1].config(text="Pa")
                    self.listunds2[2].config(text="N.m")
                    self.boton1.config(command=self.operacionesF1)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="F1")
                    self.labels2[0].config(text="F2")
                    self.labels2[1].config(text="Padm")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="lb")
                    self.listunds2[0].config(text="lb")
                    self.listunds2[1].config(text="PSI")
                    self.listunds2[2].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF1)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="Padm")
                    self.labels2[0].config(text="F1")
                    self.labels2[1].config(text="F2")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="Pa")
                    self.listunds2[0].config(text="N")
                    self.listunds2[1].config(text="N")
                    self.listunds2[2].config(text="N.m")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="Padm")
                    self.labels2[0].config(text="F1")
                    self.labels2[1].config(text="F2")
                    self.labels2[2].config(text="T")
                    self.listunds[0].config(text="PSI")
                    self.listunds2[0].config(text="lb")
                    self.listunds2[1].config(text="lb")
                    self.listunds2[2].config(text="lb.in")
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
        self.btnayuda.place(x=215, y=130, width=30, height=30)
        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn4 = Button(self, text='calc', command=self.CalcFD)
        self.btn3.place(x=320, y=300, width=40, height=40)
        self.btn4.place(x=320, y=350, width=40, height=40)



if __name__ == "__main__":
    root = Tk()
    root.resizable(0,0)
    root.wm_title("Frenos de tambor con zapata interna")
    BandaWindow(root).mainloop()