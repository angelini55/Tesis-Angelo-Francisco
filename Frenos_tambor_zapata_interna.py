from tkinter import *
from math import *
from sympy import *

class Application(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=800, height=500)
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

        valor1 = (a6*a3*(a5/2)/(sin(a9*(3.14/180))))*(((a8/2)*(3.14/180))-(0.25*sin(2*((a8)*(3.14/180)))))
        valor2 = (a2*a6*(a5/2)/(sin(a9*(3.14/180))))*((a5/2)-(a5/2)*cos(a8*(3.14/180))-(a3/2)*(sin(a8*(3.14/180))**2))
        pa = (a1*a4)/(valor1-valor2)
        pa = round(pa,3)

        self.txt13.delete(0,"end")
        self.txt13.insert(0,pa)

        T = (a2*pa*a6*((a5/2)**2)*(cos(a7*(3.14/180))-cos(a8*(3.14/180))))/(sin(a9*(3.14/180)))
        T = round(T,3)

        self.txt12.delete(0,"end")
        self.txt12.insert(0,T)



    def create_widget(self):
        self.lbl1 = Label(self,text='Fuerza de accionamiento"F"')
        self.lbl2 = Label(self,text='Coeficiente de friccion"µ"')
        self.lbl3 = Label(self,text='Distancia desde el pivote hasta el centro del tambor "a"')
        self.lbl4 = Label(self,text='Distancia desde el pto de aplicacion de la fuerza hasta el centro del pivote "c"')
        self.lbl5 = Label(self,text='Diametro del tambor')
        self.lbl6 = Label(self,text='Ancho de la zapata "b"')
        self.lbl7 = Label(self,text='Angulo inicial material de friccion "Θ1"')
        self.lbl8 = Label(self,text='Angulo final material de friccion "Θ2"')
        self.lbl9 = Label(self,text='Angulo de presion maxima "Θa"')
        self.lbl10 = Label(self,text='Reaccion del pasador en el eje x "Rx"')
        self.lbl11 = Label(self,text='Reaccion del pasador en el eje y "Ry"')
        self.lbl12 = Label(self,text='Torque de frenado "T"')
        self.lbl13 = Label(self,text='Presion maxima admisible "Padm"')
        self.lbl14 = Label(self,text='Factor de diseño "FD""')

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

        self.btn = Button(self, text='Solve', command = self.operaciones)

        self.lbl1.place(x=10, y=10, width=210, height=20)
        self.lbl2.place(x=10, y=40, width=210, height=20)
        self.lbl3.place(x=10, y=70, width=210, height=20)
        self.lbl4.place(x=10, y=100, width=210, height=20)
        self.lbl5.place(x=10, y=130, width=210, height=20)
        self.lbl6.place(x=10, y=160, width=210, height=20)
        self.lbl7.place(x=10, y=190, width=210, height=20)
        self.lbl8.place(x=10, y=220, width=210, height=20)
        self.lbl9.place(x=10, y=250, width=210, height=20)
        self.lbl10.place(x=10, y=280, width=210, height=20)
        self.lbl11.place(x=10, y=310, width=210, height=20)
        self.lbl12.place(x=10, y=340, width=210, height=20)
        self.lbl13.place(x=10, y=370, width=210, height=20)
        self.lbl14.place(x=10, y=400, width=210, height=20)

        self.txt1.place(x=220, y=10, width=210, height=20)
        self.txt2.place(x=220, y=40, width=210, height=20)
        self.txt3.place(x=220, y=70, width=210, height=20)
        self.txt4.place(x=220, y=100, width=210, height=20)
        self.txt5.place(x=220, y=130, width=210, height=20)
        self.txt6.place(x=220, y=160, width=210, height=20)
        self.txt7.place(x=220, y=190, width=210, height=20)
        self.txt8.place(x=220, y=220, width=210, height=20)
        self.txt9.place(x=220, y=250, width=210, height=20)
        self.txt10.place(x=220, y=280, width=210, height=20)
        self.txt11.place(x=220, y=310, width=210, height=20)
        self.txt12.place(x=220, y=340, width=210, height=20)
        self.txt13.place(x=220, y=370, width=210, height=20)
        self.txt14.place(x=220, y=400, width=210, height=20)

        self.btn.place(x=500, y=85, width=210, height=100)



root = Tk()
root.wm_title("Frenos de tambor con zapata interna")
app = Application(root)
app.mainloop()