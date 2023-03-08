import os
import pathlib
from math import *
from tkinter import *
from tkinter import PhotoImage, messagebox

from PIL import Image, ImageTk

from Menu_de_seleccion import Seleccion
from Menu_de_seleccion_diseño import SeleccionDiseño

from app_path import resource_path_prymary

vent = Tk()
vent.geometry("1200x700")
vent.title("Programa Frenos y embragues")
vent.resizable(False,False)
vent.focus_force()

desc = Tk()
desc.geometry("550x400")
desc.title("Bienvenido")
desc.attributes("-topmost", True)
desc.resizable(0,0)


lbl_desc = Label(desc, text="""A continuación se presentarán una serie de cálculos técnicos a traves de un programa
de ingenieria, orientados a frenos y embragues, los cuales le facilitaran al usuario
resolver problemas de forma rapida y sencilla. Todos estos cálculos guian a los usuarios
de manera confiable, precisa y rapida a traves de los pasos para el análisis y diseño de
frenos y embragues. El programa ofrece cálculos de diseño y validación para los frenos y
embragues mas comunes como los son:
1. Frenos y embragues de tambor con zapata interna
2. Frenos y embragues de tambor con zapata externa
3. Frenos de banda
4. Frenos de disco
5. Frenos de zapata anular
6. Frenos de zapata circular
7. Frenos cónicos""", justify="left", font=("Tahoma", 10))
lbl_desc.pack()

def Portada():
    desc.destroy()


btn_desc = Button(desc, text="Cerrar", command=Portada)
btn_desc.pack()

canvas =  Canvas(width=800, height=500, bg='#C0C0C0')
canvas.pack(expand=YES, fill=BOTH)

base_path2 = pathlib.Path(__file__).parent.resolve()
image_filename2 = resource_path_prymary('images\\Freno Portada.png')
image2 = Image.open(os.path.join(base_path2, image_filename2))
image2 = image2.resize((450,400), Image.Resampling.LANCZOS)
imga = ImageTk.PhotoImage(image2)
lbl4 = Label(vent, image=imga)
lbl4.place(x=40, y=140)

txtlbl = """Universidad del Zulia
Facultad de Ingeniería
Escuela de ingeniería mecánica
Departamento de diseño y construcciones mecánicas"""

lbl = Label(vent, text=txtlbl, font=("Tahoma", 18), bg="#C0C0C0")
lbl.place(x=160, y=10)

canvas.create_polygon(1030,0,400,700,600,700,1200,600,1200,0, fill="#4682B4")

lbl2text = """Programa para el análisis y diseño de 
frenos y embragues"""
lbl2 = Label(vent, text=lbl2text, font=("Tahoma", 18), bg="#4682B4")
lbl2.place(x=780, y=330)

lbl3text = "Angelo Musio,\n Francisco Barrios.\n 2022, ver. para Windows"
lbl3 = Label(vent, text=lbl3text, font=("Tahoma", 18), bg="#C0C0C0")
lbl3.place(x=80, y=570)

base_path = pathlib.Path(__file__).parent.resolve()
image_filename = resource_path_prymary('images\\Logo Luz 2.png')
image = Image.open(os.path.join(base_path, image_filename))
image = image.resize((150,150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(image)
lbl3 = Label(vent, image=img)
lbl3.place(x=1000, y=80)

base_path3 = pathlib.Path(__file__).parent.resolve()
image_filename3 = resource_path_prymary('images\\Logo ANFRA.png')
image3 = Image.open(os.path.join(base_path3, image_filename3))
image3 = image3.resize((100,50), Image.Resampling.LANCZOS)
img3 = ImageTk.PhotoImage(image3)
lbl5 = Label(vent, image=img3)
lbl5.place(x=1050, y=630)
    
def lista_Analisis():
    taro = Toplevel()
    taro.title("Menú de selección para Analisis")
    Seleccion(taro)

def lista_diseño():
    taro = Toplevel()
    taro.title("Menú de selección para Diseño")
    SeleccionDiseño(taro)

btn = Button(vent, text="Análisis", command=lista_Analisis, font=("tahoma", 12), bd=4)
btn.place(x=870, y=450, width=100, height=70)

btn2 = Button(vent, text="Diseño", command=lista_diseño, font=("tahoma", 12), bd=4)
btn2.place(x=1040, y=450, width=100, height=70)

    

if __name__ == "__main__":
    vent.mainloop()
    desc.mainloop()