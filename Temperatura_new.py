import os
import pathlib
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from tkinter import ttk
from math import *
from PIL import ImageTk, Image


class TemperaturaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1200, height=760)
        self.master = master
        self.pack()
        self.create_widgets()

    def change_graph(self):
        if self.image_filename == 'images\\hc y hr temperatura.png':
            self.image_filename = 'images\\FMC temperatura.png'
            self.base_path = pathlib.Path(__file__).parent.resolve()
            self.image = Image.open(os.path.join(self.base_path, self.image_filename))
            self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(self.image)
            self.lbl_img1 = Label(self, image=self.img)
            self.lbl_img1.place(x=650, y=40, width=350, height=350)
        else:
            self.image_filename = 'images\\hc y hr temperatura.png'
            self.base_path = pathlib.Path(__file__).parent.resolve()
            self.image = Image.open(os.path.join(self.base_path, self.image_filename))
            self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(self.image)
            self.lbl_img1 = Label(self, image=self.img)
            self.lbl_img1.place(x=650, y=40, width=350, height=350)
    
    def calculo_deltaT(self):
        wi = float(self.textos[1].get())
        wf = float(self.textos[2].get())
        I = float(self.textos[3].get())
        gamma = float(self.textos[4].get())
        C = float(self.textos[5].get())

        if self.list2.get() == "Sistema Internacional":
            E = (I/204.10)*abs(((wi*(2*pi/60))**2)-((wf*(2*pi/60))**2))
        else:
            E = (I/18672)*abs(((wi*(2*pi/60))**2)-((wf*(2*pi/60))**2))

        if self.tipo_freno.get() == "Disco":
            D = float(self.textos2[0].get())
            d = float(self.textos2[1].get())
            t = float(self.textos2[2].get())
            self.W = (pi/4)*((D**2)-(d**2)*t*gamma)
        elif self.tipo_freno.get() == "Tambor":
            L = float(self.textos2[0].get())
            D = float(self.textos2[1].get())
            t = float(self.textos2[2].get())
            self.W = pi*D*L*t*gamma
        else:
            Ri = float(self.textos2[0].get())
            ri = float(self.textos2[1].get())
            h = float(self.textos2[2].get())
            t = float(self.textos2[3].get())
            self.W = (pi/3)*h*((((Ri+t)**3)-((ri+t)**3)/Ri-ri)-((Ri**3)-(ri**3)/Ri-ri))*gamma

        deltaT = E/(self.W*C)
        deltaT = round(deltaT,2)

        self.delta_T_textbox.delete(0,"end")
        self.delta_T_textbox.insert(0,deltaT)

    def calculoTmax(self):
        Tamb = float(self.textos[0].get())
        deltaT = float(self.delta_T_textbox.get())
        hc = float(self.textos3[0].get())
        hr = float(self.textos3[1].get())
        FMC = float(self.textos3[2].get())
        C = float(self.textos[5].get())

        V = float(self.textos[6].get())
        Tt = float(self.textos[7].get())

        U = hr + FMC*hc

        if self.tipo_freno.get() == "Disco":
            D = float(self.textos2[0].get())
            d = float(self.textos2[1].get())
            A = (pi/4)*((D**2)-(d**2))
        elif self.tipo_freno.get() == "Tambor":
            L = float(self.textos2[0].get())
            D = float(self.textos2[1].get())
            A = pi*D*L
        else:
            Ri = float(self.textos2[0].get())
            ri = float(self.textos2[1].get())
            h = float(self.textos2[2].get())
            A = pi*h*(Ri+ri)

        ß = (U*A)/(self.W*C)
        Ita = (Tt/V)*3600

        Tmax = Tamb + (deltaT)/(1-(e**(-ß*Ita)))
        Tmin = Tmax - deltaT

        self.textos4[0].delete(0,"end")
        self.textos4[0].insert(0,A)

        self.textos4[1].delete(0,"end")
        self.textos4[1].insert(0,U)

        self.textos4[2].delete(0,"end")
        self.textos4[2].insert(0,ß)

        self.textos4[3].delete(0,"end")
        self.textos4[3].insert(0,Tmax)

        self.textos4[4].delete(0,"end")
        self.textos4[4].insert(0,Tmin)


    def create_widgets(self):
        Internacional = ["°C","rpm","rpm","kgm.m.s","N/m^3","Joule/(kgm.°C)","","horas","mm","mm","mm","Joule/(m2.s.°C)","Joule/(m2.s.°C)","",
        "mm^2","Joule/(m^2.s.°C)","s^-1","°C","°C"]
        Ingles = ["°F","rpm","rpm","lbm.pulg.s","lb/pulg^3","Btu/(lbm.°F)","","horas","in","in","in","Btu/(pulg2.s.°F)","Btu/(pulg2.s.°F)","",
        "in^2","Btu/(pulg2.s.°F)","s^-1","°F","°F"]

        self.lblSU = Label(self, text="Sistema de unidades", font=("Tahoma", 9))
        self.lblSU.place(x=40, y=10)

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
                for lbl in self.listunds4:
                    lbl.config(text=Internacional[i])
                    i += 1
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[4]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
                for entries in self.textos4:
                    entries.config(state=NORMAL)
                self.tipo_freno["state"] = "readonly"
                self.delta_T_textbox["state"] = "normal"
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
                for lbl in self.listunds4:
                    lbl.config(text=Ingles[i])
                    i += 1
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[4]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
                for entries in self.textos4:
                    entries.config(state=NORMAL)
                self.tipo_freno["state"] = "readonly"
                self.delta_T_textbox["state"] = "normal"
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        Label(self, text="Tipo de freno", font=("Tahoma", 9)).place(x=230, y=10)
        self.tipo_freno = Combobox(self, width=20, values=["Disco","Tambor","Cono"], state="disabled")
        def TipoFreno(event):
            if self.tipo_freno.get() == "Disco":
                for x in self.labels2:
                    x.destroy()
                for x in self.textos2:
                    x.destroy()
                self.labels2 = []
                textoslbl2 = ["D: Diametro externo","d: Diametro interno","t: Espesor"]
                for textos in textoslbl2:
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9)))
                i=360
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,3):
                    self.textos2.append(Entry(self))
                i=360
                for parameters in self.textos2:
                    parameters.place(x=400, y=i, width=60)
                    i += 30
            if self.tipo_freno.get() == "Tambor":
                for x in self.labels2:
                    x.destroy()
                for x in self.textos2:
                    x.destroy()
                self.labels2 = []
                textoslbl2 = ["L: Longitud del tambor","D: Diametro","t: Espesor"]
                for textos in textoslbl2:
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9)))
                i=360
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,3):
                    self.textos2.append(Entry(self))
                i=360
                for parameters in self.textos2:
                    parameters.place(x=400, y=i, width=60)
                    i += 30
            if self.tipo_freno.get() == "Cono":
                for x in self.labels2:
                    x.destroy()
                for x in self.textos2:
                    x.destroy()
                self.labels2 = []
                textoslbl2 = ["Rint: Radio interno mayor del cono","rint: Radio interno menor del cono", "h: Altura del cono","t: Espesor"]
                for textos in textoslbl2:
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9)))
                i=360
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,4):
                    self.textos2.append(Entry(self))
                i=360
                for parameters in self.textos2:
                    parameters.place(x=400, y=i, width=60)
                    i += 30
        self.tipo_freno.bind('<<ComboboxSelected>>', TipoFreno)
        self.tipo_freno.set("Disco")
        self.tipo_freno.place(x=230, y=30)


        self.labels = []
        textoslbl = ["Tamb: Temperatura ambiente","wi: Velocidad angular inicial","wf: Velocidad angular final",
        "I: Inercia rotatoria equivalente","gamma: Peso especifico del material del disco, tambor o cono",
        "C: Capacidad termica especifica","Veces que se activa","Tiempo de trabajo"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos, font=("Tahoma", 9)))
        i=90
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30

        self.textos = []
        for texto in range(0,8):
            self.textos.append(Entry(self, state="disabled"))
        i=90
        for parameters in self.textos:
            parameters.place(x=400, y=i, width=60)
            i += 30
        self.peso_especifico = Combobox(self, width=15, values=["Acero","Fundicion de hierro"], state="readonly")
        def peso_especifico(event):
            if self.peso_especifico.get() == "Acero":
                if self.list2.get() == "Sistema Internacional":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,76500)
                    self.textos[4]["state"] = "disabled"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,591.18)
                if self.list2.get() == "Sistema Ingles":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,0.282)
                    self.textos[4]["state"] = "disabled"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,0.12)
            if self.peso_especifico.get() == "Fundicion de hierro":
                if self.list2.get() == "Sistema Internacional":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,70600)
                    self.textos[4]["state"] = "disabled"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,591.18)
                if self.list2.get() == "Sistema Ingles":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,0.260)
                    self.textos[4]["state"] = "disabled"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,0.12)
        self.peso_especifico.bind('<<ComboboxSelected>>', peso_especifico)
        self.peso_especifico.place(x=520, y=210)

        self.listunds = []
        unds = ["°","rpm","rpm","kgm.m.s","N/m^3","Joule/(kgm.°C)","","horas"]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=90
        for unidades in self.listunds:
            unidades.place(x=470, y=i)
            i += 30


        self.labels2 = []
        textoslbl2 = ["D: Diametro externo","d: Diametro interno","t: Espesor"]
        for textos in textoslbl2:
            self.labels2.append(Label(self, text=textos, font=("Tahoma", 9)))
        i=360
        for cosas in self.labels2:
            cosas.place(x=40, y=i)
            i += 30

        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self, state="disabled"))
        i=360
        for parameters in self.textos2:
            parameters.place(x=400, y=i, width=60)
            i += 30

        self.listunds2 = []
        unds = ["mm","mm","mm"]
        for unidades in unds:
            self.listunds2.append(Label(self))
        i=360
        for unidades in self.listunds2:
            unidades.place(x=470, y=i)
            i += 30

        Button(self, text="Calcular ΔT", command=self.calculo_deltaT).place(x=490, y=90, height=20)

        self.delta_T = Label(self, text="ΔT")
        self.delta_T.place(x=750, y=10)
        self.delta_T_textbox = Entry(self, state="disabled")
        self.delta_T_textbox.place(x=770, y=10, width=60)

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'images\\hc y hr temperatura.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl_img1 = Label(self, image=self.img)
        self.lbl_img1.place(x=650, y=40, width=350, height=350)

        self.change_img_button = Button(self, text=">", command=self.change_graph)
        self.change_img_button.place(x=1010, y=150, width=30, height=30)

        self.labels3 = []
        textoslbl3 = ["hc: Coeficiente de transferencia térmica por convección","hr: Coeficiente de transferencia térmica por radiación",
        "FMC: Factor de modificación del coeficiente de transferencia térmica por convección"]
        for textos in textoslbl3:
            self.labels3.append(Label(self, text=textos, font=("Tahoma", 9)))
        i=400
        for cosas in self.labels3:
            cosas.place(x=530, y=i)
            i += 30

        self.textos3 = []
        for texto in range(0,3):
            self.textos3.append(Entry(self, state="disabled"))
        i=400
        for parameters in self.textos3:
            parameters.place(x=1020, y=i, width=60)
            i += 30

        self.listunds3 = []
        unds = ["Joule/(m2.s.°C)","Joule/(m2.s.°C)",""]
        for unidades in unds:
            self.listunds3.append(Label(self))
        i=400
        for unidades in self.listunds3:
            unidades.place(x=1090, y=i)
            i += 30

        Button(self, text="Calcular", command=self.calculoTmax).place(x=1020, y=500)

        self.labels4 = []
        textoslbl4 = ["A: Área de superficie disipadora de calor","U: Coeficiente de transferencia térmica global",
        "ß: Relación de tasa de transferencia de calor","Tmax: Temperatura máxima alcanzada por el freno o embrague",
        "Tmin: Temperatura mínima alcanzada por el freno o embrague"]
        for textos in textoslbl4:
            self.labels4.append(Label(self, text=textos, font=("Tahoma", 9)))
        i=600
        for cosas in self.labels4:
            cosas.place(x=40, y=i)
            i += 30

        self.textos4 = []
        for texto in range(0,5):
            self.textos4.append(Entry(self, state="disabled"))
        i=600
        for parameters in self.textos4:
            parameters.place(x=400, y=i, width=60)
            i += 30

        self.listunds4 = []
        unds = ["mm^2","Joule/(m^2.s.°C)","s^-1","°C","°C"]
        for unidades in unds:
            self.listunds4.append(Label(self))
        i=600
        for unidades in self.listunds4:
            unidades.place(x=470, y=i)
            i += 30




if __name__ == "__main__":
    root = Tk()
    root.wm_title("Calculos de validacion para frenos y embragues de zapata interna")
    base_path_3rd_part = pathlib.Path(__file__).parent.resolve()
    image_filename_3rd_part = "images\\Logo ANFRA.ico"
    icono = os.path.join(base_path_3rd_part, image_filename_3rd_part)
    root.iconbitmap(icono)
    TemperaturaWindow(root).mainloop()