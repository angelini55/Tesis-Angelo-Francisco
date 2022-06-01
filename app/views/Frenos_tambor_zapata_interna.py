import os
import pathlib
from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image
from .TablaMaterialesFriccionSI import TablaMaterialesSI

class ZapataInternaWindow(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=700, height=680)
        self.master = master
        self.pack()
        self.create_widget()

    def tablaSI(self):
        tabla = Toplevel()
        self.table = TablaMaterialesSI(master=tabla, parent=self)
        

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

            pa = (a1*a4)/(valor1-valor2)
            pa = round(pa,3)

            T = (a2*pa*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((pa*a6*(a5/2))/sin(a9*(3.14/180)))*(I2-(a2*I3))) - a10
            Ry = (((pa*a6*(a5/2))/sin(a9*(3.14/180)))*(I3+(a2*I2))) - a11

        if self.seleccion.get() == 2:
            
            pa = (a1*a4)/(valor1+valor2)
            pa = round(pa,3)

            T = (a2*pa*a6*((a5/2)**2)*I1)/(sin(a9*(3.14/180)))
            T = round(T,3)

            Rx = (((pa*a6*(a5/2))/sin(a9*(3.14/180)))*(I2+(a2*I3))) - a10
            Ry = (((pa*a6*(a5/2))/sin(a9*(3.14/180)))*(I3-(a2*I2))) - a11
        
        
        self.txt15.delete(0,"end")
        self.txt15.insert(0,pa)

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

        # self.labels = []
        # brakes_parmeters = ('F', 'µ', 'a', 'c', 'D', 'b', 'Θ1', 'Θ2', 'Θa', 'Fx', 'Fy', 'Rx', 'Ry', 'T', 'Padm', 'FD')
        # for parameter in brakes_parmeters:
        #    self.labels.append(Label(self, text=parameter))

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

        self.lbl20 = Label(self,text='N')
        self.lbl22 = Label(self,text='m')
        self.lbl23 = Label(self,text='m')
        self.lbl24 = Label(self,text='m')
        self.lbl25 = Label(self,text='m')
        self.lbl26 = Label(self,text='°')
        self.lbl27 = Label(self,text='°')
        self.lbl28 = Label(self,text='°')
        self.lbl29 = Label(self,text='N')
        self.lbl30 = Label(self,text='N')
        self.lbl31 = Label(self,text='N')
        self.lbl32 = Label(self,text='N')
        self.lbl33 = Label(self,text='N.m')
        self.lbl34 = Label(self,text='kPa')

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
        self.seleccion2 = IntVar()
        self.seleccion.set(1)
        self.seleccion2.set(1)
        self.radio1 = Radiobutton(self, text="autoenergizante", variable=self.seleccion, value=1)
        self.radio2 = Radiobutton(self, text="autodesenergizante", variable=self.seleccion, value=2)
        self.radio3 = Radiobutton(self, text="Sistema Internacional", variable=self.seleccion2, value=1)
        self.radio4 = Radiobutton(self, text="Sistema Ingles", variable=self.seleccion2, value=2)

        self.opciones = ["Dada F, hallar T y Padm", "Dada T, hallar F y Padm", "Dada Padm, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="readonly" )
        def callback(event): 
            if self.list.get() == self.opciones[0]:
                self.lbl1.config(text="F")
                self.lbl14.config(text="T")
                self.lbl15.config(text="Padm")
                self.btn.config(command=self.operacionesF)
            elif self.list.get() == self.opciones[1]:
                self.lbl1.config(text="T")
                self.lbl14.config(text="F")
                self.lbl15.config(text="Padm")
            elif self.list.get() == self.opciones[2]:
                self.lbl1.config(text="Padm")
                self.lbl14.config(text="T")
                self.lbl15.config(text="F") 
                self.btn.config(command=self.operacionesPadm)
        self.list.bind('<<ComboboxSelected>>', callback)
        self.list.current(0)

        self.btn = Button(self, text='Solve', command = self.operacionesF)
        self.btn2 = Button(self, text='?', command = self.ayuda)
        self.btn3 = Button(self, text='tabla', command=self.tablaSI)

        self.base_path = pathlib.Path(__file__).parent.parent.resolve()
        self.image_filename = 'Freno.png'
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((350,350), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)
        self.lbl17 = Label(self, image=self.img)

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
        self.btn2.place(x=200, y=60, width=40, height=40)
        self.btn3.place(x=200, y=540, width=40, height=40)
        
        self.radio1.place(x=15, y=10,)
        self.radio2.place(x=15, y=30,)
        self.radio3.place(x=150, y=10,)
        self.radio4.place(x=150, y=30,)

        self.list.place(x=30, y=400)   



# if __name__ == "__main__":
#     root = Tk()
#     root.wm_title("Frenos de tambor con zapata interna")
#     ZapataInternaWindow(root).mainloop()
