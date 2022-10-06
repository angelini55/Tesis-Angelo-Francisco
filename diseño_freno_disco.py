import sys
sys.path.append("..")
import os
import pathlib
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from tkinter import ttk
from math import *
from PIL import ImageTk, Image
from views_analisis.Frenos_tambor_zapata_interna_dos import ZapataInternaWindow

class FrenoDiscoWindow_diseño(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1400, height=730)
        self.master = master
        self.pack()
        self.create_widget()
        self.contador = 1

    def guardar_calc(self):
        d = float(self.textos2[0].get())
        D = float(self.textos2[1].get())
        NS = float(self.textos2[2].get())

        F = self.textos3[0].get()
        FD = self.textos3[1].get()
        T = self.textos3[3].get()
        self.contenido = "d: {} \nD:{} \nNS: {}  \nF: {}\nFD: {} \nT: {}".format(d,D,NS,F,FD,T)

        if self.contador == 1:
            self.Caja1.delete("1.0","end")
            self.Caja1.insert("1.0",self.contenido)
            self.contador += 1
        elif self.contador == 2:
            self.Caja2.delete("1.0","end")
            self.Caja2.insert("1.0",self.contenido)
            self.contador += 1
        elif self.contador == 3:
            self.Caja3.delete("1.0","end")
            self.Caja3.insert("1.0",self.contenido)
            self.contador -=2

    # def ventana_analisis(self):
    #     new_window = ZapataInternaWindow(Toplevel())
    #     self.caja = Text(new_window)
    #     self.caja.place(x=800, y=550, height=150, width=100)
    #     self.caja.insert(1.0,self.Caja1.get(1.0,"end-1c"))

    def calc_diseño(self):
        n = float(self.textos[0].get())
        Fmax = float(self.textos[1].get())
        FD = float(self.textos[2].get())
        V_activa = float(self.textos[3].get())
        t = float(self.textos[4].get())
        I = float(self.textos[5].get())
        Tmax = float(self.textos[6].get())
        V_aire = float(self.textos[7].get())

        d = float(self.textos2[0].get())
        D = float(self.textos2[1].get())
        NS = float(self.textos2[2].get())
        
        Pa = float(self.txt18.get())
        µ = float(self.coef_friccion_textbox.get())

        Padm = Pa/FD
   
        T = ((pi*µ*Padm*NS)/12)*((D**3)-(d**3))
        T = round(T,2)
        if T < Tmax:
            self.labels_comprobacion[2].config(text="Cumple")
        else:
            self.labels_comprobacion[2].config(text="No Cumple")

        F = Padm*(pi/4)*((D**2)-(d**2))
        F = round(F,2)
        if F < Fmax:
            self.labels_comprobacion[0].config(text="Cumple")
        else:
            self.labels_comprobacion[0].config(text="No Cumple")

        FD_nuevo = Fmax/F
        FD_nuevo = round(FD_nuevo,2)
        if FD_nuevo > FD:
            self.labels_comprobacion[1].config(text="Cumple")
        else:
            self.labels_comprobacion[1].config(text="No Cumple")

        Padm_nueva = Pa/FD_nuevo


        self.textos3[0].delete(0,"end")
        self.textos3[0].insert(0,F)

        self.textos3[1].delete(0,"end")
        self.textos3[1].insert(0,FD_nuevo)

        self.textos3[2].delete(0,"end")
        self.textos3[2].insert(0,Padm_nueva)

        self.textos3[3].delete(0,"end")
        self.textos3[3].insert(0,T)        


    def create_widget(self):
        frame_inicializacion = Frame(self, width=1400, height=60, bg="#A9A9A9")
        frame_inicializacion.pack()

        frame_entrada_maquina = Frame(self, width=1400, height=260, bg="#808080")
        frame_entrada_maquina.pack()

        frame_entrada_parametros_geometricos = Frame(self, width=1400, height=410, bg="#C0C0C0")
        frame_entrada_parametros_geometricos.pack()

        Internacional = ["rpm","N","","","horas","kg.m^2/s","N.mm","m/s","mm","mm","","N","","MPa","N.mm"]
        Ingles = ["rpm","lb","","","horas","lb.ft^2/s","lb.in","ft/min","in","in","","lb","","PSI","lb.in"]

        self.lblSU = Label(self, text="Sistema de unidades", bg="#A9A9A9")
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
                self.lbl18_unidad.config(text="MPa")
                self.txt18["state"]=NORMAL
                self.list3["state"]="readonly"
                self.coef_friccion_textbox["state"]="normal"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
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
                self.lbl18_unidad.config(text="PSI")
                self.txt18["state"]=NORMAL
                self.list3["state"]="readonly"
                self.coef_friccion_textbox["state"]="normal"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                for entries in self.textos2:
                    entries.config(state=NORMAL)
                for entries in self.textos3:
                    entries.config(state=NORMAL)
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        self.labels = []
        textoslbl = ["n: Velocidad","Fmax: Carga maxima","FD: Factor minimo de diseño","Veces que se activa","t: Tiempo de trabajo",
        "I: Inercia rotatoria equivalente","Tmax: Torque maximo","Velocidad de flujo del aire"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos, bg="#808080"))
        i=70
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30
        
        self.listunds = []
        unds = ["rpm","N","","","horas","kg.m^2/s","N.mm","m/s"]
        for unidades in unds:
            self.listunds.append(Label(self, bg="#808080"))
        i=70
        for unidades in self.listunds:
            unidades.place(x=530, y=i)
            i += 30

        self.textos = []
        for texto in range(0,8):
            self.textos.append(Entry(self, state="disabled"))
        i=70
        for parameters in self.textos:
            parameters.place(x=460, y=i, width=60)
            i += 30

        self.labels2 = []
        textoslabels2 = ["d: Diámetro interno del disco de fricción",
        "D: Diámetro externo del disco de fricción","NS: Numero de superficies de fricción"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos, bg="#C0C0C0"))
        i=330
        for cosas in self.labels2:
            cosas.place(x=40, y=i)
            i += 30

        self.coef_friccion = Label(self, text="µ: Coeficiente de friccion", bg="#C0C0C0")
        self.coef_friccion.place(x=40, y=590)
        self.coef_friccion_textbox = Entry(self, state="disabled")
        self.coef_friccion_textbox.place(x=460, y=590, width=60)

        self.textos2 = []
        for texto in range(0,3):
            self.textos2.append(Entry(self, state="disabled"))
        i=330
        for parameters in self.textos2:
            parameters.place(x=460, y=i, width=60)
            i += 30

        self.listunds2 = []
        unds2 = ["mm","mm",""]
        for unidades in unds2:
            self.listunds2.append(Label(self, bg="#C0C0C0"))
        i=330
        for unidades in self.listunds2:
            unidades.place(x=530, y=i)
            i += 30

        self.labels3 = []
        textoslabels3 = ["F: Fuerza de accionamiento","Factor de diseño",
        "Padm: Presión máxima admisible ejercida sobre el material de fricción", "T: Torque debido a la fuerza de fricción"]
        for textos in textoslabels3:
            self.labels3.append(Label(self, text=textos))
        i=70
        for cosas in self.labels3:
            cosas.place(x=600, y=i)
            i += 30
        self.labels3[-1].place(x=600, y=250)

        self.labels_comprobacion = []
        for labels in range(0,3):
            self.labels_comprobacion.append(Label(self))
        i=70
        for labels in self.labels_comprobacion:
            labels.place(x=1090, y=i)
            i += 30
        self.labels_comprobacion[-1].place(x=1090, y=250)

        self.textos3 = []
        for texto in range(0,4):
            self.textos3.append(Entry(self, state="disabled"))
        i=70
        for parameters in self.textos3:
            parameters.place(x=980, y=i, width=60)
            i += 30
        self.textos3[-1].place(x=980, y=250)

        self.listunds3 = []
        unds3 = ["N","","MPa","N.mm"]
        for unidades in unds3:
            self.listunds3.append(Label(self, bg="#808080"))
        i=70
        for unidades in self.listunds3:
            unidades.place(x=1050, y=i)
            i += 30
        self.listunds3[-1].place(x=1050, y=250)

        self.coef_label = Label(self, text="Para el coeficiente de friccion", bg="#C0C0C0")
        self.coef_label.place(x=40, y=530)
        self.lista_coef = ["Con material de friccion"]
        self.list3 = Combobox(self, width=25, values=self.lista_coef, state="disabled")
        def cambio_coef(event):
            self.list5["state"]="readonly"
            self.coef_friccion_textbox["state"]="disabled"
        self.list3.bind('<<ComboboxSelected>>', cambio_coef)
        self.list3.place(x=40, y=550)

        self.lista_mat_friccion_label = Label(self, text="Material de friccion", bg="#C0C0C0")
        self.lista_mat_friccion_label.place(x=420, y=530)
        self.lista_mat_friccion = ["Fundicion de hierro","Metal sinterizado con tambor de acero","Metal sinterizado con tambor de fundicion de hierro",
        "Madera","Cuero","Corcho","Fieltro","Asbesto tejido","Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet",
        "Cuerda de asbesto arrollado","Tira de asbesto tejido","Algodón tejido","Papel resiliente"]
        self.list4 = Combobox(self, width=20, values=self.lista_mat_friccion, state="disabled")
        def Mat(event):
            base_path2 = pathlib.Path(__file__).parent.parent.resolve()
            nombre_bd = 'Tabla materiales de friccion.db'
            dbfile = os.path.join(base_path2, nombre_bd)
            conexion = sqlite3.connect(dbfile)
            cursor = conexion.cursor()
            if self.list5.get() == self.lista_humedo_seco[0]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.coef_friccion_textbox["state"]="normal"
                    self.coef_friccion_textbox.delete(0,"end")
                    self.coef_friccion_textbox.insert(0,coeficiente_dato)
                    self.coef_friccion_textbox["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Ingles WHERE Material_de_friccion='{self.list4.get()}' ")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.coef_friccion_textbox["state"]="normal"
                    self.coef_friccion_textbox.delete(0,"end")
                    self.coef_friccion_textbox.insert(0,coeficiente_dato)
                    self.coef_friccion_textbox["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            if self.list5.get() == self.lista_humedo_seco[1]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.coef_friccion_textbox["state"]="normal"
                    self.coef_friccion_textbox.delete(0,"end")
                    self.coef_friccion_textbox.insert(0,coeficiente_dato)
                    self.coef_friccion_textbox["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.coef_friccion_textbox["state"]="normal"
                    self.coef_friccion_textbox.delete(0,"end")
                    self.coef_friccion_textbox.insert(0,coeficiente_dato)
                    self.coef_friccion_textbox["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            conexion.close()
            #self.btn3["state"] = "disabled"
        self.list4.bind('<<ComboboxSelected>>', Mat)
        self.list4.place(x=420, y=550)

        self.lista_humedo_seco_lbl = Label(self, text="Tipo de ambiente", bg="#C0C0C0")
        self.lista_humedo_seco_lbl.place(x=240, y=530) 
        self.lista_humedo_seco = ["Ambiente humedo","Ambiente seco"]
        self.list5 = Combobox(self, width=20, values=self.lista_humedo_seco, state="disabled")
        def humedo_seco(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list4["state"]="readonly"
        self.list5.bind('<<ComboboxSelected>>', humedo_seco)
        self.list5.place(x=240, y=550)

        self.lbl18 = Label(self,text='Pa', bg="#C0C0C0")
        self.lbl18.place(x=650, y=550)
        self.txt18 = Entry(self, state="disabled")
        self.txt18.place(x=670, y=550, width=60)
        self.lbl18_unidad = Label(self, bg="#C0C0C0")
        self.lbl18_unidad.place(x=740, y=550)
        self.lbl36 = Label(self)
        self.lbl36.place(x=650, y=530)

        self.solve_button = Button(self, text="Calcular", command=self.calc_diseño)
        self.solve_button.place(x=950, y=650, width=50, height=50)
        self.record_button = Button(self, text="Guardar", command=self.guardar_calc)
        self.record_button.place(x=1000, y=650, width=50, height=50)

        self.Caja1 = Text(self)
        self.Caja1.place(x=720, y=380, height=150, width=100)
        self.Caja2 = Text(self)
        self.Caja2.place(x=840, y=380, height=150, width=100)
        self.Caja3 = Text(self)
        self.Caja3.place(x=960, y=380, height=150, width=100)

        self.boton_distancias_recomendadas = Button(self, text="Distancias recomendadas" )
        self.boton_distancias_recomendadas.place(x=40, y=650)

        # self.importar_analisis = Button(self, text="Importar", command=self.ventana_analisis)
        # self.importar_analisis.place(x=745, y=350)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Calculos de diseño para frenos y embragues de zapata interna")
    base_path_3rd_part = pathlib.Path(__file__).parent.parent.resolve()
    image_filename_3rd_part = "images\\Logo ANFRA.ico"
    icono = os.path.join(base_path_3rd_part, image_filename_3rd_part)
    root.iconbitmap(icono)
    FrenoDiscoWindow_diseño(root).mainloop()