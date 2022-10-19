import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from tkinter.ttk import * 
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles
import tkinter as tk 

class TemperaturaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=1000)
        self.master = master
        self.pack()
        self.create_widgets()
    
    def tablaMaterial(self):
        if self.list2.get() == self.listaUnds[0]:
            tabla = Toplevel()
            self.table = TablaMaterialesSI(tabla, self)
        if self.list2.get() == self.listaUnds[1]:
            tabla = Toplevel()
            self.table = TablaMaterialesIngles(tabla, self)

    def operacionesPadm(self):
        Tamb = float(self.textos[0].get())
        wi = float(self.textos[1].get())
        wf = float(self.textos[2].get())
        I = float(self.textos[3].get())
        D = float(self.textos[4].get())
        L = float(self.textos[5].get())
        h = float (self.textos[6].get())
        C = float(self.textos[7].get())
        ρ= float(self.textos[8].get()) 
        

        W = (pi*D*L*h*ρ)

        E = (I/18672)*(wi**2-wf**2)

        ΔT = (E/W*C)

        

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,W)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,E)

        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,ΔT)

    def operaciones2(self):
        hr = float(self.textos3[0].get())
        FMC = float(self.textos3[1].get())
        hc = float(self.textos3[2].get())
        D = float(self.textos3[3].get())
        L = float(self.textos3[4].get())
        C = float(self.textos3[5].get())
        h = float(self.textos3[6].get())
        ρ = float(self.textos3[7].get())

        

        W = (pi*D*L*h*ρ)
    
        U = hr + (FMC*hc)

        β = (U)*(L*pi*D)/(W*C)

        self.textos4[0].delete(0,"end")
        self.textos4[0].insert(0,β)

    def operaciones3(self):
        NAF = float(self.textos5[0].get())
        Tt = float(self.textos5[1].get())
        Tamb = float(self.textos5[2].get())
        ΔT = float(self.textos5[3].get())
        β = float(self.textos5[4].get())
        
     
        t1 = (Tt/NAF)*60*60

        Tmax = Tamb + (ΔT/1-(e**(-β*t1)))
        
        Tmin = (Tmax- ΔT)

        self.textos6[0].delete(0,"end")
        self.textos6[0].insert(0,t1)

        self.textos6[1].delete(0, "end")
        self.textos6[1].insert(0, Tmax)

        self.textos6[2].delete(0, "end")
        self.textos6[2].insert(0, Tmin)

        self.btn6["state"]= "normal"

    def ayuda(self):
        self.mensaje = """Tamb: Temperatura ambiente
wi: Velocidad inicial
wf: Velocidad final
I: Inercia equivalente
D: Diametro del tambor
L: longitud del tambor
h: Espesor del tambor 
C: Capacidad termica especifica 
ρ: Peso especifico del material, disco o tambor 
W: Peso del disco o tambor
E: Energía disipado por el freno o embrague
ΔT: Diferencial de temperatura
U: Coeficiente de transferencia termica global
hr: Coefciente de transfercia termica por radiación
hc: Coeficiente de transferencia termica por convección
FMC: Factor de modificación del coeficiente de transferencia térmica por convección"""

        messagebox.showinfo(title="Ayuda", message=self.mensaje)
    
    def graficos(self):

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'HERRAMIENTAGRAFICA.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl18 = Label(self, image=self.img)
        self.lbl18.place(x=360, y=10, height=350, width=350)


    def create_widgets(self): 

        self.labels = []
        textoslbl = ["Tamb","wi","wf","I","D","L","h","C","ρ"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=10
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos = []
        for texto in range(0,9):
            self.textos.append(Entry(self))
        i=10
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30


        self.listunds = []
        unds = ["ºF","rad/s","rad/s","lbm.pulg.s","pulg","pulg","pulg","Btu/Lbm.ºF","Lb/pulg^3"]
        for unidades in unds:
            self.listunds.append(Label(self, text=unidades))
        i=10
        for unidades in self.listunds:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels2 = []
        textoslabels2 = ["W","E","ΔT"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=320
        for cosas in self.labels2:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30


        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self))
        i=320
        for parameters in self.textos2:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds2 = []
        unds2 = ["lb","Btu","ºF"]
        for unidades in unds2:
            self.listunds2.append(Label(self, text=unidades))
        i=320
        for unidades in self.listunds2:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30


        self.labels3 = []
        textoslb3 = ["hr","FMC","hc","L","D","C","h","ρ"]
        for textos in textoslb3:
            self.labels3.append(Label(self, text=textos))
        i=440
        for cosas in self.labels3:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30

        self.textos3 = []
        for texto in range(0,8):
            self.textos3.append(Entry(self))
        i=440
        for parameters in self.textos3:
            parameters.place(x=70, y=i, width=80)
            i += 30
        
        self.listunds3 = []
        unds = ["Btu/pulg2.s.°F","","Btu/pulg2.s.°F","pulg","pulg"]
        for unidades in unds:
            self.listunds3.append(Label(self, text=unidades))
        i=440
        for unidades in self.listunds3:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        self.labels4 = []
        textoslabels4 = ["β"]
        for textos in textoslabels4:
            self.labels4.append(Label(self, text=textos))
        i=680
        for cosas in self.labels4:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30


        self.textos4 = []
        for texto in range(0,1):
            self.textos4.append(Entry(self))
        i=680
        for parameters in self.textos4:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds4 = []
        unds = ["s-1"]
        for unidades in unds:
            self.listunds4.append(Label(self, text=unidades))
        i=680
        for unidades in self.listunds4:
            unidades.place(x=160, y=i, width=60, height=20)
            i += 30

        
        self.labels5 = []
        textoslabels5 = ["NAF","Tt", "Tamb", "ΔT", "β"]
        for textos in textoslabels5:
            self.labels5.append(Label(self, text=textos))
        i=440
        for cosas in self.labels5:
            cosas.place(x=510, y=i, width=60, height=20)
            i += 30


        self.textos5 = []
        for texto in range(0,5):
            self.textos5.append(Entry(self))
        i=440
        for parameters in self.textos5:
            parameters.place(x=580, y=i, width=80)
            i += 30

        self.listunds5 = []
        unds = ["veces que se activa","Horas" ,"ºF", "ºF","s^-1"]
        for unidades in unds:
            self.listunds5.append(Label(self, text=unidades))
        i=440
        for unidades in self.listunds5:
            unidades.place(x=670, y=i, width=60, height=20)
            i += 30

        self.labels6 = []
        textoslabels6 = ["t1","Tmax","Tmin"]
        for textos in textoslabels6:
            self.labels6.append(Label(self, text=textos))
        i=640
        for cosas in self.labels6:
            cosas.place(x=510, y=i, width=60, height=20)
            i += 30


        self.textos6 = []
        for texto in range(0,3):
            self.textos6.append(Entry(self))
        i=640
        for parameters in self.textos6:
            parameters.place(x=580, y=i, width=80)
            i += 30

        self.listunds6 = []
        unds = ["s","ºF","ºF"]
        for unidades in unds:
            self.listunds6.append(Label(self, text=unidades))
        i=640
        for unidades in self.listunds6:
            unidades.place(x=670, y=i, width=60, height=20)
            i += 30


        self.labels7 = []
        textoslabels7 = ["Tcon"]
        for textos in textoslabels7:
            self.labels7.append(Label(self, text=textos))
        i=750
        for cosas in self.labels7:
            cosas.place(x=510, y=i, width=60, height=20)
            i += 30


        self.txt18 = Entry(self)
        self.txt18.place(x=580, y=750, width=80)

        self.lbl36 = Label(self)
        self.lbl36.place(x=580, y=730)

        self.cumple_si_no = Label(self)
        self.cumple_si_no.place(x=750, y=730)

        self.listunds7 = []
        unds = ["ºF"]
        for unidades in unds:
            self.listunds7.append(Label(self, text=unidades))
        i=750
        for unidades in self.listunds7:
            unidades.place(x=670, y=i, width=60, height=20)
            i += 30


        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'images\\frenoscamara.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((320,320), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=370, y=10, height=350, width=350)

        self.boton1 = tk.Button(self, text="Solve", command=self.operacionesPadm, bg="light blue")
        self.btn2 = tk.Button(self, text='?', command = self.ayuda, bg="yellow")
        self.btn3 = tk.Button(self, text = "graficos", command= self.graficos, bg="white")
        self.btn4 = tk.Button(self, text= "solve", command=self.operaciones2, bg="light blue")
        self.btn5 = tk.Button(self, text= "solve", command=self.operaciones3, bg = "light blue")
        self.btn6 = Button(self, text='tabla', command=self.tablaMaterial, state="disabled")
        self.boton1.place(x=400, y=400, width=100, height=80)
        self.btn2.place(x=230, y=100, width=50, height=40)
        self.btn3.place(x=240,y = 400, width=100, height=80)
        self.btn4.place(x= 240, y= 600, width=100, height=80)
        self.btn5.place(x= 800, y=400, width=60, height=40)
        self.btn6.place(x= 800, y=500, width=60, height=40)

        Internacional = ["ºC","rad/s","rad/s","kg.m.s","m","m","m","Joules/N.ºC","N/m^3","N","J","ºC","Joules/m^2","","Joules/m^2","m","m"]
        Ingles = ["ºF","rad/s","rad/s","lbm.pulg.s","pulg","pulg","pulg","Btu/lbm.ºF","lb/pulg^3","Lb","Btu","ºF","Btu/pulg^2","", "Btu/pulg^2","pulg","pulg"]

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
                for lbl in self.listunds3:
                    lbl.config(text=Internacional[i])
                    i += 1
                #self.list["state"]="readonly"
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds3:
                    lbl.config(text=Ingles[i])
                    i += 1
                #self.list["state"]="readonly"
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.current(1)

        self.list2.place(x=220, y=50)


if __name__ == "__main__":
    root = Tk()
    root.resizable(1,1)
    root.wm_title("Aumento y disipación de energía")
    #root.iconbitmap(r"C:\Users\Eukaris\Downloads\Luz2.ico")
    TemperaturaWindow(root).mainloop()


















        

