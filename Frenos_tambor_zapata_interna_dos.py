import os
import pathlib
import sqlite3
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from tkinter import ttk
from math import *
from PIL import ImageTk, Image


class ZapataInternaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1400, height=730)
        self.master = master
        self.pack()
        self.create_widget()

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

        µ = float(self.textos[1].get())

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
            material = self.lbl2["text"]
            self.txt18.delete(0,"end")
            self.txt18.insert(0, mawp)
            self.lbl36.config(text=material)
            if mawp:
                self.table_window.destroy()
                return mawp 

        self.submit = Button(self.table_window, text="Insertar", command=set_mawp)
        self.submit.place(x=160, y=450)

    def Calc_pasadores(self,R):
        Lp = float(self.textos[10].get())
        Dp = float(self.textos[11].get())
        Syp = float(self.textos[12].get())
        sigma_pasador = (16*R*Lp)/(pi*(Dp**3))
        FSp = Syp/sigma_pasador
        self.FSp = FSp
        return FSp

    def Calc_tambor(self,D,padm):
        Dt = float(self.textos[13].get())
        #Lt = float(self.textos[14].get())
        t = float(self.textos[15].get())
        Syt = float(self.textos[16].get())
        if t/(D/2) <= 0.05:
            sigma_tambor = (padm*(D+t))/2*t
        if t/(D/2) > 0.05:
            gt = ((padm*((D/2)**2))/(((Dt/2)**2)-((D/2)**2)))*(1+(((Dt/2)**2)/((D/2)**2)))
            gr = ((padm*((D/2)**2))/(((Dt/2)**2)-((D/2)**2)))*(1-(((Dt/2)**2)/((D/2)**2)))
            sigma_tambor = sqrt((gt**2)-(gt*gr)+(gr**2))
        FSt = Syt/sigma_tambor
        self.FSt =FSt
        return FSt

    def operacionesT(self):
        a1 = float(self.textos[0].get())
        a2 = float(self.textos[1].get())
        a3 = float(self.textos[2].get())
        a4 = float(self.textos[3].get())
        a5 = float(self.textos[4].get())
        a6 = float(self.textos[5].get())
        a7 = float(self.textos[6].get())
        a8 = float(self.textos[7].get())
        y = float(self.textos[8].get())
        x = float(self.textos[9].get())
        Pa = float(self.txt18.get())

        if a8 <= 90:
            a9 = a8
        if a8 > 90:
            a9 = 90

        I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
        I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
        I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

        Padm = (a1*sin(a9*(3.14/180)))/(a2*a6*((a5/2)**2)*I1)

        Mn = (Padm*a6*a3*(a5/2)/(sin(a9*(pi/180))))*I3
        Mf = (a2*Padm*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

        Θ3 = atan(x/y)
        
        if self.list_sentido_fuerza.get() == "hacia la derecha":
            self.sentido_fuerza = +1
        if self.list_sentido_fuerza.get() == "hacia la izquierda":
            self.sentido_fuerza = -1
        if self.list_sentido_giro.get() == "horario":
            self.sentido_giro = +1
        if self.list_sentido_giro.get() == "antihorario":
            self.sentido_giro = -1
        self.result = self.sentido_fuerza*self.sentido_giro
        if self.result == 1:
            self.label_ener_desener.config(text="Autoenergizante")
        if self.result == -1:
            self.label_ener_desener.config(text="Autodesenergizante")

        if self.result == 1:
            F = (Mn-Mf)/a4
            F = round(F,3)

            Fx = F*sin(Θ3)
            Fx = round(Fx,3)
            Fy = F*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - Fx
            Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - Fy
        
        if self.result == -1:
            F = (Mn+Mf)/a4
            F = round(F,3)

            Fx = F*sin(Θ3)
            Fx = round(Fx,3)
            Fy = F*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - Fx
            Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - Fy
        
        R = sqrt((Rx**2)+(Ry**2))

        if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
            self.Calc_pasadores(R)
            FSp = self.FSp
            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FSp)

        if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
            self.Calc_tambor(a5,Padm)
            FSt = self.FSt
            self.textos2[9].delete(0,"end")
            self.textos2[9].insert(0,FSt)

        FD = Pa/Padm
        
        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,Padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,F)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,a9)

        self.textos2[3].delete(0,"end")
        self.textos2[3].insert(0,Fx)
        self.textos2[4].delete(0,"end")
        self.textos2[4].insert(0,Fy)

        self.textos2[5].delete(0,"end")
        self.textos2[5].insert(0,Rx)
        self.textos2[6].delete(0,"end")
        self.textos2[6].insert(0,Ry)

        self.textos2[7].delete(0,"end")
        self.textos2[7].insert(0,R)

        self.textos2[10].delete(0,"end")
        self.textos2[10].insert(0,FD)
    
    def operacionesPadm(self):
        a1 = float(self.textos[0].get())
        a2 = float(self.textos[1].get())
        a3 = float(self.textos[2].get())
        a4 = float(self.textos[3].get())
        a5 = float(self.textos[4].get())
        a6 = float(self.textos[5].get())
        a7 = float(self.textos[6].get())
        a8 = float(self.textos[7].get())
        y = float(self.textos[8].get())
        x = float(self.textos[9].get())
        Pa = float(self.txt18.get())

        if a8 <= 90:
            a9 = a8
        if a8 > 90:
            a9 = 90

        I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
        I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
        I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

        Mn = (a1*a6*a3*(a5/2)/(sin(a9*(3.14/180))))*I3
        Mf = (a2*a1*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

        Θ3 = atan(x/y)
        
        if self.list_sentido_fuerza.get() == "hacia la derecha":
            self.sentido_fuerza = +1
        if self.list_sentido_fuerza.get() == "hacia la izquierda":
            self.sentido_fuerza = -1
        if self.list_sentido_giro.get() == "horario":
            self.sentido_giro = +1
        if self.list_sentido_giro.get() == "antihorario":
            self.sentido_giro = -1
        self.result = self.sentido_fuerza*self.sentido_giro
        if self.result == 1:
            self.label_ener_desener.config(text="Autoenergizante")
        if self.result == -1:
            self.label_ener_desener.config(text="Autodesenergizante")

        if self.result == 1:
            F = (Mn-Mf)/a4
            F = round(F,3)

            T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Fx = F*sin(Θ3)
            Fx = round(Fx,3)
            Fy = F*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - Fx
            Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - Fy
        
        if self.result == -1:
            F = (Mn+Mf)/a4
            F = round(F,3)

            T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Fx = F*sin(Θ3)
            Fx = round(Fx,3)
            Fy = F*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - Fx
            Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - Fy
        
        R = sqrt((Rx**2)+(Ry**2))

        if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
            self.Calc_pasadores(R)
            FSp = self.FSp
            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FSp)

        if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
            self.Calc_tambor(a5,a1)
            FSt = self.FSt
            self.textos2[9].delete(0,"end")
            self.textos2[9].insert(0,FSt)
        FD = Pa/a1

        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,F)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,a9)

        self.textos2[3].delete(0,"end")
        self.textos2[3].insert(0,Fx)
        self.textos2[4].delete(0,"end")
        self.textos2[4].insert(0,Fy)

        self.textos2[5].delete(0,"end")
        self.textos2[5].insert(0,Rx)
        self.textos2[6].delete(0,"end")
        self.textos2[6].insert(0,Ry)

        self.textos2[7].delete(0,"end")
        self.textos2[7].insert(0,R)

        self.textos2[10].delete(0,"end")
        self.textos2[10].insert(0,FD)
        

    def operacionesF(self):
        a1 = float(self.textos[0].get())
        a2 = float(self.textos[1].get())
        a3 = float(self.textos[2].get())
        a4 = float(self.textos[3].get())
        a5 = float(self.textos[4].get())
        a6 = float(self.textos[5].get())
        a7 = float(self.textos[6].get())
        a8 = float(self.textos[7].get())
        y = float(self.textos[8].get())
        x = float(self.textos[9].get())
        Pa = float(self.txt18.get())

        if a8 <= 90:
            a9 = a8
        if a8 > 90:
            a9 = 90

        I1 = -cos(radians(a8)) + cos(radians(a7))
        I2 = 0.5*(sin(radians(a8))**2) - 0.5*(sin(radians(a7))**2)
        I3 = (radians(a8/2))-0.25*sin(2*(radians(a8))) - ((radians(a7/2))-0.25*sin(2*(radians(a7))))

        valor1 = (a6*a3*(a5/2)/(sin(radians(a9))))*I3
        valor2 = (a2*a6*(a5/2)/(sin(radians(a9))))*((a5/2)*I1 - a3*I2)
        
        Θ3 = atan(x/y)
        
        if self.list_sentido_fuerza.get() == "hacia la derecha":
            self.sentido_fuerza = +1
        if self.list_sentido_fuerza.get() == "hacia la izquierda":
            self.sentido_fuerza = -1
        if self.list_sentido_giro.get() == "horario":
            self.sentido_giro = +1
        if self.list_sentido_giro.get() == "antihorario":
            self.sentido_giro = -1
        self.result = self.sentido_fuerza*self.sentido_giro
        if self.result == 1:
            self.label_ener_desener.config(text="Autoenergizante")
        if self.result == -1:
            self.label_ener_desener.config(text="Autodesenergizante")

        if self.result == 1:

            padm = (a1*a4)/(valor1-valor2)
            padm = round(padm,3)

            T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(radians(a9)))
            T = round(T,3)

            Fx = a1*sin(Θ3)
            Fx = round(Fx,3)
            Fy = a1*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((padm*a6*(a5/2))/sin(radians(a9)))*(I2-(a2*I3))) - Fx
            Rx = round(Rx,3)
            Ry = (((padm*a6*(a5/2))/sin(radians(a9)))*(I3+(a2*I2))) - Fy
            Ry = round(Ry,3)

        if self.result == -1:
            
            padm = (a1*a4)/(valor1+valor2)
            padm = round(padm,3)

            T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Fx = a1*sin(Θ3)
            Fx = round(Fx,3)
            Fy = a1*cos(Θ3)
            Fy = round(Fy,3)

            Rx = (((padm*a6*(a5/2))/sin(radians(a9)))*(I2+(a2*I3))) - Fx
            Rx = round(Rx,3)
            Ry = (((padm*a6*(a5/2))/sin(radians(a9)))*(I3-(a2*I2))) - Fy
            Ry = round(Ry,3)
        
        R = sqrt((Rx**2)+(Ry**2))
        
        if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
            self.Calc_pasadores(R)
            FSp = self.FSp
            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FSp)

        if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
            self.Calc_tambor(a5,padm)
            FSt = self.FSt
            self.textos2[9].delete(0,"end")
            self.textos2[9].insert(0,FSt)

        FD = Pa/padm
        
        self.textos2[2].delete(0,"end")
        self.textos2[2].insert(0,padm)

        self.textos2[1].delete(0,"end")
        self.textos2[1].insert(0,T)

        self.textos2[0].delete(0,"end")
        self.textos2[0].insert(0,a9)

        self.textos2[3].delete(0,"end")
        self.textos2[3].insert(0,Fx)
        self.textos2[4].delete(0,"end")
        self.textos2[4].insert(0,Fy)

        self.textos2[5].delete(0,"end")
        self.textos2[5].insert(0,Rx)
        self.textos2[6].delete(0,"end")
        self.textos2[6].insert(0,Ry)

        self.textos2[7].delete(0,"end")
        self.textos2[7].insert(0,R)

        self.textos2[10].delete(0,"end")
        self.textos2[10].insert(0,FD)

    def info(self):
        self.mensaje = """Programa que resuelve casos generales tomando en cuenta cada zapata individualmente y un sistema de referencia
que coincide con el pasador"""
        messagebox.showinfo(title="Aclaratoria", message=self.mensaje)

    def create_widget(self):

        Internacional = ["N","","mm","mm","mm","mm","°","°","mm","mm","mm","mm","MPa","mm","mm","mm","MPa","°","N.mm","MPa","N","N","N","N","N","","",""]
        Ingles = ["lb","","in","in","in","in","°","°","in","in","in","in","PSI","in","in","in","PSI","°","lb.in","PSI","lb","lb","lb","lb","lb","","",""]

        self.lblSU = Label(self, text="Sistema de unidades")
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
                self.list["state"]="readonly"
                self.list3["state"]="readonly"
                self.list_sentido_fuerza["state"]="readonly"
                self.list_sentido_giro["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[1]["state"]="disabled"
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
                self.list3["state"]="readonly"
                self.list_sentido_fuerza["state"]="readonly"
                self.list_sentido_giro["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[1]["state"]="disabled"
                for entries in self.textos2:
                    entries.config(state=NORMAL)
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        self.info_button = Button(self, text="!", bg="yellow", command=self.info)
        self.info_button.place(x=240, y=30, width=25, height=25)

        self.lbl_options = Label(self, text="Variables a calcular")
        self.lbl_options.place(x=40, y=60)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="disabled")
        def callback(event):
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="F: fuerza de accionamiento")
                    self.labels2[1].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[2].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.listunds[0].config(text="N")
                    self.listunds2[1].config(text="N.mm")
                    self.listunds2[2].config(text="MPa")
                    self.solve_button.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="F: fuerza de accionamiento")
                    self.labels2[1].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[2].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.listunds[0].config(text="lb")
                    self.listunds2[1].config(text="lb.in")
                    self.listunds2[2].config(text="PSI")
                    self.solve_button.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[1].config(text="F: fuerza de accionamiento")
                    self.labels2[2].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.listunds[0].config(text="N.mm")
                    self.listunds2[1].config(text="N")
                    self.listunds2[2].config(text="MPa")
                    self.solve_button.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[1].config(text="F: fuerza de accionamiento")
                    self.labels2[2].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.listunds[0].config(text="lb.in")
                    self.listunds2[1].config(text="lb")
                    self.listunds2[2].config(text="PSI")
                    self.solve_button.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.labels[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[2].config(text="F: fuerza de accionamiento")
                    self.listunds[0].config(text="MPa")
                    self.listunds2[1].config(text="N.mm")
                    self.listunds2[2].config(text="N")
                    self.solve_button.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.labels[0].config(text="Padm: Presión máxima admisible ejercida sobre el material de fricción")
                    self.labels2[1].config(text="T: Torque debido a la fuerza de fricción")
                    self.labels2[2].config(text="F: fuerza de accionamiento")
                    self.listunds[0].config(text="PSI")
                    self.listunds2[1].config(text="lb.in")
                    self.listunds2[2].config(text="lb")
                    self.solve_button.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(0)
        self.list.place(x=40, y=80)

        self.lbl_casos_zapatas = Label(self, text="Casos de zapata")
        self.lbl_casos_zapatas.place(x=240, y=60)

        self.lbl_sentido_fuerza = Label(self, text="Sentido de la fuerza")
        self.lbl_sentido_fuerza.place(x=240, y=80)
        self.list_sentido_fuerza = Combobox(self, width=25, values=("hacia la derecha","hacia la izquierda"), state="disabled")
        self.list_sentido_fuerza.place(x=360, y=80)

        self.lbl_sentido_giro = Label(self, text="Sentido de giro")
        self.lbl_sentido_giro.place(x=240, y=110)
        self.list_sentido_giro = Combobox(self, width=25, values=("horario", "antihorario"), state="disabled")
        self.list_sentido_giro.place(x=360, y=110)

        self.label_ener_desener = Label(self)
        self.label_ener_desener.place(x=570, y=80)

        self.coef_label = Label(self, text="Para el coeficiente de friccion")
        self.coef_label.place(x=40, y=140)
        self.lista_coef = ["Con material de friccion","Ingresando valor"]
        self.list3 = Combobox(self, width=25, values=self.lista_coef, state="disabled")
        def cambio_coef(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list4["state"]="readonly"
                self.textos[1]["state"]="disabled"
            if self.list3.get() == self.lista_coef[1]:
                self.textos[1]["state"]="normal"
                self.list4["state"]="disabled"
                self.list5["state"]="disabled"
                self.btn3["state"] = "normal"
        self.list3.bind('<<ComboboxSelected>>', cambio_coef)
        self.list3.place(x=40, y=160)

        self.lista_mat_friccion_label = Label(self, text="Material de friccion")
        self.lista_mat_friccion_label.place(x=240, y=140)
        self.lista_mat_friccion = ["Fundicion de hierro","Metal sinterizado","Madera","Cuero","Corcho","Fieltro","Asbesto tejido",
        "Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet","Cuerda de asbesto arrollado","Tira de asbesto tejido",
        "Algodón tejido","Papel resiliente"]
        self.list4 = Combobox(self, width=20, values=self.lista_mat_friccion, state="disabled")
        def Mat(event):
            self.list5["state"]="readonly"
        self.list4.bind('<<ComboboxSelected>>', Mat)
        self.list4.place(x=240, y=160)

        self.lista_humedo_seco_lbl = Label(self, text="Tipo de ambiente")
        self.lista_humedo_seco_lbl.place(x=420, y=140)
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
                    self.textos[1]["state"]="normal"
                    self.textos[1].delete(0,"end")
                    self.textos[1].insert(0,coeficiente_dato)
                    self.textos[1]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_humedo FROM Ingles WHERE Material_de_friccion='{self.list4.get()}' ")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[1]["state"]="normal"
                    self.textos[1].delete(0,"end")
                    self.textos[1].insert(0,coeficiente_dato)
                    self.textos[1]["state"]="disabled"

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
                    self.textos[1]["state"]="normal"
                    self.textos[1].delete(0,"end")
                    self.textos[1].insert(0,coeficiente_dato)
                    self.textos[1]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
                if self.list2.get() == self.listaUnds[1]:
                    cursor.execute(f"SELECT Coeficiente_de_friccion_minimo_seco FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    coeficiente_dato = cursor.fetchone()
                    cursor.execute(f"SELECT Presion_maxima FROM Ingles WHERE Material_de_friccion='{self.list4.get()}'")
                    presion_maxima_dato = cursor.fetchone()
                    self.textos[1]["state"]="normal"
                    self.textos[1].delete(0,"end")
                    self.textos[1].insert(0,coeficiente_dato)
                    self.textos[1]["state"]="disabled"

                    self.txt18.delete(0,"end")
                    self.txt18.insert(0, presion_maxima_dato)
                    self.lbl36.config(text=self.list4.get())
            conexion.close()
            self.btn3["state"] = "disabled"
        self.list5.bind('<<ComboboxSelected>>', humedo_seco)
        self.list5.place(x=420, y=160)

        self.labels = []
        textoslbl = ["F: fuerza de accionamiento","µ: Coeficiente de friccion","a: Distancia desde el pivote hasta el centro del tambor",
        "c: Distancia desde el pto de aplicacion de la fuerza hasta el centro del pivote","D: Diametro del tambor",
        "b: Ancho de la zapata","Θ1: Angulo entre el pasador y el material de friccion","Θ2: Angulo final material de friccion",
        "y: Distancia vertical desde el eje de referencia x hasta el pasador","x: Distancia horizontal desde el eje de referencia y hasta el pasador",
        "Lp: Longitud del pasador","Dp: Diametro del pasador", "Sy material del pasador", "Dt: Diametro externo del tambor", "Lt: Longitud del tambor",
        "t: Espesor de pared", "Sy material del tambor"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos))
        i=200
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30
        
        self.listunds = []
        unds = ["N","","mm","mm","mm","mm","°","°","mm","mm","mm","mm","MPa","mm","mm","mm","MPa"]
        for unidades in unds:
            self.listunds.append(Label(self))
        i=200
        for unidades in self.listunds:
            unidades.place(x=530, y=i)
            i += 30

        self.textos = []
        for texto in range(0,17):
            self.textos.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos:
            parameters.place(x=460, y=i, width=60)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'images\\Freno.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=1050, y=0, width=350, height=350)

        self.base_path_2nd_part = pathlib.Path(__file__).parent.resolve()
        self.image_filename_2nd_part = 'images\\Zapata interna ancho de cara.png'
        self.image2 = Image.open(os.path.join(self.base_path_2nd_part, self.image_filename_2nd_part))
        self.image2 = self.image2.resize((350,380), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.image2)
        self.lbl_img2 = Label(self, image=self.img2)
        self.lbl_img2.place(x=1050, y=350, width=350, height=380)

        self.labels2 = []
        textoslabels2 = ["Θa: Angulo donde se aplica la presión máxima admisible","T: Torque debido a la fuerza de fricción",
        "Padm: Presión máxima admisible ejercida sobre el material de fricción","Fx: Componente en el eje x de la fuerza de accionamiento",
        "Fy: Componente en el eje y de la fuerza de accionamiento", "Rx: Reacción del pasador en el eje x", "Ry: Reacción del pasador en el eje y",
        "R: Reaccion en el pasador", "Factor de seguridad del pasador", "Factor de seguridad del tambor", "Factor de diseño"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos))
        i=200
        for cosas in self.labels2:
            cosas.place(x=560, y=i)
            i += 30

        self.textos2 = []
        for texto in range(0,11):
            self.textos2.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos2:
            parameters.place(x=950, y=i, width=60)
            i += 30

        self.listunds2 = []
        unds2 = ["°","N.mm","MPa","N","N","N","N","N","","",""]
        for unidades in unds2:
            self.listunds2.append(Label(self))
        i=200
        for unidades in self.listunds2:
            unidades.place(x=1020, y=i)
            i += 30       

        self.lbl18 = Label(self,text='Pa')
        self.lbl18.place(x=700, y=80)
        self.txt18 = Entry(self)
        self.txt18.place(x=720, y=80, width=60)
        self.lbl36 = Label(self)
        self.lbl36.place(x=700, y=60, width=150, height=20)

        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn3.place(x=790, y=80, width=40, height=40)
        # self.btn4 = Button(self, text='calc', command=self.CalcFD)        
        # self.btn4.place(x=320, y=350, width=40, height=40)
        self.solve_button = Button(self, text="Calcular", command=self.operacionesF)
        self.solve_button.place(x=570, y=650, width=50, height=50)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Calculos de validacion para frenos y embragues de zapata interna")
    base_path_3rd_part = pathlib.Path(__file__).parent.resolve()
    image_filename_3rd_part = "images\\Logo ANFRA.ico"
    icono = os.path.join(base_path_3rd_part, image_filename_3rd_part)
    root.iconbitmap(icono)
    ZapataInternaWindow(root).mainloop()