import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from TablaMaterialesFriccionSI import TablaMaterialesSI
from TablaMaterialesFriccionIngles import TablaMaterialesIngles

class ZapataInternaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=680)
        self.master = master
        self.pack()
        self.create_widget()

    def tablaMaterial(self):
        if self.list2.get() == self.listaUnds[0]:
            tabla = Toplevel()
            self.table = TablaMaterialesSI(tabla, self)
        if self.list2.get() == self.listaUnds[1]:
            tabla = Toplevel()
            self.table = TablaMaterialesIngles(tabla, self)

    def CalcFD(self):
        Pa = float(self.txt18.get())
        if self.list.get() == self.opciones[2]:
            Fdiseño = Pa/float(self.txt1.get())
            self.txt16.delete(0,"end")
            self.txt16.insert(0,Fdiseño)
        else:
            Fdiseño = Pa/float(self.txt15.get())
            self.txt16.delete(0,"end")
            self.txt16.insert(0,Fdiseño)

    def operacionesT(self):
        a1 = float(self.txt1.get())
        a2 = float(self.txt2.get())
        a3 = float(self.txt3.get())
        a4 = float(self.txt4.get())
        a5 = float(self.txt5.get())
        a6 = float(self.txt6.get())
        a7 = float(self.txt7.get())
        a8 = float(self.txt8.get())
        a9 = float(self.txt9.get())
        a10 = float(self.txt10.get())
        a11 = float(self.txt11.get())

        I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
        I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
        I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

        Padm = (a1*sin(a9*(3.14/180)))/(a2*a6*((a5/2)**2)*I1)

        Mn = (Padm*a6*a3*(a5/2)/(sin(a9*(pi/180))))*I3
        Mf = (a2*Padm*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

        if self.seleccion.get() == 1:
            F = (Mn-Mf)/a4
            F = round(F,3)

            Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - a10
            Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - a11
        
        if self.seleccion.get() == 2:
            F = (Mn+Mf)/a4
            F = round(F,3)

            Rx = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - a10
            Ry = (((Padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - a11
        
        self.txt14.delete(0,"end")
        self.txt14.insert(0,F)

        self.txt15.delete(0,"end")
        self.txt15.insert(0,Padm)

        self.txt12.delete(0,"end")
        self.txt12.insert(0,Rx)
        self.txt13.delete(0,"end")
        self.txt13.insert(0,Ry)
    
    def operacionesPadm(self):
        a1 = float(self.txt1.get())
        a2 = float(self.txt2.get())
        a3 = float(self.txt3.get())
        a4 = float(self.txt4.get())
        a5 = float(self.txt5.get())
        a6 = float(self.txt6.get())
        a7 = float(self.txt7.get())
        a8 = float(self.txt8.get())
        a9 = float(self.txt9.get())
        a10 = float(self.txt10.get())
        a11 = float(self.txt11.get())

        I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
        I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
        I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

        Mn = (a1*a6*a3*(a5/2)/(sin(a9*(3.14/180))))*I3
        Mf = (a2*a1*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

        if self.seleccion.get() == 1:
            F = (Mn-Mf)/a4
            F = round(F,3)

            T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - a10
            Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - a11
        
        if self.seleccion.get() == 2:
            F = (Mn+Mf)/a4
            F = round(F,3)

            T = (a2*a1*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - a10
            Ry = (((a1*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - a11

        self.txt15.delete(0,"end")
        self.txt15.insert(0,F)

        self.txt14.delete(0,"end")
        self.txt14.insert(0,T)

        
        self.txt12.delete(0,"end")
        self.txt12.insert(0,Rx)
        self.txt13.delete(0,"end")
        self.txt13.insert(0,Ry)
        

    def operacionesF(self):
        a1 = float(self.txt1.get())
        a2 = float(self.txt2.get())
        a3 = float(self.txt3.get())
        a4 = float(self.txt4.get())
        a5 = float(self.txt5.get())
        a6 = float(self.txt6.get())
        a7 = float(self.txt7.get())
        a8 = float(self.txt8.get())
        a9 = float(self.txt9.get())
        a10 = float(self.txt10.get())
        a11 = float(self.txt11.get())

        I1 = -cos(a8*(3.14/180)) + cos(a7*(3.14/180))
        I2 = 0.5*(sin(a8*(3.14/180))**2) - 0.5*(sin(a7*(3.14/180))**2)
        I3 = ((a8/2)*(3.14/180))-0.25*sin(2*((a8)*(3.14/180))) - (((a7/2)*(3.14/180))-0.25*sin(2*((a7)*(3.14/180))))

        valor1 = (a6*a3*(a5/2)/(sin(a9*(3.14/180))))*I3
        valor2 = (a2*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)*I1 - a3*I2)

        if self.seleccion.get() == 1:

            padm = (a1*a4)/(valor1-valor2)
            padm = round(padm,3)

            T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - a10
            Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - a11

        if self.seleccion.get() == 2:
            
            padm = (a1*a4)/(valor1+valor2)
            padm = round(padm,3)

            T = (a2*padm*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - a10
            Ry = (((padm*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - a11
        
        
        self.txt15.delete(0,"end")
        self.txt15.insert(0,padm)

        self.txt14.delete(0,"end")
        self.txt14.insert(0,T)

        
        self.txt12.delete(0,"end")
        self.txt12.insert(0,Rx)
        self.txt13.delete(0,"end")
        self.txt13.insert(0,Ry)
    
    def ayuda(self):
        self.mensaje = """F: fuerza de accionamiento
µ: Coeficiente de friccion
a: Distancia desde el pivote hasta el centro del tambor
c: Distancia desde el pto de aplicacion de la fuerza hasta el centro del pivote "c" 
D: Diametro del tambor
b: Ancho de la zapata
Θ1: Angulo inicial material de friccion
Θ2: Angulo final material de friccion
Θa: Angulo de presion maxima
Fx: Componente en x de la fuerza
Fy: Componente en y de la fuerza
Rx: Reaccion del pasador en el eje x
Ry: Reaccion del pasador en el eje y
T: Torque de frenado
Padm: Presion maxima admisible
FD: Factor de diseño"""

        messagebox.showinfo(title="Ayuda", message=self.mensaje)


    def create_widget(self):

#parametros
        self.lbl1 = Label(self,text='F')
        self.lbl2 = Label(self,text='µ')
        self.lbl3 = Label(self,text='a')
        self.lbl4 = Label(self,text='c')
        self.lbl5 = Label(self,text='D')
        self.lbl6 = Label(self,text='b')
        self.lbl7 = Label(self,text='Θ1')
        self.lbl8 = Label(self,text='Θ2')
        self.lbl9 = Label(self,text='Θa')
        self.lbl10 = Label(self,text='Fx')
        self.lbl11 = Label(self,text='Fy')
        self.lbl12 = Label(self,text='Rx')
        self.lbl13 = Label(self,text='Ry')
        self.lbl14 = Label(self,text='T')
        self.lbl15 = Label(self,text='Padm')
        self.lbl16 = Label(self,text='FD')
        self.lbl18 = Label(self,text='Pa')

#unidades
        Internacional = ["N","m","m","m","m","°","°","°","N","N","N","N","N.m","Pa"]
        Ingles = ["lb","in","in","in","in","°","°","°","lb","lb","lb","lb","lb.in","PSI"]
        self.lbl20 = Label(self)
        self.lbl22 = Label(self)
        self.lbl23 = Label(self)
        self.lbl24 = Label(self)
        self.lbl25 = Label(self)
        self.lbl26 = Label(self)
        self.lbl27 = Label(self)
        self.lbl28 = Label(self)
        self.lbl29 = Label(self)
        self.lbl30 = Label(self)
        self.lbl31 = Label(self)
        self.lbl32 = Label(self)
        self.lbl33 = Label(self)
        self.lbl34 = Label(self)

        self.lbl35 = Label(self, text="Sistema de unidades")

        self.lbl36 = Label(self)

        unds=[self.lbl20,self.lbl22,self.lbl23,self.lbl24,self.lbl25,self.lbl26,self.lbl27,self.lbl28,self.lbl29,self.lbl30,self.lbl31,self.lbl32,self.lbl33,self.lbl34]

        self.txt1 = Entry(self)
        self.txt2 = Entry(self)
        self.txt3 = Entry(self)
        self.txt4 = Entry(self)
        self.txt5 = Entry(self)
        self.txt6 = Entry(self)
        self.txt7 = Entry(self)
        self.txt8 = Entry(self)
        self.txt9 = Entry(self)
        self.txt10 = Entry(self)
        self.txt11 = Entry(self)
        self.txt12 = Entry(self)
        self.txt13 = Entry(self)
        self.txt14 = Entry(self)
        self.txt15 = Entry(self)
        self.txt16 = Entry(self)
        self.txt18 = Entry(self)

        self.seleccion = IntVar()
        self.seleccion.set(1)
        self.radio1 = Radiobutton(self, text="autoenergizante", variable=self.seleccion, value=1)
        self.radio2 = Radiobutton(self, text="autodesenergizante", variable=self.seleccion, value=2)

        self.listaUnds = ["Sistema Internacional","Sistema Ingles"]
        self.list2 = Combobox(self, width=20, values=self.listaUnds, state="readonly")
        def cambioUnds(event):
            if self.list2.get() == self.listaUnds[0]:
                i=0
                for lbl in unds:
                    lbl.config(text=Internacional[i])
                    i += 1
            if self.list2.get() == self.listaUnds[1]:
                i=0
                for lbl in unds:
                    lbl.config(text=Ingles[i])
                    i += 1
        self.list2.bind('<<ComboboxSelected>>', cambioUnds)


        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="readonly")
        def callback(event): 
            if self.list.get() == self.opciones[0]:
                if self.list2.get() == self.listaUnds[0]:
                    self.lbl1.config(text="F")
                    self.lbl14.config(text="T")
                    self.lbl15.config(text="Padm")
                    self.lbl20.config(text="N")
                    self.lbl33.config(text="N.m")
                    self.lbl34.config(text="Pa")
                    self.btn.config(command=self.operacionesF)
                if self.list2.get() == self.listaUnds[1]:
                    self.lbl1.config(text="F")
                    self.lbl14.config(text="T")
                    self.lbl15.config(text="Padm")
                    self.lbl20.config(text="lb")
                    self.lbl33.config(text="lb.in")
                    self.lbl34.config(text="PSI")
                    self.btn.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                if self.list2.get() == self.listaUnds[0]:
                    self.lbl1.config(text="T")
                    self.lbl14.config(text="F")
                    self.lbl15.config(text="Padm")
                    self.lbl20.config(text="N.m")
                    self.lbl33.config(text="N")
                    self.lbl34.config(text="Pa")
                    self.btn.config(command=self.operacionesT)
                if self.list2.get() == self.listaUnds[1]:
                    self.lbl1.config(text="T")
                    self.lbl14.config(text="F")
                    self.lbl15.config(text="Padm")
                    self.lbl20.config(text="lb.in")
                    self.lbl33.config(text="lb")
                    self.lbl34.config(text="PSI")
                    self.btn.config(command=self.operacionesT)
            elif self.list.get() == self.opciones[2]:
                if self.list2.get() == self.listaUnds[0]:
                    self.lbl1.config(text="Padm")
                    self.lbl14.config(text="T")
                    self.lbl15.config(text="F") 
                    self.lbl20.config(text="Pa")
                    self.lbl33.config(text="N.m")
                    self.lbl34.config(text="N")
                    self.btn.config(command=self.operacionesPadm)
                if self.list2.get() == self.listaUnds[1]:
                    self.lbl1.config(text="Padm")
                    self.lbl14.config(text="T")
                    self.lbl15.config(text="F") 
                    self.lbl20.config(text="PSI")
                    self.lbl33.config(text="lb.in")
                    self.lbl34.config(text="lb")
                    self.btn.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(0)

        self.btn = Button(self, text='Solve', command = self.operacionesF)
        self.btn2 = Button(self, text='?', command = self.ayuda)
        self.btn3 = Button(self, text='tabla', command=self.tablaMaterial)
        self.btn4 = Button(self, text='calc', command=self.CalcFD)

        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image_filename = 'Freno.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)

#ubicar widget
        self.lbl1.place(x=10, y=70, width=50, height=20)
        self.lbl2.place(x=10, y=100, width=50, height=20)
        self.lbl3.place(x=10, y=130, width=50, height=20)
        self.lbl4.place(x=10, y=160, width=50, height=20)
        self.lbl5.place(x=10, y=190, width=50, height=20)
        self.lbl6.place(x=10, y=220, width=50, height=20)
        self.lbl7.place(x=10, y=250, width=50, height=20)
        self.lbl8.place(x=10, y=280, width=50, height=20)
        self.lbl9.place(x=10, y=310, width=50, height=20)
        self.lbl10.place(x=10, y=340, width=50, height=20)
        self.lbl11.place(x=10, y=370, width=50, height=20)
        self.lbl12.place(x=10, y=510, width=50, height=20)
        self.lbl13.place(x=10, y=540, width=50, height=20)
        self.lbl14.place(x=10, y=570, width=50, height=20)
        self.lbl15.place(x=10, y=600, width=50, height=20)
        self.lbl16.place(x=10, y=630, width=50, height=20)
        self.lbl17.place(x=300, y=10, width=350, height=350)
        self.lbl18.place(x=190, y=510, width=40, height=20)

        self.lbl20.place(x=150, y=70, width=50, height=20)
        self.lbl22.place(x=150, y=130, width=50, height=20)
        self.lbl23.place(x=150, y=160, width=50, height=20)
        self.lbl24.place(x=150, y=190, width=50, height=20)
        self.lbl25.place(x=150, y=220, width=50, height=20)
        self.lbl26.place(x=150, y=250, width=50, height=20)
        self.lbl27.place(x=150, y=280, width=50, height=20)
        self.lbl28.place(x=150, y=310, width=50, height=20)
        self.lbl29.place(x=150, y=340, width=50, height=20)
        self.lbl30.place(x=150, y=370, width=50, height=20)
        self.lbl31.place(x=150, y=510, width=50, height=20)
        self.lbl32.place(x=150, y=540, width=50, height=20)
        self.lbl33.place(x=150, y=570, width=50, height=20)
        self.lbl34.place(x=150, y=600, width=50, height=20)

        self.lbl35.place(x=155, y=15, width=120, height=20)

        self.lbl36.place(x=190, y=480, width=150, height=20)

        self.txt1.place(x=70, y=70, width=80, height=20)
        self.txt2.place(x=70, y=100, width=80, height=20)
        self.txt3.place(x=70, y=130, width=80, height=20)
        self.txt4.place(x=70, y=160, width=80, height=20)
        self.txt5.place(x=70, y=190, width=80, height=20)
        self.txt6.place(x=70, y=220, width=80, height=20)
        self.txt7.place(x=70, y=250, width=80, height=20)
        self.txt8.place(x=70, y=280, width=80, height=20)
        self.txt9.place(x=70, y=310, width=80, height=20)
        self.txt10.place(x=70, y=340, width=80, height=20)
        self.txt11.place(x=70, y=370, width=80, height=20)
        self.txt12.place(x=70, y=510, width=80, height=20)
        self.txt13.place(x=70, y=540, width=80, height=20)
        self.txt14.place(x=70, y=570, width=80, height=20)
        self.txt15.place(x=70, y=600, width=80, height=20)
        self.txt16.place(x=70, y=630, width=80, height=20)
        self.txt18.place(x=220, y=510, width=80, height=20)

        self.btn.place(x=385, y=400, width=150, height=100)
        self.btn2.place(x=200, y=70, width=40, height=40)
        self.btn3.place(x=320, y=500, width=40, height=40)
        self.btn4.place(x=280, y=550, width=40, height=40)
        
        self.radio1.place(x=15, y=10,)
        self.radio2.place(x=15, y=30,)

        self.list.place(x=30, y=400)
        self.list2.place(x=155, y=35)   



if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    ZapataInternaWindow(root).mainloop()
