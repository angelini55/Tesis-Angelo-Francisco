import os
import sqlite3
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class CircularWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1000, height=630)
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
            self.generated_table.heading("#0", text="Material de friccion", anchor=CENTER)
            self.generated_table.heading("col1", text="P maxima MPa", anchor=CENTER)
            self.generated_table.heading("col2", text="µ minimo humedo", anchor=CENTER)
            self.generated_table.heading("col3", text="µ minimo seco", anchor=CENTER)
            self.generated_table.heading("col4", text="T maxima instantanea °C", anchor=CENTER)
            self.generated_table.heading("col5", text="T maxima continua °C", anchor=CENTER)
            self.generated_table.heading("col6", text="Velocidad maxima m/s", anchor=CENTER)
        if self.list2.get() == self.listaUnds[1]: 
            self.generated_table.heading("#0", text="Material de friccion", anchor=CENTER)
            self.generated_table.heading("col1", text="P maxima PSI", anchor=CENTER)
            self.generated_table.heading("col2", text="µ minimo humedo", anchor=CENTER)
            self.generated_table.heading("col3", text="µ minimo seco", anchor=CENTER)
            self.generated_table.heading("col4", text="T maxima instantanea °F", anchor=CENTER)
            self.generated_table.heading("col5", text="T maxima continua °F", anchor=CENTER)
            self.generated_table.heading("col6", text="Velocidad maxima pie/min", anchor=CENTER)

        µ = float(self.textos[3].get())

        base_path2 = pathlib.Path(__file__).parent.resolve()
        nombre_bd = 'Tabla materiales de friccion.db'
        dbfile = os.path.join(base_path2, nombre_bd)
        conexion = sqlite3.connect(dbfile)
        cursor = conexion.cursor()

        if self.list2.get() == self.listaUnds[0]:
            cursor.execute(f"""SELECT 
                                        Presion_maxima,
                                        Coeficiente_de_friccion_minimo_humedo,
                                        Coeficiente_de_friccion_minimo_seco,
                                        Temperatura_maxima_instantanea,
                                        Temperatura_maxima_continua,
                                        Velocidad maxima
                                FROM Internacional WHERE Coeficiente_de_friccion_minimo_humedo >'{µ}' OR Coeficiente_de_friccion_minimo_seco >'{µ}'""")
        if self.list2.get() == self.listaUnds[1]:
            cursor.execute(f"""SELECT 
                                        Presion_maxima,
                                        Coeficiente_de_friccion_minimo_humedo,
                                        Coeficiente_de_friccion_minimo_seco,
                                        Temperatura_maxima_instantanea,
                                        Temperatura_maxima_continua,
                                        Velocidad maxima
                                FROM Ingles WHERE Coeficiente_de_friccion_minimo_humedo >'{µ}' OR Coeficiente_de_friccion_minimo_seco >'{µ}'""")
        values = cursor.fetchall()
        cursor.execute(f"SELECT Material_de_friccion FROM Internacional WHERE Coeficiente_de_friccion_minimo_humedo>'{µ}' OR Coeficiente_de_friccion_minimo_seco>'{µ}'")
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
        self.lbl2.place(x=10, y=420, width=150, height=20)
        self.txttabla = Entry(self.table_window)
        self.txttabla.place(x=70, y=450, width=80, height=20)

        def set_mawp():
            mawp = float(self.txttabla.get())
            mawp = mawp*1000
            material = self.lbl2["text"]
            self.txt18.delete(0,"end")
            self.txt18.insert(0, mawp)
            self.lbl36.config(text=material)
            if mawp:
                self.table_window.destroy()
                return mawp 

        self.submit = Button(self.table_window, text="Insertar", command=set_mawp)
        self.submit.place(x=160, y=450)

    def CalcFD(self):
        if self.list2.get() == self.listaUnds[0]:
            Pa = float(self.txt18.get())*1000
        else:
            Pa = float(self.txt18.get())
        if self.list.get() == self.opciones[2]:
            Fdiseño = Pa/float(self.textos[0].get())
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
        R = float(self.textos[2].get())
        valor_tabla = float(self.textos[1].get())
        Padm = float(self.textos[0].get())
        µ = float(self.textos[3].get())

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[0]:
            r = valor_tabla
            Interpolation_string = "Rr"
            Rr = R/r
            self._interpolation(Interpolation_string,Rr)
            alpha = self.interpolation_results["alpha"]
            beta = self.interpolation_results["beta"]
            
            Pprom = alpha*Padm
            F = pi*(R**2)*Pprom
            T = µ*F*beta*r

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[1]:     
            alpha = valor_tabla
            Interpolation_string = "alpha"
            self._interpolation(Interpolation_string,alpha)
            Rr = self.interpolation_results["Rr"]
            beta = self.interpolation_results["beta"]

            Pprom = alpha*Padm
            F = pi*(R**2)*Pprom
            T = µ*F*beta*(R/Rr)
        
        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[2]:
            beta = valor_tabla
            Interpolation_string = "beta"
            self._interpolation(Interpolation_string,beta)
            Rr = self.interpolation_results["Rr"]
            alpha = self.interpolation_results["alpha"]

            Pprom = alpha*Padm
            F = pi*(R**2)*Pprom
            T = µ*F*beta*(R/Rr)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,F)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)


    def operacionesT(self):
        R = float(self.textos[2].get())
        valor_tabla = float(self.textos[1].get())
        T = float(self.textos[0].get())
        µ = float(self.textos[3].get())

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[0]:
            r = valor_tabla
            Interpolation_string = "Rr"
            Rr = R/r
            self._interpolation(Interpolation_string,Rr)
            alpha = self.interpolation_results["alpha"]
            beta = self.interpolation_results["beta"]
            
            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            F = T/(µ*beta*r)

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[1]:     
            alpha = valor_tabla
            Interpolation_string = "alpha"
            self._interpolation(Interpolation_string,alpha)
            Rr = self.interpolation_results["Rr"]
            beta = self.interpolation_results["beta"]

            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            F = T/(µ*beta*r)
        
        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[2]:
            beta = valor_tabla
            Interpolation_string = "beta"
            self._interpolation(Interpolation_string,beta)
            Rr = self.interpolation_results["Rr"]
            alpha = self.interpolation_results["alpha"]

            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            F = T/(µ*beta*r)
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,F)

    def operacionesF(self):
        R = float(self.textos[2].get())
        valor_tabla = float(self.textos[1].get())
        F = float(self.textos[0].get())
        µ = float(self.textos[3].get())

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[0]:
            r = valor_tabla
            Interpolation_string = "Rr"
            Rr = R/r
            self._interpolation(Interpolation_string,Rr)
            alpha = self.interpolation_results["alpha"]
            beta = self.interpolation_results["beta"]
            
            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            T = µ*F*beta*(R/Rr)

        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[1]:     
            alpha = valor_tabla
            Interpolation_string = "alpha"
            self._interpolation(Interpolation_string,alpha)
            Rr = self.interpolation_results["Rr"]
            beta = self.interpolation_results["beta"]

            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            T = µ*F*beta*(R/Rr)
        
        if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[2]:
            beta = valor_tabla
            Interpolation_string = "beta"
            self._interpolation(Interpolation_string,beta)
            Rr = self.interpolation_results["Rr"]
            alpha = self.interpolation_results["alpha"]

            Pprom = F/(pi*(R**2))
            Padm = Pprom/alpha
            T = µ*F*beta*(R/Rr)
        
        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)
        

    def create_widget(self):

        self.labels = []
        textoslbl = ["Padm","r'","R","µ"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=70
        for cosas in self.labels:
            cosas.place(x=10, y=i, width=60, height=20)
            i += 30
        
        self.textos = []
        for texto in range(0,4):
            self.textos.append(Entry(self, state="disabled"))
        i=70
        for parameters in self.textos:
            parameters.place(x=70, y=i, width=80)
            i += 30

        self.listunds = []
        unds = ["Pa","m","m",""]
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
            self.textos2.append(Entry(self, state="disabled"))
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
        self.lbl17.place(x=700, y=10, height=250, width=300)

        self.boton1 = Button(self, text="Solve", command=self.operacionesPadm)
        self.boton1.place(x=450, y=300, width=100, height=80)

        self.lblSU = Label(self, text="Sistema de unidades")
        self.lblSU.place(x=215, y=15, width=120, height=20)

        Internacional = ["Pa","m","m","","N","N.m",""]
        Ingles = ["PSI","in","in","","lb","lb.in",""]

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
                self.list_interpolation_table["state"]="readonly"
                self.list3["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[3]["state"]="disabled"
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
                self.list_interpolation_table["state"]="readonly"
                self.list3["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[3]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)

        self.list2.place(x=215, y=35)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[0].config(text="N")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N.m")
                    self.boton1.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="F")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="T")
                    self.listunds[0].config(text="lb")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb.in")
                    self.boton1.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[0].config(text="N.m")
                    self.listunds2[0].config(text="Pa")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="T")
                    self.labels2[0].config(text="Padm")
                    self.labels2[1].config(text="F")
                    self.listunds[0].config(text="lb.in")
                    self.listunds2[0].config(text="PSI")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[0].config(text="Pa")
                    self.listunds2[0].config(text="N.m")
                    self.listunds2[1].config(text="N")
                    self.boton1.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="Padm")
                    self.labels2[0].config(text="T")
                    self.labels2[1].config(text="F")
                    self.listunds[0].config(text="PSI")
                    self.listunds2[0].config(text="lb.in")
                    self.listunds2[1].config(text="lb")
                    self.boton1.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(2)
        self.list.place(x=215, y=70)

        self.opciones_list_interpolation_table = ["Dada r'", "Dado α", "Dado ß"]
        self.list_interpolation_table = Combobox(self, width=15, values=self.opciones_list_interpolation_table, state="disabled")
        def callback1(event):
            if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[0]:
                self.labels[1].config(text="r'")
            if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[1]:
                self.labels[1].config(text="α")
            if self.list_interpolation_table.get() == self.opciones_list_interpolation_table[2]:
                self.labels[1].config(text="ß")
        self.list_interpolation_table.bind('<<ComboboxSelected>>', callback1)
        self.list_interpolation_table.current(0)
        self.list_interpolation_table.place(x=395, y=70)

        self.coef_label = Label(self, text="Para el coeficiente de friccion")
        self.coef_label.place(x=215, y=95)
        self.lista_coef = ["Con material de friccion","Ingresando valor"]
        self.list3 = Combobox(self, width=25, values=self.lista_coef, state="disabled")
        def cambio_coef(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list4["state"]="readonly"
            if self.list3.get() == self.lista_coef[1]:
                self.textos[3]["state"]="normal"
                self.btn3["state"] = "normal"
        self.list3.bind('<<ComboboxSelected>>', cambio_coef)
        self.list3.place(x=215, y=115)

        self.lista_mat_friccion_label = Label(self, text="Material de friccion")
        self.lista_mat_friccion_label.place(x=395, y=95)
        self.lista_mat_friccion = ["Fundicion de hierro","Metal sinterizado","Madera","Cuero","Corcho","Fieltro","Asbesto tejido",
        "Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet","Cuerda de asbesto arrollado","Tira de asbesto tejido",
        "Algodón tejido","Papel resiliente"]
        self.list4 = Combobox(self, width=20, values=self.lista_mat_friccion, state="disabled")
        def Mat(event):
            self.list5["state"]="readonly"
        self.list4.bind('<<ComboboxSelected>>', Mat)
        self.list4.place(x=395, y=115)

        self.lista_humedo_seco = ["Ambiente humedo","Ambiente seco"]
        self.list5 = Combobox(self, width=20, values=self.lista_humedo_seco, state="disabled")
        def humedo_seco(event):
            base_path2 = pathlib.Path(__file__).parent.resolve()
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
                    presion_maxima_dato = presion_maxima_dato[0]*1000
                    self.textos[3]["state"]="normal"
                    self.textos[3].delete(0,"end")
                    self.textos[3].insert(0,coeficiente_dato)
                    self.textos[3]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Ingles WHERE Material_de_friccion='{self.list4.get()}' ")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[3]["state"]="normal"
                    self.textos[3].delete(0,"end")
                    self.textos[3].insert(0,coeficiente_dato)
                    self.textos[3]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            if self.list5.get() == self.lista_humedo_seco[1]:
                if self.list2.get() == self.listaUnds[0]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Internacional WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    presion_maxima_dato = presion_maxima_dato[0]*1000
                    self.textos[3]["state"]="normal"
                    self.textos[3].delete(0,"end")
                    self.textos[3].insert(0,coeficiente_dato)
                    self.textos[3]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[3]["state"]="normal"
                    self.textos[3].delete(0,"end")
                    self.textos[3].insert(0,coeficiente_dato)
                    self.textos[3]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            conexion.close()
            self.btn3["state"] = "disabled"
        self.list5.bind('<<ComboboxSelected>>', humedo_seco)
        self.list5.place(x=545, y=115)

        self.lbl18 = Label(self,text='Pa')
        self.lbl18.place(x=200, y=305, width=40, height=20)
        self.txt18 = Entry(self)
        self.txt18.place(x=240, y=300, width=70, height=20)
        self.lbl36 = Label(self)
        self.lbl36.place(x=200, y=270, width=150, height=20)

        self.btnayuda = Button(self, text='?', command = self.ayuda)
        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn4 = Button(self, text='calc', command=self.CalcFD)
        self.btnayuda.place(x=215, y=140, width=30, height=30)
        self.btn3.place(x=320, y=300, width=40, height=40)
        self.btn4.place(x=320, y=350, width=40, height=40)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    CircularWindow(root).mainloop()