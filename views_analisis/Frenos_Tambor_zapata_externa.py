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

class ZapataExternaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1400, height=730)
        self.master = master
        self.pack()
        self.create_widget()

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

            µ = float(self.textos[1].get())
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
            messagebox.showerror(title="Error", message="Completa la sección de coeficiente de fricción para obtener un valor", parent=self)

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
        vent.tipo_freno.set("Tambor")
        vent.tipo_freno.event_generate('<<ComboboxSelected>>')
        vent.tipo_freno["state"] = "disabled"
        vent.list5.event_generate('<<ComboboxSelected>>')
        vent.list4.event_generate('<<ComboboxSelected>>')
        vent.peso_especifico.event_generate('<<ComboboxSelected>>')
        Dext = self.textos[13].get()
        Lt = self.textos[14].get()
        t = self.textos[15].get()
        if unidades == "Sistema Internacional":
            vent.textos2[0].insert(0,float(Lt)/1000)
            vent.textos2[1].insert(0,float(Dext)/1000)
            vent.textos2[2].insert(0,float(t)/1000)
        else:
            vent.textos2[0].insert(0,Lt)
            vent.textos2[1].insert(0,Dext)
            vent.textos2[2].insert(0,t)

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

    def calc_torque_frenado(self,T):
        Treq = float(self.torque_frenado_txt.get())

        if self.nro_zapatas.get() == "1":
                self.zapatas[0].delete(0,"end")
                self.zapatas[0].insert(0,T)
                Ttotal = float(self.zapatas[0].get())
                self.torque_total_txt.delete(0,"end")
                self.torque_total_txt.insert(0,self.zapatas[0].get())
        elif self.nro_zapatas.get() == "2":
            if not self.zapatas[0].get():
                self.lbl_contador_zapata.config(text="Primera zapata")
                self.zapatas[0].delete(0,"end")
                self.zapatas[0].insert(0,T)
            else:
                    self.lbl_contador_zapata.config(text="Segunda zapata")
                    self.zapatas[1].delete(0,"end")
                    self.zapatas[1].insert(0,T)
                    Ttotal = float(self.zapatas[0].get()) + float(self.zapatas[1].get())
                    self.torque_total_txt.delete(0,"end")
                    self.torque_total_txt.insert(0,Ttotal)
        elif self.nro_zapatas.get() == "3":
            if not self.zapatas[0].get():
                self.lbl_contador_zapata.config(text="Primera zapata")
                self.zapatas[0].delete(0,"end")
                self.zapatas[0].insert(0,T)
            elif self.zapatas[0].get() and not self.zapatas[1].get():
                self.lbl_contador_zapata.config(text="Segunda zapata")
                self.zapatas[1].delete(0,"end")
                self.zapatas[1].insert(0,T)
            else:
                self.lbl_contador_zapata.config(text="Tercera zapata")
                self.zapatas[2].delete(0,"end")
                self.zapatas[2].insert(0,T)
                Ttotal = float(self.zapatas[0].get()) + float(self.zapatas[1].get()) + float(self.zapatas[2].get())
                self.torque_total_txt.delete(0,"end")
                self.torque_total_txt.insert(0,Ttotal)
        elif self.nro_zapatas.get() == "4":
            if not self.zapatas[0].get():
                self.lbl_contador_zapata.config(text="Primera zapata")
                self.zapatas[0].delete(0,"end")
                self.zapatas[0].insert(0,T)
            elif self.zapatas[0].get() and not self.zapatas[1].get():
                self.lbl_contador_zapata.config(text="Segunda zapata")
                self.zapatas[1].delete(0,"end")
                self.zapatas[1].insert(0,T)
            elif self.zapatas[0].get() and self.zapatas[1].get() and not self.zapatas[2].get():
                self.lbl_contador_zapata.config(text="Tercera zapata")
                self.zapatas[2].delete(0,"end")
                self.zapatas[2].insert(0,T)
            else:
                self.lbl_contador_zapata.config(text="Cuarta zapata")
                self.zapatas[3].delete(0,"end")
                self.zapatas[3].insert(0,T)
                Ttotal = float(self.zapatas[0].get()) + float(self.zapatas[1].get()) + float(self.zapatas[2].get()) + float(self.zapatas[3].get())
                self.torque_total_txt.delete(0,"end")
                self.torque_total_txt.insert(0,Ttotal)

        if self.torque_total_txt.get():
            if Ttotal < Treq:
                self.lbl_comparacion_torque["text"] = "Se reduce la velocidad"
            else:
                self.lbl_comparacion_torque["text"] = "El sistema frena\ncompletamente"

    def limpiar(self):
        for caja_de_texto in self.textos:
            caja_de_texto.delete(0,"end")
        for caja_de_texto in self.textos2:
            caja_de_texto.delete(0,"end")
        self.txt18.delete(0,"end")

    def operacionesPadm(self):
        try:
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

            if y == 0:
                Θ3 = radians(90)
            else:
                Θ3 = atan(x/y)
            
            if self.list_cuadrante.get() == "superior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "superior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "inferior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
            elif self.list_cuadrante.get() == "inferior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1

            if self.result == 1:
                self.label_ener_desener.config(text="Autoenergizante")
            if self.result == -1:
                self.label_ener_desener.config(text="Autodesenergizante")

            if self.result == 1:
                
                F = (Mn-Mf)/a4
                F = round(F,2)

                T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
                T = round(T,2)

                Fx = F*sin(Θ3)
                Fx = round(Fx,2)
                Fy = F*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - Fx
                Ry = round(Rx,2)
                Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3-(a2*I2))) + Fy
                Ry = round(Rx,2)

            if self.result == -1:

                F = (Mn+Mf)/a4
                F = round(F,2)

                T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
                T = round(T,2)

                Fx = F*sin(Θ3)
                Fx = round(Fx,2)
                Fy = F*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - Fx
                Rx = round(Rx,2)
                Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3+(a2*I2))) + Fy
                Rx = round(Rx,2)

            R = sqrt((Rx**2)+(Ry**2))
            R = round(R,2)

            if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
                self.Calc_pasadores(R)
                FSp = self.FSp
                FSp = round(FSp,2)
                self.textos2[9].delete(0,"end")
                self.textos2[9].insert(0,FSp)

            if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
                self.Calc_tambor(a5,a1)
                FSt = self.FSt
                FSt = round(FSt,2)
                self.textos2[10].delete(0,"end")
                self.textos2[10].insert(0,FSt)
            FD = Pa/a1
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL)

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

            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FD)

            if self.torque_frenado_txt.get(T):
                self.calc_torque_frenado(a1)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros por lo menos hasta la distancia x, incluyendo Pa, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros de inicialización", parent=self)

    def operacionesT(self):
        try:
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

            if y == 0:
                Θ3 = radians(90)
            else:
                Θ3 = atan(x/y)
            
            if self.list_cuadrante.get() == "superior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "superior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "inferior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
            elif self.list_cuadrante.get() == "inferior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1

            if self.result == 1:
                self.label_ener_desener.config(text="Autoenergizante")
            if self.result == -1:
                self.label_ener_desener.config(text="Autodesenergizante")

            if self.result == 1:

                F = (Mn-Mf)/a4
                F = round(F,2)

                Fx = F*sin(Θ3)
                Fx = round(Fx,2)
                Fy = F*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - Fx
                Rx = round(Rx,2)
                Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3-(a2*I2))) + Fy
                Ry = round(Ry,2)

            if self.result == -1:

                F = (Mn+Mf)/a4
                F = round(F,2)

                Fx = F*sin(Θ3)
                Fx = round(Fx,2)
                Fy = F*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - Fx
                Rx = round(Rx,2)
                Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3+(a2*I2))) + Fy
                Ry = round(Ry,2)
            
            R = sqrt((Rx**2)+(Ry**2))
            R = round(R,2)

            if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
                self.Calc_pasadores(R)
                FSp = self.FSp
                FSp = round(FSp,2)
                self.textos2[9].delete(0,"end")
                self.textos2[9].insert(0,FSp)

            if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
                self.Calc_tambor(a5,Padm)
                FSt = self.FSt
                FSt = round(FSt,2)
                self.textos2[10].delete(0,"end")
                self.textos2[10].insert(0,FSt)

            FD = Pa/Padm
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL)
            
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

            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FD)

            if self.torque_frenado_txt.get():
                self.calc_torque_frenado(a1)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros por lo menos hasta la distancia x, incluyendo Pa, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros de inicialización", parent=self)

    def operacionesF(self):
        try:
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

            valor1 = (a6*a3*(a5/2)/(sin(a9*(3.14/180))))*I3
            valor2 = (a2*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

            if y == 0:
                Θ3 = radians(90)
            else:
                Θ3 = atan(x/y)
            
            if self.list_cuadrante.get() == "superior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "superior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
            elif self.list_cuadrante.get() == "inferior izquierda":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1
            elif self.list_cuadrante.get() == "inferior derecha":
                if self.list_sentido_fuerza.get() == "hacia la derecha" or self.list_sentido_fuerza.get() == "hacia arriba":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = -1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = 1
                elif self.list_sentido_fuerza.get() == "hacia la izquierda" or self.list_sentido_fuerza.get() == "hacia abajo":
                    if self.list_sentido_giro.get() == "horario":
                        self.result = 1
                    elif self.list_sentido_giro.get() == "antihorario":
                        self.result = -1

            if self.result == 1:
                self.label_ener_desener.config(text="Autoenergizante")
            if self.result == -1:
                self.label_ener_desener.config(text="Autodesenergizante")

            if self.result == 1:

                padm = (a1*a4)/(valor1-valor2)
                padm = round(padm,2)

                T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
                T = round(T,2)
                
                Fx = a1*sin(Θ3)
                Fx = round(Fx,2)
                Fy = a1*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - Fx
                Rx = round(Rx,2)
                Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3-(a2*I2))) + Fy
                Ry = round(Ry,2)

            if self.result == -1:
                
                padm = (a1*a4)/(valor1+valor2)
                padm = round(padm,2)

                T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
                T = round(T,2)

                Fx = a1*sin(Θ3)
                Fx = round(Fx,2)
                Fy = a1*cos(Θ3)
                Fy = round(Fy,2)

                Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - Fx
                Rx = round(Rx,2)
                Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(-I3+(a2*I2))) + Fy
                Ry = round(Ry,2)
            
            R = sqrt((Rx**2)+(Ry**2))
            R = round(R,2)
            
            if  self.textos[10].get() and self.textos[11].get() and self.textos[12].get():
                self.Calc_pasadores(R)
                FSp = self.FSp
                FSp = round(FSp,2)
                self.textos2[9].delete(0,"end")
                self.textos2[9].insert(0,FSp)

            if self.textos[13].get() and self.textos[15].get() and self.textos[16].get():
                self.Calc_tambor(a5,padm)
                FSt = self.FSt
                FSt = round(FSt,2)
                self.textos2[10].delete(0,"end")
                self.textos2[10].insert(0,FSt)

            FD = Pa/padm
            FD = round(FD,2)

            for entries in self.textos2:
                entries.config(state=NORMAL)
            
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

            self.textos2[8].delete(0,"end")
            self.textos2[8].insert(0,FD)

            if self.torque_frenado_txt.get():
                self.calc_torque_frenado(T)
        except ValueError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros por lo menos hasta la distancia x, incluyendo Pa, y debes ingresar solamente números", parent=self)
        except AttributeError:
            messagebox.showerror(title="Error", message="Debes ingresar todos los párametros de inicialización", parent=self) 

    def info(self):
        self.mensaje = """Programa que resuelve casos generales tomando en cuenta cada zapata individualmente y un sistema de referencia
que coincide con el pasador"""
        messagebox.showinfo(title="Aclaratoria", message=self.mensaje, parent=self)

    def create_widget(self):

        frame_inicializacion = Frame(self, width=1400, height=195, bg="#A9A9A9")
        frame_inicializacion.pack()

        frame_entrada_freno = Frame(self, width=1400, height=300, bg="#808080")
        frame_entrada_freno.pack()

        frame_entrada_pasador = Frame(self, width=1400, height=90, bg="#C0C0C0")
        frame_entrada_pasador.pack()

        frame_entrada_tambor = Frame(self, width=1400, height=145, bg="#DCDCDC")
        frame_entrada_tambor.pack()

        Internacional = ["N","","mm","mm","mm","mm","°","°","mm","mm","mm","mm","MPa","mm","mm","mm","MPa","°","N.mm","MPa","N","N","N","N","N","","",""]
        Ingles = ["lb","","in","in","in","in","°","°","in","in","in","in","PSI","in","in","in","PSI","°","lb.in","PSI","lb","lb","lb","lb","lb","","",""]

        self.lblSU = Label(self, text="Sistema de unidades", bg="#A9A9A9", font=("Tahoma", 9))
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
                self.lbl18_unidad.config(text="MPa")
                self.txt18["state"]=NORMAL
                self.list["state"]="readonly"
                self.list3["state"]="readonly"
                self.list_sentido_fuerza["state"]="readonly"
                self.list_sentido_giro["state"]="readonly"
                self.list_cuadrante["state"]="readonly"
                self.nro_zapatas["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[1]["state"]="disabled"
                # for entries in self.textos2:
                #     entries.config(state=NORMAL)
                self.torque_frenado_txt["state"]="normal"
                self.torque_total_txt["state"]="normal"
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
                self.list_sentido_fuerza["state"]="readonly"
                self.list_sentido_giro["state"]="readonly"
                self.list_cuadrante["state"]="readonly"
                self.nro_zapatas["state"]="readonly"
                for entries in self.textos:
                    entries.config(state=NORMAL)
                self.textos[1]["state"]="disabled"
                # for entries in self.textos2:
                #     entries.config(state=NORMAL)
                self.torque_frenado_txt["state"]="normal"
                self.torque_total_txt["state"]="normal"
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)
        self.list2.place(x=40, y=30)

        self.info_button = Button(self, text="!", bg="yellow", command=self.info)
        self.info_button.place(x=210, y=30, width=25, height=25)

        self.lbl_options = Label(self, text="Variables a calcular", bg="#A9A9A9", font=("Tahoma", 9))
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

        self.lbl_casos_zapatas = Label(self, text="Casos de zapata", bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl_casos_zapatas.place(x=240, y=30)

        self.lbl_cuadrante = Label(self, text="Cuadrante Fuerza",bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl_cuadrante.place(x=240, y=50)
        self.list_cuadrante = Combobox(self, width=25, values=("superior derecha","superior izquierda","inferior izquierda","inferior derecha"), state="disabled")
        self.list_cuadrante.place(x=360, y=50)

        self.lbl_sentido_fuerza = Label(self, text="Sentido de la fuerza", bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl_sentido_fuerza.place(x=240, y=80)
        self.list_sentido_fuerza = Combobox(self, width=25, values=("hacia la derecha","hacia la izquierda","hacia arriba","hacia abajo"), state="disabled")
        self.list_sentido_fuerza.place(x=360, y=80)

        self.lbl_sentido_giro = Label(self, text="Sentido de giro", bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl_sentido_giro.place(x=240, y=110)
        self.list_sentido_giro = Combobox(self, width=25, values=("horario", "antihorario"), state="disabled")
        self.list_sentido_giro.place(x=360, y=110)

        self.label_ener_desener = Label(self, font=("Tahoma", 9), bg="#A9A9A9")
        self.label_ener_desener.place(x=360, y=30)

        self.coef_label = Label(self, text="Para el coeficiente de fricción", bg="#A9A9A9", font=("Tahoma", 9))
        self.coef_label.place(x=40, y=140)
        self.lista_coef = ["Con material de fricción","Ingresando valor"]
        self.list3 = Combobox(self, width=25, values=self.lista_coef, state="disabled")
        def cambio_coef(event):
            if self.list3.get() == self.lista_coef[0]:
                self.list5["state"]="readonly"
                self.textos[1]["state"]="disabled"
            if self.list3.get() == self.lista_coef[1]:
                self.textos[1]["state"]="normal"
                self.list4["state"]="disabled"
                self.list5["state"]="readonly"
                self.btn3["state"] = "normal"
        self.list3.bind('<<ComboboxSelected>>', cambio_coef)
        self.list3.place(x=40, y=160)

        self.lista_mat_friccion_label = Label(self, text="Material de fricción", bg="#A9A9A9", font=("Tahoma", 9))
        self.lista_mat_friccion_label.place(x=420, y=140)
        self.lista_mat_friccion = ["Fundición de hierro","Metal sinterizado con tambor de acero","Metal sinterizado con tambor de fundición de hierro",
        "Madera","Cuero","Corcho","Fieltro","Asbesto tejido","Asbesto moldeado","Asbesto impregnado","Grafito de carbono","Cermet",
        "Cuerda de asbesto arrollado","Tira de asbesto tejido","Algodón tejido","Papel resiliente"]
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

        self.labels = []
        textoslbl = ["F: Fuerza de accionamiento","µ: Coeficiente de friccion","a: Distancia desde el pivote hasta el centro del tambor",
        "c: Distancia desde el pto de aplicacion de la fuerza hasta el centro del pivote","D: Diámetro del tambor",
        "b: Ancho de la zapata","Θ1: Ángulo entre el pasador y el material de fricción","Θ2: Ángulo final material de fricción",
        "y: Distancia vertical desde el eje de referencia x hasta el pasador","x: Distancia horizontal desde el eje de referencia y hasta el pasador",
        "Lp: Longitud del pasador","Dp: Diámetro del pasador", "Sy: Material del pasador", "Dt: Diámetro externo del tambor", "Lt: Longitud del tambor",
        "t: Espesor de pared", "Sy: Material del tambor"]
        for textos in textoslbl:
            self.labels.append(Label(self, text=textos, bg="#808080", font=("Tahoma", 9)))
        i=200
        for cosas in self.labels:
            cosas.place(x=40, y=i)
            i += 30
        for label in self.labels[10:13]:
            label["bg"] = "#C0C0C0"
        for label in self.labels[13:18]:
            label["bg"] = "#DCDCDC"
        
        self.listunds = []
        unds = ["N","","mm","mm","mm","mm","°","°","mm","mm","mm","mm","MPa","mm","mm","mm","MPa"]
        for unidades in unds:
            self.listunds.append(Label(self, bg="#808080"))
        i=200
        for unidades in self.listunds:
            unidades.place(x=530, y=i)
            i += 30
        for label in self.listunds[10:13]:
            label["bg"] = "#C0C0C0"
        for label in self.listunds[13:18]:
            label["bg"] = "#DCDCDC"

        self.textos = []
        for texto in range(0,17):
            self.textos.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos:
            parameters.place(x=460, y=i, width=60)
            i += 30

        self.base_path = pathlib.Path(__file__).parent.parent.resolve()
        self.image_filename = resource_path('images\\Freno Zapata Externa.png')
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((300,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)
        self.lbl17.place(x=1100, y=0, width=300, height=350)

        self.base_path_2nd_part = pathlib.Path(__file__).parent.parent.resolve()
        self.image_filename_2nd_part = resource_path('images\\Zapata externa ancho de cara.png')
        self.image2 = Image.open(os.path.join(self.base_path_2nd_part, self.image_filename_2nd_part))
        self.image2 = self.image2.resize((300,330), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.image2)
        self.lbl_img2 = Label(self, image=self.img2)
        self.lbl_img2.place(x=1100, y=350, width=300, height=330)

        self.labels2 = []
        textoslabels2 = ["Θa: Ángulo donde se aplica la presión máxima admisible","T: Torque debido a la fuerza de fricción",
        "Padm: Presión máxima admisible ejercida sobre el material de fricción","Fx: Componente en el eje x de la fuerza de accionamiento",
        "Fy: Componente en el eje y de la fuerza de accionamiento", "Rx: Reacción del pasador en el eje x", "Ry: Reacción del pasador en el eje y",
        "R: Reacción en el pasador", "Factor de diseño", "Factor de seguridad del pasador", "Factor de seguridad del tambor"]
        for textos in textoslabels2:
            self.labels2.append(Label(self, text=textos, bg="#808080", font=("Tahoma", 9)))
        i=200
        for cosas in self.labels2:
            cosas.place(x=590, y=i)
            i += 30
        self.labels2[9].place(x=590, y=520)
        self.labels2[9]["bg"]="#C0C0C0"
        self.labels2[10].place(x=590, y=620)
        self.labels2[10]["bg"]="#DCDCDC"

        self.textos2 = []
        for texto in range(0,11):
            self.textos2.append(Entry(self, state="disabled"))
        i=200
        for parameters in self.textos2:
            parameters.place(x=980, y=i, width=60)
            i += 30
        self.textos2[9].place(x=980, y=520)
        self.textos2[10].place(x=980, y=620)

        self.listunds2 = []
        unds2 = ["°","N.mm","MPa","N","N","N","N","N","","",""]
        for unidades in unds2:
            self.listunds2.append(Label(self, bg="#808080"))
        i=200
        for unidades in self.listunds2:
            unidades.place(x=1050, y=i)
            i += 30
        self.listunds2[9].place(x=1050, y=520)
        self.listunds2[9]["bg"] = "#C0C0C0"
        self.listunds2[10].place(x=1050, y=620)
        self.listunds2[10]["bg"] = "#DCDCDC"  

        self.lbl18 = Label(self,text='Pa', bg="#A9A9A9")
        self.lbl18.place(x=630, y=65)
        self.txt18 = Entry(self, state="disabled")
        self.txt18.place(x=650, y=65, width=60)
        self.lbl18_unidad = Label(self, bg="#A9A9A9")
        self.lbl18_unidad.place(x=710, y=65)
        self.lbl36 = Label(self)
        self.lbl36.place(x=610, y=105)

        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn3.place(x=740, y=65, width=40, height=40)
        self.solve_button = Button(self, text="Calcular", command=self.operacionesF)
        self.solve_button.place(x=950, y=650, width=50, height=50)
        self.limpiar_button = Button(self, text="Limpiar", command=self.limpiar)
        self.limpiar_button.place(x=1010, y=650, width=50, height=50)
        self.temp_button = Button(self, text="Calc.\ntemperatura", command=self.vent_temp)
        self.temp_button.place(x=870, y=650, width=75,height=50)

        self.nro_zapatas_label = Label(self, text="Número de zapatas", bg="#A9A9A9", font=("Tahoma", 9))
        self.nro_zapatas_label.place(x=800, y=10)
        self.nro_zapatas = Combobox(self, width=20, values=["1","2","3","4"], state="disabled")
        def nro_zapatas(event):
            self.zapatas = []
            for caja_de_texto in range(0,int(self.nro_zapatas.get())):
                self.zapatas.append(Entry(self))
        self.nro_zapatas.bind('<<ComboboxSelected>>', nro_zapatas)
        self.nro_zapatas.place(x=800, y=30)
        self.torque_frenado_lbl =  Label(self, text="Agregar torque necesario para frenar", bg="#A9A9A9", font=("Tahoma", 9))
        self.torque_frenado_lbl.place(x=800, y=60)
        self.torque_frenado_txt = Entry(self, state="disabled")
        self.torque_frenado_txt.place(x=1030, y=60, width=60)
        self.torque_total_lbl =  Label(self, text="Torque total de frenado de la máquina", bg="#A9A9A9", font=("Tahoma", 9))
        self.torque_total_lbl.place(x=800, y=80)
        self.torque_total_txt = Entry(self, state="disabled")
        self.torque_total_txt.place(x=1030, y=80, width=60)

        self.lbl_comparacion_torque = Label(self, bg="#A9A9A9", font=("Tahoma", 9))
        self.lbl_comparacion_torque.place(x=920, y=100)

if __name__ == "__main__":
    root = Tk()
    root.wm_title("Calculos de validacion para frenos y embragues de zapata externa")
    base_path_3rd_part = pathlib.Path(__file__).parent.parent.resolve()
    image_filename_3rd_part = resource_path("images\\Logo ANFRA.ico")
    icono = os.path.join(base_path_3rd_part, image_filename_3rd_part)
    root.iconbitmap(icono)
    ZapataExternaWindow(root).mainloop()