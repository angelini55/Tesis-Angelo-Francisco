from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Combobox; PhotoImage; Combobox
from math import *
from PIL import ImageTk, Image

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=800, height=700)
        self.master = master
        self.pack()
        self.create_widget()
        

    def operaciones(self):
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

        self.seleccion = IntVar()
        self.seleccion.set(1)
        self.radio1 = Radiobutton(self, text="autoenergizante", variable=self.seleccion, value=1)
        self.radio2 = Radiobutton(self, text="autodesenergizante", variable=self.seleccion, value=2)

        self.opciones = ["Dada F, hallar T y PD", "Dada T, hallar F y PD", "Dada PD, hallar F y T"]
        self.list = Combobox(self, width=25, values=self.opciones, state="readonly" )

        self.btn = Button(self, text='Solve', command = self.operaciones)
        self.btn2 = Button(self, text='?', command = self.ayuda)

        self.image = Image.open("C:\\Users\\angel\\Desktop\\Codigo_python\\Freno.png")
        self.image = self.image.resize((400,400), Image.ANTIALIAS)
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
        self.lbl12.place(x=10, y=540, width=50, height=20)
        self.lbl13.place(x=10, y=570, width=50, height=20)
        self.lbl14.place(x=10, y=600, width=50, height=20)
        self.lbl15.place(x=10, y=630, width=50, height=20)
        self.lbl16.place(x=10, y=660, width=50, height=20)
        self.lbl17.place(x=400, y=10, width=400, height=400)
        

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
        self.txt12.place(x=70, y=540, width=80, height=20)
        self.txt13.place(x=70, y=570, width=80, height=20)
        self.txt14.place(x=70, y=600, width=80, height=20)
        self.txt15.place(x=70, y=630, width=80, height=20)
        self.txt16.place(x=70, y=660, width=80, height=20)

        self.btn.place(x=500, y=450, width=150, height=100)
        self.btn2.place(x=280, y=10, width=40, height=40)
        
        self.radio1.place(x=130, y=10,)
        self.radio2.place(x=130, y=30,)

        self.list.place(x=30, y=400)        



if __name__ == "__main__":
    root = Tk()
    root.wm_title("Frenos de tambor con zapata interna")
    Application(root).mainloop()
