from tkinter import *
from tkinter import messagebox; PhotoImage
from math import *
from PIL import ImageTk, Image
from Frenos_tambor_zapata_interna_energizante_V3 import Application
from Menu_de_seleccion import Seleccion


vent = Tk()
vent.geometry("800x500")
vent.title("Programa Frenos")

txtlbl = """Universidad del Zulia
Facultad de Ingenieria
Escuela de ingenieria mecanica
Departamento de diseño y construcciones mecanicas"""

lbl = Label(vent, text=txtlbl)
lbl.place(x=250, y=50)

lbl2 = Label(vent, text="Programa para el analisis y diseño de frenos y embragues")
lbl2.place(x=250, y=250)

image = Image.open("C:\\Users\\angel\\Desktop\\Codigo_python\\Logo_LUZ.png")
image = image.resize((200,200), Image.ANTIALIAS)
img = ImageTk.PhotoImage(image)
lbl3 = Label(vent, image=img)
lbl3.place(x=1, y=1)
    
def lista():
    taro = Toplevel()
    Seleccion(taro)

btn = Button(vent, text="Analisis", command=lista)
btn.place(x=150, y=350)

btn2 = Button(vent, text="Diseño")
btn2.place(x=600, y=350)

    

if __name__ == "__main__":
    vent.mainloop()

    







