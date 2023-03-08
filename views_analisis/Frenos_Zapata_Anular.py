import os
import sys

sys.path.append("..")
import pathlib
import sqlite3
from math import *
from tkinter import *
from tkinter import messagebox, ttk

from PIL import Image, ImageTk

from Temperatura_new import TemperaturaWindow

from tkinter.ttk import Combobox; PhotoImage; Combobox

from app_path import resource_path

class ZapataAnularWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1370, height=500)
        self.master = master
        self.pack()
        self.create_widget()

    def info(self):
        self.mensaje = """Programa que resuelve casos generales tomando en cuenta cada zapata individualmente y un sistema de referencia
que coincide con el pasador"""
        messagebox.showinfo(title="Aclaratoria", message=self.mensaje, parent=self)


    def tablaMaterial(self):
        try:
            self.table_window = Toplevel(width=1100, height=500)        
            self.generated_table = ttk.Treeview(self.table_window, columns=("col1","col2","col3","col4","col5","col6","col7"))
            self.generated_table.place(x=0, y=0, width=1100, height=400)
            self.generated_table.column("#0", width=100)
            self.generated_table.column("col1", width=90)
            self.generated_table.column("col2", width=100)
            self.generated_table.column("col3", width=100)
            self.generated_table.column("col4", width=100)
            self.generated_table.column("col5", width=100)
            self.generated_table.column("col6", width=100)

            if self.list2.get() == self.listaUnds[0]: 
                self.generated_table.heading("#0", text="Material de fricción", anchor=CENTER)
                self.generated_table.heading("col1", text="P máxima MPa", anchor=CENTER)
                self.generated_table.heading("col2", text="µ mínimo húmedo", anchor=CENTER)
                self.generated_table.heading("col3", text="µ mínimo seco", anchor=CENTER)
                self.generated_table.heading("col4", text="T máxima instantánea °C", anchor=CENTER)
                self.generated_table.heading("col5", text="T máxima continua °C", anchor=CENTER)
                self.generated_table.heading("col6", text="Velocidad máxima m/s", anchor=CENTER)
            if self.list2.get() == self.listaUnds[1]: 
                self.generated_table.heading("#0", text="Material de fricción", anchor=CENTER)
                self.generated_table.heading("col1", text="P máxima PSI", anchor=CENTER)
                self.generated_table.heading("col2", text="µ mínimo húmedo", anchor=CENTER)
                self.generated_table.heading("col3", text="µ mínimo seco", anchor=CENTER)
                self.generated_table.heading("col4", text="T máxima instantánea °F", anchor=CENTER)
                self.generated_table.heading("col5", text="T máxima continua °F", anchor=CENTER)
                self.generated_table.heading("col6", text="Velocidad máxima pie/min", anchor=CENTER)

            µ = float(self.textos[5].get())
            if not self.list5.get():
                raise ValueError

            base_path2 = pathlib.Path(__file__).parent.parent.resolve()
            nombre_bd = resource_path('images/Tabla materiales de friccion.db')
            dbfile = os.path.join(base_path2, nombre_bd)
            conexion = sqlite3.connect(dbfile)
            cursor = conexion.cursor()

            if self.list2.get() == self.listaUnds[0]:
                if self.list5.get() == self.lista_humedo_seco[0]:
                    cursor.execute(f"""SELECT 
                                            Presion_maxima,
                                            Coeficiente_de_friccion_minimo_humedo,
                                            Coeficiente_de_friccion_minimo_seco,
                                            Temperatura_maxima_instantanea,
                                            Temperatura_maxima_continua,
                                            Velocidad maxima
                                    FROM Internacional WHERE Coeficiente_de_friccion_minimo_humedo <='{µ}' """)
                if self.list5.get() == self.lista_humedo_seco[1]:
                    cursor.execute(f"""SELECT 
                                            Presion_maxima,
                                            Coeficiente_de_friccion_minimo_humedo,
                                            Coeficiente_de_friccion_minimo_seco,
                                            Temperatura_maxima_instantanea,
                                            Temperatura_maxima_continua,
                                            Velocidad maxima
                                    FROM Internacional WHERE Coeficiente_de_friccion_minimo_seco <='{µ}' """)
            if self.list2.get() == self.listaUnds[1]:
                if self.list5.get() == self.lista_humedo_seco[0]:
                    cursor.execute(f"""SELECT 
                                            Presion_maxima,
                                            Coeficiente_de_friccion_minimo_humedo,
                                            Coeficiente_de_friccion_minimo_seco,
                                            Temperatura_maxima_instantanea,
                                            Temperatura_maxima_continua,
                                            Velocidad maxima
                                    FROM Ingles WHERE Coeficiente_de_friccion_minimo_humedo <='{µ}'""")
                if self.list5.get() == self.lista_humedo_seco[1]:
                    cursor.execute(f"""SELECT 
                                            Presion_maxima,
                                            Coeficiente_de_friccion_minimo_humedo,
                                            Coeficiente_de_friccion_minimo_seco,
                                            Temperatura_maxima_instantanea,
                                            Temperatura_maxima_continua,
                                            Velocidad maxima
                                    FROM Ingles WHERE Coeficiente_de_friccion_minimo_seco <='{µ}'""")
            values = cursor.fetchall()
            if self.list5.get() == self.lista_humedo_seco[0]:
                cursor.execute(f"SELECT Material_de_friccion FROM Internacional WHERE Coeficiente_de_friccion_minimo_humedo <='{µ}'")
            if self.list5.get() == self.lista_humedo_seco[1]:
                cursor.execute(f"SELECT Material_de_friccion FROM Internacional WHERE Coeficiente_de_friccion_minimo_seco <='{µ}'")
            material = cursor.fetchall()
            i=0
            for elements in material:
                self.generated_table.insert("", END,text=elements, values=(values[i]))
                i+=1

            def selectItem(event):
                curItem = self.generated_table.focus()
                sas = self.generated_table.item(curItem)
                a12 = sas.get("values")[0]
                self.txttabla.delete(0,"end")
                self.txttabla.insert(0,a12)
                material = sas.get("text")
                self.lbl2.config(text=material)

            self.generated_table.bind('<ButtonRelease-1>', selectItem)

            self.lbl = Label(self.table_window,text='Pa')
            self.lbl.place(x=10, y=450, width=50, height=20)
            self.lbl2 = Label(self.table_window)
            self.lbl2.place(x=10, y=420, height=20)
            self.txttabla = Entry(self.table_window)
            self.txttabla.place(x=70, y=450, width=80, height=20)

            def set_mawp():
                mawp = float(self.txttabla.get())
                material = self.lbl2["text"]
                self.txt18.delete(0,"end")
                self.txt18.insert(0, mawp)
                self.lbl36.config(text=material)
                if mawp:
                    self.table_window.destroy()
                    return mawp 

            self.submit = Button(self.table_window, text="Insertar", command=set_mawp)
            self.submit.place(x=160, y=450)
        except:
            self.table_window.destroy()
            messagebox.showerror(title="Error", message="Completa la seccion de coeficiente de friccion para obtener un valor", parent=self)

    def vent_temp(self):
        vent = TemperaturaWindow(Toplevel())
        unidades = self.list2.get()
        material = self.lbl36["text"].strip("}{")
        ambiente = self.list5.get()
        tambor = self.list6.get()
        vent.list2.set(unidades)
        vent.list4.set(material)
        vent.list5.set(ambiente)
        vent.peso_especifico.set(tambor)
        vent.list2.event_generate('<<ComboboxSelected>>')
        vent.tipo_freno.set("Disco")
        vent.tipo_freno.event_generate('<<ComboboxSelected>>')
        vent.tipo_freno["state"] = "disabled"
        vent.list5.event_generate('<<ComboboxSelected>>')
        vent.list4.event_generate('<<ComboboxSelected>>')
        vent.peso_especifico.event_generate('<<ComboboxSelected>>')
        # Dext = self.textos[13].get()
        # Lt = self.textos[14].get()
        # t = self.textos[15].get()
        # vent.textos2[0].insert(0,Lt)
        # vent.textos2[1].insert(0,Dext)
        # vent.textos2[2].insert(0,t)

    def operacionesPadm(self):
        try:
            ri = float(self.textos[1].get())
            ro = float(self.textos[2].get())
            Θ1 = float(self.textos[3].get())
            Θ2 = float(self.textos[4].get())
            µ = float(self.textos[5].get())
            Padm = float(self.textos[0].get())
            Pa = float(self.txt18.get())

            if self.seleccion.get() == 1:
                
                F = (1/2)*(radians(Θ2-Θ1))*Padm*((ro**2)-(ri**2))
                F = round(F,2)
                T = (1/3)*µ*Padm*(radians(Θ2-Θ1))*((ro**3)-(ri**3))
                T = round(T,2)
                rprima = (2/3)*((((ro**3)-(ri**3)))/((ro**2)-(ri**2)))*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)

            if self.seleccion.get() == 2:

                F = (radians(Θ2-Θ1))*Padm*ri*(ro-ri)
                F = round(F,2)
                T = (1/2)*µ*Padm*ri*(radians(Θ2-Θ1))*((ro**2)-(ri**2))
                T = round(T,2)
                rprima = ((ro+ri)/2)*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)
            
            FD = Pa/Padm
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL) 
            
            self.textos2[0].delete(0,"end")
            self.textos2[0].insert(0,T)

            self.textos2[1].delete(0,"end")
            self.textos2[1].insert(0,F)

            self.textos2[2].delete(0,"end")
            self.textos2[2].insert(0,rprima)

            self.textos2[3].delete(0,"end")
            self.textos2[3].insert(0,FD)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros geométricos de la columna izquierda, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros de inicialización", parent=self)

    def operacionesT(self):
        try:
            ri = float(self.textos[1].get())
            ro = float(self.textos[2].get())
            Θ1 = float(self.textos[3].get())
            Θ2 = float(self.textos[4].get())
            µ = float(self.textos[5].get())
            T = float(self.textos[0].get())
            Pa = float(self.txt18.get())

            if self.seleccion.get() == 1:

                Padm = (3*T)/(µ*radians(Θ2-Θ1)*((ro**3)-(ri**3)))
                Padm = round(Padm,2)
                F = 0.5*radians(Θ2-Θ1)*Padm*((ro**2)-(ri**2))
                F = round(F,2)
                rprima = (2/3)*((((ro**3)-(ri**3)))/((ro**2)-(ri**2)))*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)

            if self.seleccion.get() == 2:

                Padm = (2*T)/(µ*ri*radians(Θ2-Θ1)*((ro**2)-(ri**2)))
                Padm = round(Padm,2)
                F = radians(Θ2-Θ1)*Padm*ri*(ro-ri)
                F = round(F,2)
                rprima = ((ro+ri)/2)*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)
            
            FD = Pa/Padm
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL) 

            self.textos2[0].delete(0,"end")
            self.textos2[0].insert(0,Padm)

            self.textos2[1].delete(0,"end")
            self.textos2[1].insert(0,F)

            self.textos2[2].delete(0,"end")
            self.textos2[2].insert(0,rprima)

            self.textos2[3].delete(0,"end")
            self.textos2[3].insert(0,FD)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los parámetros geométricos de la columna izquierda, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los parámetros de inicialización", parent=self)

    def operacionesF(self):
        try:
            ri = float(self.textos[1].get())
            ro = float(self.textos[2].get())
            Θ1 = float(self.textos[3].get())
            Θ2 = float(self.textos[4].get())
            µ = float(self.textos[5].get())
            F = float(self.textos[0].get())
            Pa = float(self.txt18.get())

            if self.seleccion.get() == 1:

                Padm = (2*F)/((radians(Θ2-Θ1))*((ro**2)-(ri**2)))
                Padm = round(Padm,2)
                T = (1/3)*µ*Padm*(radians(Θ2-Θ1))*((ro**3)-(ri**3))
                T = round(T,2)
                rprima = (2/3)*((((ro**3)-(ri**3)))/((ro**2)-(ri**2)))*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)

            if self.seleccion.get() == 2:

                Padm = (F)/((radians(Θ2-Θ1))*ri*(ro-ri))
                Padm = round(Padm,2)
                T = (1/2)*µ*Padm*ri*(radians(Θ2-Θ1))*((ro**2)-(ri**2))
                T = round(T,2)
                rprima = ((ro+ri)/2)*(((cos(radians(Θ1))-cos(radians(Θ2))))/radians(Θ2-Θ1))
                rprima = round(rprima,2)
            
            FD = Pa/Padm
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL)         
            
            self.textos2[0].delete(0,"end")
            self.textos2[0].insert(0,Padm)

            self.textos2[1].delete(0,"end")
            self.textos2[1].insert(0,T)

            self.textos2[2].delete(0,"end")
            self.textos2[2].insert(0,rprima)

            self.textos2[3].delete(0,"end")
            self.textos2[3].insert(0,FD)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los parámetros geométricos de la columna izquierda, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los parámetros de inicialización", parent=self)        

    def create_widget(self):

        frame_inicializacion = Frame(self, width=1370, height=195, bg="#A9A9A9")
        frame_inicializacion.pack()

        frame_entrada_freno = Frame(self, width=1370, height=305, bg="#808080")
        frame_entrada_freno.pack()

        self.raio_lbl = Label(self, text="Metodo de análisis", bg="#A9A9A9", font=("Tahoma", 9))
        self.raio_lbl.place(x=240, y=60)

        self.seleccion = IntVar()
        self.seleccion.set(1)
        self.radio1 = Radiobutton(self, text="Presión uniforme", variable=self.seleccion, value=1, bg="#A9A9A9", font=("Tahoma", 9))
        self.radio2 = Radiobutton(self, text="Desgaste uniforme", variable=self.seleccion, value=2, bg="#A9A9A9", font=("Tahoma", 9))

        self.radio1.place(x=240, y=80)
        self.radio2.place(x=240, y=100)

        self.labels = []
        textoslbl = ["T: Par de torsión del freno o embrague","ri: Radio interno de la zapata anular","ro: Radio externo de la zapata anular",
        "Θ1: Ángulo inicial del material de fricción","Θ2: Ángulo final del material de fricción","µ: Coeficiente de fricción dinámico del material de fricción"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos, bg="#808080", font=("Tahoma", 9)))
        i=200
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30
        
        self.textos = []
        for texto in range(0,6):
            self.textos.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos:
            parameters.place(x=460, y=i, width=60)
            i += 30

        self.listunds = []
        unds = ["N.m","m","m","°","°",""]
        for unidades in unds:
            self.listunds.append(Label(self, bg="#808080", font=("Tahoma", 9)))
        i=200
        for unidades in self.listunds:
            unidades.place(x=530, y=i)
            i += 30
        
        self.labels2 = []
        textoslabels2 = ["Padm: Presión máxima admisible ejercida sobre el material de fricción","F: Fuerza de accionamiento",
        "r': Ubicación de la línea de acción de la fuerza de accionamiento","FD: Factor de diseño"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos, bg="#808080", font=("Tahoma", 9)))
        i=200
        for cosas in self.labels2:
            cosas.place(x=570, y=i)
            i += 30

        self.textos2 = []
        for texto in range(0,4):
            self.textos2.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos2:
            parameters.place(x=950, y=i, width=60)
            i += 30

        self.listunds2 = []
        unds2 = ["Pa","N","m",""]
        for unidades in unds2:
            self.listunds2.append(Label(self, bg="#808080", font=("Tahoma", 9)))
        i=200
        for unidades in self.listunds2:
            unidades.place(x=1020, y=i)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.parent.resolve()
        self.image_filename =resource_path('images\\Freno Zapata Anular.png')
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((300,250), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=1070, y=0, height=250, width=300)

        self.boton1 = Button(self, text="Calcular", command=self.operacionesT)
        self.boton1.place(x=450, y=400, width=70, height=50)
        self.temp_button = Button(self, text="Calc.\ntemperatura", command=self.vent_temp)
        self.temp_button.place(x=870, y=400, width=75,height=50)

        self.lblSU = Label(self, text="Sistema de unidades", bg="#A9A9A9", font=("Tahoma", 9))
        self.lblSU.place(x=40, y=10)

        Internacional = ["N.mm","mm","mm","°","°","","MPa","N","mm",""]
        Ingles = ["lb.in","in","in","°","°","","PSI","lb","in",""]

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
                self.lbl18_unidad.config(text="MPa")
                self.txt18["state"]=NORMAL
                self.list["state"]="readonly"
                self.list3["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[5]["state"]="disabled"
                # for entries in self.textos2:
                #     entries.config(state=NORMAL)
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in self.listunds:
                    lbl.config(text=Ingles[i])
                    i += 1
                for lbl in self.listunds2:
                    lbl.config(text=Ingles[i])
                    i += 1
                self.lbl18_unidad.config(text="PSI")
                self.txt18["state"]=NORMAL
                self.list["state"]="readonly"
                self.list3["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[5]["state"]="disabled"
                # for entries in self.textos2:
                #     entries.config(state=NORMAL)
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        self.lbl_options = Label(self, text="Variables a calcular", bg="#A9A9A9")
        self.lbl_options.place(x=40, y=60)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="F: Fuerza de accionamiento")
                    self.labels2[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="T: Par de torsión del freno o embrague")
                    self.listunds[0].config(text="N")
                    self.listunds2[0].config(text="MPa")
                    self.listunds2[1].config(text="N.mm")
                    self.boton1.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="F: Fuerza de accionamiento")
                    self.labels2[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="T: Par de torsión del freno o embrague")
                    self.listunds[0].config(text="lb")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="T: Par de torsión del freno o embrague")
                    self.labels2[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="F: Fuerza de accionamiento")
                    self.listunds[0].config(text="N.mm")
                    self.listunds2[0].config(text="MPa")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="T: Par de torsión del freno o embrague")
                    self.labels2[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="F: Fuerza de accionamiento")
                    self.listunds[0].config(text="lb.in")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[0].config(text="T: Par de torsión del freno o embrague")
                    self.labels2[1].config(text="F: Fuerza de accionamiento")
                    self.listunds[0].config(text="MPa")
                    self.listunds2[0].config(text="N.mm")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[0].config(text="T: Par de torsión del freno o embrague")
                    self.labels2[1].config(text="F: Fuerza de accionamiento")
                    self.listunds[0].config(text="PSI")
                    self.listunds2[0].config(text="lb.in")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(1)
        self.list.place(x=40, y=80)

        self.coef_label = Label(self, text="Para el coeficiente de fricción", bg="#A9A9A9", font=("Tahoma", 9))
        self.coef_label.place(x=40, y=140)
        self.lista_coef = ["Con material de fricción","Ingresando valor"]
        self.list3 = Combobox(self, width=25, values=self.lista_coef, state="disabled")
        def cambio_coef(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list5["state"]="readonly"
                self.textos[5]["state"]="disabled"
            if self.list3.get() == self.lista_coef[1]:
                self.textos[5]["state"]="normal"
                self.list4["state"]="disabled"
                self.list5["state"]="readonly"
                self.btn3["state"] = "normal"
        self.list3.bind('<<ComboboxSelected>>', cambio_coef)
        self.list3.place(x=40, y=160)

        self.lista_mat_friccion_label = Label(self, text="Material de fricción", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_mat_friccion_label.place(x=420, y=140)
        self.lista_mat_friccion = ["Fundición de hierro","Metal sinterizado con tambor de acero","Metal sinterizado con tambor de fundición de hierro",
        "Madera","Cuero","Corcho","Fieltro","Asbesto tejido","Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet","Cuerda de asbesto arrollado",
        "Tira de asbesto tejido","Algodón tejido","Papel resiliente"]
        self.list4 = Combobox(self, width=20, values=self.lista_mat_friccion, state="disabled")
        def Mat(event):
            base_path2 = pathlib.Path(__file__).parent.parent.resolve()
            nombre_bd = resource_path('images/Tabla materiales de friccion.db')
            dbfile = os.path.join(base_path2, nombre_bd)
            conexion = sqlite3.connect(dbfile)
            cursor = conexion.cursor()
            if self.list5.get() == self.lista_humedo_seco[0]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[5]["state"]="normal"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,coeficiente_dato)
                    self.textos[5]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Ingles WHERE Material_de_friccion='{self.list4.get()}' ")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[5]["state"]="normal"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,coeficiente_dato)
                    self.textos[5]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            if self.list5.get() == self.lista_humedo_seco[1]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[5]["state"]="normal"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,coeficiente_dato)
                    self.textos[5]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[5]["state"]="normal"
                    self.textos[5].delete(0,"end")
                    self.textos[5].insert(0,coeficiente_dato)
                    self.textos[5]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            conexion.close()
            self.btn3["state"] = "disabled"
            self.list6["state"] = "readonly"
            if self.list4.get() == "Fundición de hierro" or self.list4.get() == "Metal sinterizado con tambor de fundición de hierro":
                self.list6.set("Fundición de hierro")
                self.list6["state"] = "disabled"
            elif self.list4.get() == "Grafito de carbono" or self.list4.get() == "Metal sinterizado con tambor de acero":
                self.list6.set("Acero")
                self.list6["state"] = "disabled"
        self.list4.bind('<<ComboboxSelected>>', Mat)
        self.list4.place(x=420, y=160)

        self.lista_mat_tambor_lbl = Label(self, text="Material del tambor", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_mat_tambor_lbl.place(x=590, y=140)
        self.lista_mat_tambor = ["Fundición de hierro", "Acero"]     
        self.list6 = Combobox(self, width=20, values=self.lista_mat_tambor, state="disabled")
        self.list6.place(x=590, y=160)

        self.lista_humedo_seco_lbl = Label(self, text="Tipo de ambiente", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_humedo_seco_lbl.place(x=240, y=140) 
        self.lista_humedo_seco = ["Ambiente húmedo","Ambiente seco"]
        self.list5 = Combobox(self, width=20, values=self.lista_humedo_seco, state="disabled")
        def humedo_seco(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list4["state"]="readonly"
        self.list5.bind('<<ComboboxSelected>>', humedo_seco)
        self.list5.place(x=240, y=160)

        self.lbl18 = Label(self,text='Pa', bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl18.place(x=700, y=80)
        self.txt18 = Entry(self, state="disabled")
        self.txt18.place(x=720, y=80, width=60)
        self.lbl18_unidad = Label(self)
        self.lbl18_unidad.place(x=790, y=80)
        self.lbl36 = Label(self)
        self.lbl36.place(x=700, y=60)

        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn3.place(x=820, y=80, width=40, height=40)
        # self.info_button = Button(self, text="!", bg="yellow", command=self.info)
        # self.info_button.place(x=240, y=30, width=25, height=25)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    ZapataAnularWindow(root).mainloop()