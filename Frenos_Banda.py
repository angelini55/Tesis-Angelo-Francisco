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
        super().__init__(master, width=700, height=680)
        self.master = master
        self.pack()
        self.create_widget()

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


        listunds = []
        unds = ["PSI","in","in","","°"]
        for unidades in unds:
            listunds.append(Label(self, text=unidades))
        i=10
        for unidades in listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["P1","P2","T"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=200
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self))
        i=200
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        listunds2 = []
        unds2 = ["lb","lb","lb.in"]
        for unidades in unds2:
            listunds2.append(Label(self, text=unidades))
        i=200
        for unidades in listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'Freno Banda.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((250,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=350, y=10, height=350, width=250)

        self.boton1 = Button(self, text="Solve", command=self.operacionesPadm)
        self.boton1.place(x=400, y=400, width=100, height=80)



if __name__ == "__main__":
    root = Tk()
    root.resizable(0,0)
    root.wm_title("Frenos de tambor con zapata interna")
    BandaWindow(root).mainloop()