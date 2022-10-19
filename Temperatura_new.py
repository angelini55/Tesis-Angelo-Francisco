import os
import pathlib
import sqlite3
from math import *
from tkinter import *
from tkinter.ttk import Combobox

from PIL import Image, ImageTk


class TemperaturaWindow(Frame):

    def __init__(self, master):
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
            self.lbl_img1.place(x=750, y=40, width=350, height=350)
        else:
            self.image_filename = 'images\\hc y hr temperatura.png'
            self.base_path = pathlib.Path(__file__).parent.resolve()
            self.image = Image.open(os.path.join(self.base_path, self.image_filename))
            self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
            self.img = ImageTk.PhotoImage(self.image)
            self.lbl_img1 = Label(self, image=self.img)
            self.lbl_img1.place(x=750, y=40, width=350, height=350)
    
    def calculo_deltaT(self):
        Tamb = float(self.textos[0].get())
        wi = float(self.textos[1].get())
        wf = float(self.textos[2].get())
        I = float(self.textos[3].get())
        gamma = float(self.textos[4].get())
        C = float(self.textos[5].get())
        V_activa = float(self.textos[6].get())
        Tt = float(self.textos[7].get())
        V = float(self.textos[8].get())

        if self.list2.get() == "Sistema Internacional":
            E = (I/204.10)*abs(((wi*(2*pi/60))**2)-((wf*(2*pi/60))**2))
            V = V*3.28084
        else:
            E = (I/18672)*abs(((wi*(2*pi/60))**2)-((wf*(2*pi/60))**2))

        if self.tipo_freno.get() == "Disco":
            D = float(self.textos2[0].get())
            d = float(self.textos2[1].get())
            t = float(self.textos2[2].get())
            W = (pi/4)*((D**2)-(d**2)*t*gamma)
        elif self.tipo_freno.get() == "Tambor":
            L = float(self.textos2[0].get())
            D = float(self.textos2[1].get())
            t = float(self.textos2[2].get())
            W = pi*D*L*t*gamma
        else:
            Ri = float(self.textos2[0].get())
            ri = float(self.textos2[1].get())
            h = float(self.textos2[2].get())
            t = float(self.textos2[3].get())
            W = (pi/3)*h*((((Ri+t)**3)-((ri+t)**3)/Ri-ri)-((Ri**3)-(ri**3)/Ri-ri))*gamma

        deltaT = E/(W*C)
        if self.list2.get() == "Sistema Internacional":
            deltaT = (deltaT*(9/5))+32
        deltaT = round(deltaT,2)

        self.delta_T_textbox.delete(0,"end")
        self.delta_T_textbox.insert(0,deltaT)

        hc = log(deltaT,13.74)
        hc = hc*(10**-6)
        hc = round(hc,8)

        hr = 1.95*exp((2.38*(10**-3))*deltaT)
        hr = hr*(10**-6)
        hr = round(hr, 8)

        FMC = (4.24107*(10**-9))*(V**5) - (1.13467*(10**-6))*(V**4) + (1.20833*(10**-4))*(V**3) - (7.33185*(10**-3))*(V**2) + 0.306702*(V)+ 0.1
        FMC = round(FMC,2)

        self.textos3[0].delete(0,"end")
        self.textos3[0].insert(0,hc)

        self.textos3[1].delete(0,"end")
        self.textos3[1].insert(0,hr)

        self.textos3[2].delete(0,"end")
        self.textos3[2].insert(0,FMC)    

        U = hr + FMC*hc

        if self.tipo_freno.get() == "Disco":
            D = float(self.textos2[0].get())
            d = float(self.textos2[1].get())
            A = (pi/4)*((D**2)-(d**2))
            A = round(A,2)
        elif self.tipo_freno.get() == "Tambor":
            L = float(self.textos2[0].get())
            D = float(self.textos2[1].get())
            A = pi*D*L
            A = round(A,2)
        else:
            Ri = float(self.textos2[0].get())
            ri = float(self.textos2[1].get())
            h = float(self.textos2[2].get())
            A = pi*h*(Ri+ri)
            A = round(A,2)

        ß = (U*A)/(W*C)
        Ita = (Tt/V_activa)*3600

        Tmax = Tamb + (deltaT)/(1-(e**(-ß*Ita)))
        if float(self.temp_text.get()) > Tmax:
            self.comprobacion_lbl["text"] = "El material resiste la \ntemperatura máxima de trabajo"
        else:
            self.comprobacion_lbl["text"] = "El material no resiste la \ntemperatura máxima de trabajo"
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

        frame_inicializacion = Frame(self, width=1200, height=550, bg="#A9A9A9")
        frame_inicializacion.pack()

        frame_entrada_temp = Frame(self, width=1200, height=210, bg="#808080")
        frame_entrada_temp.pack()

        Internacional = ["°C","rpm","rpm","kgm.m.s","N/m^3","Joule/(kgm.°C)","","horas","m/s","mm","mm","mm","Joule/(m2.s.°C)","Joule/(m2.s.°C)","",
        "mm^2","Joule/(m^2.s.°C)","s^-1","°C","°C"]
        Ingles = ["°F","rpm","rpm","lbm.pulg.s","lb/pulg^3","Btu/(lbm.°F)","","horas","pie/s","in","in","in","Btu/(pulg2.s.°F)","Btu/(pulg2.s.°F)","",
        "in^2","Btu/(pulg2.s.°F)","s^-1","°F","°F"]

        self.lblSU = Label(self, text="Sistema de unidades", font=("Tahoma", 9), bg="#A9A9A9")
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
                self.temp_und["text"] = "°C"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[4]["state"]="disabled"
                self.textos[5]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
                for entries in self.textos4:
                    entries.config(state=NORMAL)
                self.tipo_freno["state"] = "readonly"
                self.delta_T_textbox["state"] = "normal"
                self.peso_especifico["state"] = "readonly"
                self.list5["state"] = "readonly"
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
                self.temp_und["text"] = "°F"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[4]["state"]="disabled"
                self.textos[5]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
                for entries in self.textos4:
                    entries.config(state=NORMAL)
                self.tipo_freno["state"] = "readonly"
                self.delta_T_textbox["state"] = "normal"
                self.peso_especifico["state"] = "readonly"
                self.list5["state"] = "readonly"
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        Label(self, text="Tipo de freno", font=("Tahoma", 9), bg="#A9A9A9").place(x=230, y=10)
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
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
                i=390
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,3):
                    self.textos2.append(Entry(self))
                i=390
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
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
                i=390
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,3):
                    self.textos2.append(Entry(self))
                i=390
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
                    self.labels2.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
                i=390
                for cosas in self.labels2:
                    cosas.place(x=40, y=i)
                    i += 30

                self.textos2 = []
                for texto in range(0,4):
                    self.textos2.append(Entry(self))
                i=390
                for parameters in self.textos2:
                    parameters.place(x=400, y=i, width=60)
                    i += 30
        self.tipo_freno.bind('<<ComboboxSelected>>', TipoFreno)
        self.tipo_freno.set("Disco")
        self.tipo_freno.place(x=230, y=30)


        self.labels = []
        textoslbl = ["Tamb: Temperatura ambiente","wi: Velocidad angular inicial","wf: Velocidad angular final",
        "I: Inercia rotatoria equivalente","γ: Peso especifico del material del disco, tambor o cono",
        "C: Capacidad termica especifica","Veces que se activa","Tiempo de trabajo","V: Velocidad del aire"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
        i=90
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30

        self.textos = []
        for texto in range(0,9):
            self.textos.append(Entry(self, state="disabled"))
        i=90
        for parameters in self.textos:
            parameters.place(x=400, y=i, width=60)
            i += 30
        self.peso_especifico = Combobox(self, width=15, values=["Acero","Fundicion de hierro"], state="disabled")
        def peso_especifico(event):
            self.capacidad_termica["state"] = "readonly"
            if self.peso_especifico.get() == "Acero":
                if self.list2.get() == "Sistema Internacional":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,76500)
                    self.textos[4]["state"] = "disabled"
                if self.list2.get() == "Sistema Ingles":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,0.282)
                    self.textos[4]["state"] = "disabled"
            if self.peso_especifico.get() == "Fundicion de hierro":
                if self.list2.get() == "Sistema Internacional":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,70600)
                    self.textos[4]["state"] = "disabled"
                if self.list2.get() == "Sistema Ingles":
                    self.textos[4]["state"] = "normal"
                    self.textos[4].delete(0,"end")
                    self.textos[4].insert(0,0.260)
                    self.textos[4]["state"] = "disabled"
        self.peso_especifico.bind('<<ComboboxSelected>>', peso_especifico)
        self.peso_especifico.place(x=560, y=210)

        self.capacidad_termica = Combobox(self, width=15, values=["Valor predeterminado","Ingresar valor"],state="disabled")
        def capacidad_termica(event):
            if self.capacidad_termica.get() == "Ingresar valor":
                self.textos[5]["state"]="normal"
            else:
                if self.peso_especifico.get() == "Acero":
                    if self.list2.get() == "Sistema Internacional":
                        self.textos[5]["state"] = "normal"
                        self.textos[5].delete(0,"end")
                        self.textos[5].insert(0,591.18)
                        self.textos[5]["state"] = "disabled"
                    if self.list2.get() == "Sistema Ingles":
                        self.textos[5]["state"] = "normal"
                        self.textos[5].delete(0,"end")
                        self.textos[5].insert(0,0.12)
                        self.textos[5]["state"] = "disabled"
                if self.peso_especifico.get() == "Fundicion de hierro":
                    if self.list2.get() == "Sistema Internacional":
                        self.textos[5]["state"] = "normal"
                        self.textos[5].delete(0,"end")
                        self.textos[5].insert(0,591.18)
                        self.textos[5]["state"] = "disabled"
                    if self.list2.get() == "Sistema Internacional":
                        self.textos[5]["state"] = "normal"
                        self.textos[5].delete(0,"end")
                        self.textos[5].insert(0,0.12)
                        self.textos[5]["state"] = "disabled"
        self.capacidad_termica.bind('<<ComboboxSelected>>', capacidad_termica)
        self.capacidad_termica.place(x=560, y=240)

        self.listunds = []
        unds = ["°","rpm","rpm","kgm.m.s","N/m^3","Joule/(kgm.°C)","","horas","m/s"]
        for unidades in unds:
            self.listunds.append(Label(self, bg="#A9A9A9"))
        i=90
        for unidades in self.listunds:
            unidades.place(x=470, y=i)
            i += 30


        self.labels2 = []
        textoslbl2 = ["D: Diametro externo","d: Diametro interno","t: Espesor"]
        for textos in textoslbl2:
            self.labels2.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
        i=390
        for cosas in self.labels2:
            cosas.place(x=40, y=i)
            i += 30

        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self, state="disabled"))
        i=390
        for parameters in self.textos2:
            parameters.place(x=400, y=i, width=60)
            i += 30

        self.listunds2 = []
        unds = ["mm","mm","mm"]
        for unidades in unds:
            self.listunds2.append(Label(self, bg="#A9A9A9"))
        i=390
        for unidades in self.listunds2:
            unidades.place(x=470, y=i)
            i += 30

        #Button(self, text="Calcular ΔT", command=self.calculo_deltaT).place(x=490, y=90, height=20)

        self.delta_T = Label(self, text="ΔT", bg="#A9A9A9")
        self.delta_T.place(x=750, y=10)
        self.delta_T_textbox = Entry(self, state="disabled")
        self.delta_T_textbox.place(x=770, y=10, width=60)

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'images\\hc y hr temperatura.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl_img1 = Label(self, image=self.img)
        self.lbl_img1.place(x=750, y=40, width=350, height=350)

        self.change_img_button = Button(self, text=">", command=self.change_graph)
        self.change_img_button.place(x=1110, y=150, width=30, height=30)

        self.labels3 = []
        textoslbl3 = ["hc: Coeficiente de transferencia térmica por convección","hr: Coeficiente de transferencia térmica por radiación",
        "FMC: Factor de modificación del coeficiente de transferencia térmica por convección"]
        for textos in textoslbl3:
            self.labels3.append(Label(self, text=textos, font=("Tahoma", 9), bg="#A9A9A9"))
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
            self.listunds3.append(Label(self, bg="#A9A9A9"))
        i=400
        for unidades in self.listunds3:
            unidades.place(x=1090, y=i)
            i += 30

        Button(self, text="Calcular", command=self.calculo_deltaT).place(x=200, y=500, height=50, width=80)

        self.labels4 = []
        textoslbl4 = ["A: Área de superficie disipadora de calor","U: Coeficiente de transferencia térmica global",
        "ß: Relación de tasa de transferencia de calor","Tmax: Temperatura máxima alcanzada por el freno o embrague",
        "Tmin: Temperatura mínima alcanzada por el freno o embrague"]
        for textos in textoslbl4:
            self.labels4.append(Label(self, text=textos, font=("Tahoma", 9), bg="#808080"))
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
            self.listunds4.append(Label(self, bg="#808080"))
        i=600
        for unidades in self.listunds4:
            unidades.place(x=470, y=i)
            i += 30

        self.temp_lbl = Label(self, text="Temperatura maxima instantanea", font=("Tahoma", 9), bg="#A9A9A9")
        self.temp_lbl.place(x=530, y=490)
        self.temp_text = Entry(self)
        self.temp_text.place(x=1020, y=490, width=60)
        self.temp_und = Label(self, font=("Tahoma", 9), bg="#A9A9A9")
        self.temp_und.place(x=1090, y=490)

        self.comprobacion_lbl = Label(self, font=("Tahoma", 9), bg="#A9A9A9")
        self.comprobacion_lbl.place(x=1020, y=510)

        self.lista_humedo_seco_lbl = Label(self, text="Tipo de ambiente", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_humedo_seco_lbl.place(x=540, y=90) 
        self.lista_humedo_seco = ["Ambiente humedo","Ambiente seco"]
        self.list5 = Combobox(self, width=20, values=self.lista_humedo_seco, state="disabled")
        def humedo_seco(event):
            #if self.list3.get() == self.lista_coef[0]:
                self.list4["state"]="readonly"
        self.list5.bind('<<ComboboxSelected>>', humedo_seco)
        self.list5.place(x=540, y=110)

        self.lista_mat_friccion_label = Label(self, text="Material de friccion", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_mat_friccion_label.place(x=540, y=140)
        self.lista_mat_friccion = ["Fundicion de hierro","Metal sinterizado con tambor de acero","Metal sinterizado con tambor de fundicion de hierro",
        "Madera","Cuero","Corcho","Fieltro","Asbesto tejido","Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet","Cuerda de asbesto arrollado",
        "Tira de asbesto tejido","Algodón tejido","Papel resiliente"]
        self.list4 = Combobox(self, width=20, values=self.lista_mat_friccion, state="disabled")
        def Mat(event):
            base_path2 = pathlib.Path(__file__).parent.resolve()
            nombre_bd = 'Tabla materiales de friccion.db'
            dbfile = os.path.join(base_path2, nombre_bd)
            conexion = sqlite3.connect(dbfile)
            cursor = conexion.cursor()
            if self.list5.get() == self.lista_humedo_seco[0]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Temperatura_maxima_continua FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    temp_maxima = cursor.fetchone()
                    # cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    # presion_maxima_dato = cursor.fetchone()
                    # self.textos[1]["state"]="normal"
                    # self.textos[1].delete(0,"end")
                    # self.textos[1].insert(0, coeficiente_dato)
                    # self.textos[1]["state"]="disabled"

                    self.temp_text.delete(0,"end")
                    self.temp_text.insert(0, temp_maxima)
                    # self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Temperatura_maxima_continua FROM Ingles WHERE Material_de_friccion='{self.list4.get()}' ")
                    temp_maxima = cursor.fetchone()
                    # cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    # presion_maxima_dato = cursor.fetchone()
                    # self.textos[1]["state"]="normal"
                    # self.textos[1].delete(0,"end")
                    # self.textos[1].insert(0, coeficiente_dato)
                    # self.textos[1]["state"]="disabled"

                    self.temp_text.delete(0,"end")
                    self.temp_text.insert(0, temp_maxima)
                    # self.lbl36.config(text=self.list4.get())
            if self.list5.get() == self.lista_humedo_seco[1]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Temperatura_maxima_continua FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    temp_maxima = cursor.fetchone()
                    # cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    # presion_maxima_dato = cursor.fetchone()
                    # self.textos[1]["state"]="normal"
                    # self.textos[1].delete(0,"end")
                    # self.textos[1].insert(0, coeficiente_dato)
                    # self.textos[1]["state"]="disabled"

                    self.temp_text.delete(0,"end")
                    self.temp_text.insert(0, temp_maxima)
                    # self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Temperatura_maxima_continua FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    temp_maxima = cursor.fetchone()
                    # cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    # presion_maxima_dato = cursor.fetchone()
                    # self.textos[1]["state"]="normal"
                    # self.textos[1].delete(0,"end")
                    # self.textos[1].insert(0, coeficiente_dato)
                    # self.textos[1]["state"]="disabled"

                    self.temp_text.delete(0,"end")
                    self.temp_text.insert(0, temp_maxima)
                    # self.lbl36.config(text=self.list4.get())
            conexion.close()
        self.list4.bind('<<ComboboxSelected>>', Mat)
        self.list4.place(x=540, y=160)


if __name__ == "__main__":
    root = Tk()
    root.wm_title("Calculos de validacion para frenos y embragues de zapata interna")
    base_path_3rd_part = pathlib.Path(__file__).parent.resolve()
    image_filename_3rd_part = "images\\Logo ANFRA.ico"
    icono = os.path.join(base_path_3rd_part, image_filename_3rd_part)
    root.iconbitmap(icono)
    TemperaturaWindow(root).mainloop()