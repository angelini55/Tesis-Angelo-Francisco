import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class DiscoWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=480)
        self.master = master
        self.pack()
        self.create_widget()

    def operacionesPadm(self):
        D = float(self.textos[0].get())
        d = float(self.textos[1].get())
        µ = float(self.textos[2].get())
        Padm = float(self.textos[3].get())
        NS = float(self.textos[4].get())

        if self.seleccion.get() == 1:
            
            F = Padm*(pi/4)*((D**2)-(d**2))
            T = ((pi*µ*Padm*NS)/12)*((D**3)-(d**3))

        if self.seleccion.get() == 2:

            F = Padm*((pi*d)/2)*(D-d)
            T = ((pi*d*µ*Padm*NS)/8)*((D**2)-(d**2))
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,F)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)

    def operacionesT(self):
        pass
        # D = float(self.textos[0].get())
        # d = float(self.textos[1].get())
        # µ = float(self.textos[2].get())
        # F = float(self.textos[3].get())
        # NS = float(self.textos[4].get())

    def operacionesF(self):
        D = float(self.textos[0].get())
        d = float(self.textos[1].get())
        µ = float(self.textos[2].get())
        F = float(self.textos[3].get())
        NS = float(self.textos[4].get())

        if self.seleccion.get() == 1:

            Padm = (4*F)/(pi*((D**2)-(d**2)))
            T = ((pi*µ*Padm*NS)/12)*((D**3)-(d**3))

        if self.seleccion.get() == 2:

            Padm = (2*F)/(pi*d*(D-d))
            T = ((pi*d*µ*Padm*NS)/8)*((D**2)-(d**2))
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)
        

    def create_widget(self):

        self.seleccion = IntVar()
        self.seleccion.set(1)
        self.radio1 = Radiobutton(self, text="Presion uniforme", variable=self.seleccion, value=1)
        self.radio2 = Radiobutton(self, text="Desgaste uniforme", variable=self.seleccion, value=2)

        self.radio1.place(x=20, y=10)
        self.radio2.place(x=20, y=30)

        self.labels = []
        textoslbl = ["D","d","µ","F","NS"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=70
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30
        
        self.textos = []
        for texto in range(0,5):
            self.textos.append(Entry(self))
        i=70
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds = []
        unds = ["m","m","","N",""]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=70
        for unidades in self.listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["Padm","T"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=270
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos2 = []
        for texto in range(0,2):
            self.textos2.append(Entry(self))
        i=270
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds2 = []
        unds2 = ["Pa","N.m"]
        for unidades in unds2:
            self.listunds2.append(Label(self))
        i=270
        for unidades in self.listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename ='Freno Disco.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((250,250), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=410, y=10, height=250, width=250)

        self.boton1 = Button(self, text="Solve", command=self.operacionesF)
        self.boton1.place(x=450, y=300, width=100, height=80)

        self.lblSU = Label(self, text="Sistema de unidades")
        self.lblSU.place(x=215, y=15, width=120, height=20)

        Internacional = ["m","m","","N","","Pa","N.m"]
        Ingles = ["in","in","","lb","","PSI","lb.in"]

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
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Ingles[i])
                    i += 1
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)

        self.list2.place(x=215, y=35)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="readonly")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[3].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[3].config(text="N")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N.m")
                    self.boton1.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[3].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[3].config(text="lb")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[3].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[3].config(text="N.m")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[3].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[3].config(text="lb.in")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[3].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[3].config(text="Pa")
                    self.listunds2[0].config(text="N.m")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[3].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[3].config(text="PSI")
                    self.listunds2[0].config(text="lb.in")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(0)

        self.list.place(x=215, y=70)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    DiscoWindow(root).mainloop()