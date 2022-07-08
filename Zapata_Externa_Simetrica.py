import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class ZapataESimetricaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=680)
        self.master = master
        self.pack()
        self.create_widget()

    def ayuda(self):
        self.mensaje = """r: Radio externo del tambor
µ: Coeficiente de friccion
b: Ancho de la zapata
Padm: Presion maxima admisible
Θ2: Angulo final material de friccion
a: Distancia desde el pivote hasta el centro del tambor en la cual Mf es cero
Rx: Reaccion del pasador en el eje x
Ry: Reaccion del pasador en el eje y
T: Torque de frenado
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
        if self.list.get() == self.opciones[1]:
            Fdiseño = Pa/float(self.textos[0].get())
            self.textos2[4].delete(0,"end")
            self.textos2[4].insert(0,Fdiseño)
        else:
            Fdiseño = Pa/float(self.textos2[3].get())
            self.textos2[4].delete(0,"end")
            self.textos2[4].insert(0,Fdiseño)

    def operacionesPadm(self):
        r = float(self.textos[3].get())
        µ = float(self.textos[1].get())
        b = float(self.textos[2].get())
        Padm = float(self.textos[0].get())
        Θ2 = float(self.textos[4].get())
            
        a = (4*r*(sin(radians(Θ2))))/(2*radians(Θ2)+(sin(radians(2*Θ2))))
        a = round(a,3)

        Rx = ((Padm*b*r)/2)*(2*radians(Θ2)+(sin(2*radians(Θ2))))
        Rx = round(Rx,3)

        Ry = ((µ*Padm*b*r)/2)*(2*radians(Θ2)+(sin(2*radians(Θ2))))
        Ry = round(Ry,3)

        N = 2*Padm*b*r*(sin(radians(Θ2)))

        T = a*µ*N
        T = round(T,3)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,a)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,Rx)
        
        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,Ry)

        self.textos2[3].delete(0,"end")
        self.textos2[3].insert(0,T)

    def operacionesT(self):
        r = float(self.textos[3].get())
        µ = float(self.textos[1].get())
        b = float(self.textos[2].get())
        T = float(self.textos[0].get())
        Θ2 = float(self.textos[4].get())

        a = (4*r*(sin(radians(Θ2))))/(2*radians(Θ2)+(sin(radians(2*Θ2))))
        a = round(a,3)

        N = T/(a*µ)

        Padm = N/(2*b*r*(sin(radians(Θ2))))
        Padm = round(Padm,3)

        Rx = ((Padm*b*r)/2)*(2*radians(Θ2)+(sin(2*radians(Θ2))))
        Rx = round(Rx,3)

        Ry = ((µ*Padm*b*r)/2)*(2*radians(Θ2)+(sin(2*radians(Θ2))))
        Ry = round(Ry,3)
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,a)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,Rx)
        
        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,Ry)

        self.textos2[3].delete(0,"end")
        self.textos2[3].insert(0,Padm)

    # def operacionesF(self):
    #     a1 = float(self.textos[0].get())
    #     a2 = float(self.textos[1].get())
    #     a3 = float(self.textos[2].get())
    #     a4 = float(self.textos[3].get())
    #     a5 = float(self.textos[4].get())
    #     a6 = float(self.textos[5].get())
    #     a7 = float(self.textos[6].get())
    #     a8 = float(self.textos[7].get())
    #     a9 = float(self.textos[8].get())
    #     a10 = float(self.textos[9].get())
    #     a11 = float(self.textos[10].get())

    #     I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
    #     I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
    #     I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

    #     valor1 = (a6*a3*(a5/2)/(sin(a9*(3.14/180))))*I3
    #     valor2 = (a2*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

    #     if self.seleccion.get() == 1:

    #         padm = (a1*a4)/(valor1-valor2)
    #         padm = round(padm,3)

    #         T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
    #         T = round(T,3)

    #         Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - a10
    #         Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3-(a2*I2))) + a11

    #     if self.seleccion.get() == 2:
            
    #         padm = (a1*a4)/(valor1+valor2)
    #         padm = round(padm,3)

    #         T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
    #         T = round(T,3)

    #         Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - a10
    #         Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3+(a2*I2))) + a11
        
    #     self.textos2[0].delete(0,"end")
    #     self.textos2[0].insert(0,Rx)

    #     self.textos2[1].delete(0,"end")
    #     self.textos2[1].insert(0,Ry)
        
    #     self.textos2[3].delete(0,"end")
    #     self.textos2[3].insert(0,padm)

    #     self.textos2[2].delete(0,"end")
    #     self.textos2[2].insert(0,T)
        

    def create_widget(self):

        self.labels = []
        textoslbl = ["Padm","µ","b","r","Θ2"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=80
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30
        
        self.textos = []
        for texto in range(0,5):
            self.textos.append(Entry(self, state="disabled"))
        i=80
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds = []
        unds = ["Pa","","m","m","°"]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=80
        for unidades in self.listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["a","Rx","Ry","T","FD"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=450
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos2 = []
        for texto in range(0,5):
            self.textos2.append(Entry(self, state="disabled"))
        i=450
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds2 = []
        unds2 = ["m","N","N","N.m",""]
        for unidades in unds2:
            self.listunds2.append(Label(self))
        i=450
        for unidades in self.listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename ='images\\Freno Zapata Externa Simetrica.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((300,300), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=350, y=110, height=300, width=300)

        self.boton1 = Button(self, text="Solve", command=self.operacionesPadm)
        self.boton1.place(x=450, y=500, width=100, height=80)

        self.lblSU = Label(self, text="Sistema de unidades")
        self.lblSU.place(x=215, y=15, width=120, height=20)

        Internacional = ["Pa","","m","m","°","m","N","N","N.m",""]
        Ingles = ["PSI","","in","in","°","in","lb","lb","lb.in",""]

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
                for entries in self.textos:
                    entries.config(state=NORMAL)
                for entries in self.textos2:
                    entries.config(state=NORMAL)
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Ingles[i])
                    i += 1
                self.list["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                for entries in self.textos2:
                    entries.config(state=NORMAL)
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)

        self.list2.place(x=215, y=35)

        self.opciones = ["Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="T")
                    self.labels2[3].config(text="Padm")
                    self.listunds[0].config(text="N.m")
                    self.listunds2[3].config(text="Pa")
                    self.boton1.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="T")
                    self.labels2[3].config(text="Padm")
                    self.listunds[0].config(text="lb.in")
                    self.listunds2[3].config(text="PSI")
                    self.boton1.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="Padm")
                    self.labels2[3].config(text="T")
                    self.listunds[0].config(text="Pa")
                    self.listunds2[3].config(text="N.m")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="Padm")
                    self.labels2[3].config(text="T")
                    self.listunds[0].config(text="PSI")
                    self.listunds2[3].config(text="lb.in")
                    self.boton1.config(command=self.operacionesPadm)
            # elif self.list.get() == self.opciones[2]:
            #     if self.list2.get() == self.listaUnds[0]:
            #         self.labels[0].config(text="Padm")
            #         self.labels2[2].config(text="T")
            #         self.labels2[3].config(text="F")
            #         self.listunds[0].config(text="Pa")
            #         self.listunds2[2].config(text="N.m")
            #         self.listunds2[3].config(text="N")
            #         self.boton1.config(command=self.operacionesPadm)
            #     if self.list2.get() == self.listaUnds[1]:
            #         self.labels[0].config(text="Padm")
            #         self.labels2[2].config(text="T")
            #         self.labels2[3].config(text="F")
            #         self.listunds[0].config(text="PSI")
            #         self.listunds2[2].config(text="lb.in")
            #         self.listunds2[3].config(text="lb")
            #         self.boton1.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(1)

        self.list.place(x=215, y=70)

#parte de la tabla
        self.lbl18 = Label(self,text='Pa')
        self.lbl18.place(x=200, y=505, width=40, height=20)
        self.txt18 = Entry(self)
        self.txt18.place(x=240, y=500, width=70, height=20)
        self.lbl36 = Label(self)
        self.lbl36.place(x=200, y=470, width=150, height=20)

        self.btnayuda = Button(self, text='?', command = self.ayuda)
        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn4 = Button(self, text='calc', command=self.CalcFD)
        self.btnayuda.place(x=215, y=130, width=30, height=30)
        self.btn3.place(x=320, y=500, width=40, height=40)
        self.btn4.place(x=320, y=550, width=40, height=40)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    ZapataESimetricaWindow(root).mainloop()