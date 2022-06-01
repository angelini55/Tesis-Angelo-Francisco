from tkinter import *

vent = Tk()
vent.title('Frenos con zapata interna')
vent.geometry("1220x600")



lbl1 = Label(vent,text='Torque de frenado"T"')
lbl2 = Label(vent,text='Coeficiente de friccion"µ"')
lbl3 = Label(vent,text='Numero de zapatas')
lbl4 = Label(vent,text='Diametro del tambor')
lbl5 = Label(vent,text='Ancho de la zapata "b"')
lbl6 = Label(vent,text='Angulo inicial material de friccion "Θ1"')
lbl7 = Label(vent,text='Angulo final material de friccion "Θ2"')
lbl8 = Label(vent,text='Fuerza de accionamiento"F"')
lbl9 = Label(vent,text='Reaccion del pasador en el eje x "Rx"')
lbl10 = Label(vent,text='Reaccion del pasador en el eje y "Ry"')
lbl11 = Label(vent,text='Angulo de presion maxima "Θa"')
lbl12 = Label(vent,text='Presion maxima admisible "Padm"')
lbl13 = Label(vent,text='Fuerza ejercida en la banda')

txt1 = Entry(vent)
txt2 = Entry(vent)
txt3 = Entry(vent)
txt4 = Entry(vent)
txt5 = Entry(vent)
txt6 = Entry(vent)
txt7 = Entry(vent)
txt8 = Entry(vent)
txt9 = Entry(vent)
txt10 = Entry(vent)
txt11 = Entry(vent)
txt12 = Entry(vent)
txt13 = Entry(vent)

btn = Button(vent, text='Solve')

lbl1.place(x=10, y=10, width=210, height=20)
lbl2.place(x=10, y=40, width=210, height=20)
lbl3.place(x=10, y=70, width=210, height=20)
lbl4.place(x=10, y=100, width=210, height=20)
lbl5.place(x=10, y=130, width=210, height=20)
lbl6.place(x=10, y=160, width=210, height=20)
lbl7.place(x=10, y=190, width=210, height=20)
lbl8.place(x=10, y=220, width=210, height=20)
lbl9.place(x=10, y=250, width=210, height=20)
lbl10.place(x=10, y=280, width=210, height=20)
lbl11.place(x=10, y=310, width=210, height=20)
lbl12.place(x=10, y=340, width=210, height=20)
lbl13.place(x=10, y=370, width=210, height=20)

txt1.place(x=220, y=10, width=210, height=20)
txt2.place(x=220, y=40, width=210, height=20)
txt3.place(x=220, y=70, width=210, height=20)
txt4.place(x=220, y=100, width=210, height=20)
txt5.place(x=220, y=130, width=210, height=20)
txt6.place(x=220, y=160, width=210, height=20)
txt7.place(x=220, y=190, width=210, height=20)
txt8.place(x=220, y=220, width=210, height=20)
txt9.place(x=220, y=250, width=210, height=20)
txt10.place(x=220, y=280, width=210, height=20)
txt11.place(x=220, y=310, width=210, height=20)
txt12.place(x=220, y=340, width=210, height=20)
txt13.place(x=220, y=370, width=210, height=20)

btn.place(x=500, y=85, width=210, height=100)







vent.mainloop()