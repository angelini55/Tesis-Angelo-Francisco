import os
import pathlib
from tkinter import *
from tkinter import messagebox; PhotoImage
from math import *
from PIL import ImageTk, Image
from Frenos_tambor_zapata_interna import ZapataInternaWindow
from Menu_de_seleccion import Seleccion


vent = Tk()
vent.geometry("800x500")
vent.title("Programa Frenos")
#vent.iconbitmap(r'C:\Users\angel\Desktop\Codigo_python\Logo_LUZ.ico')

canvas =  Canvas(width=800, height=500, bg='#C0C0C0')
canvas.pack(expand=YES, fill=BOTH)

base_path2 = pathlib.Path(__file__).parent.resolve()
image_filename2 = 'images\\Freno Portada.png'
image2 = Image.open(os.path.join(base_path2, image_filename2))
image2 = image2.resize((250,200), Image.Resampling.LANCZOS)
imga = ImageTk.PhotoImage(image2)
lbl4 = Label(vent, image=imga)
lbl4.place(x=40, y=140)

txtlbl = """Universidad del Zulia
Facultad de Ingenieria
Escuela de ingenieria mecanica
Departamento de diseño y construcciones mecanicas"""

lbl = Label(vent, text=txtlbl, font=("Tahoma", 15), bg="#C0C0C0")
lbl.place(x=110, y=10)

canvas.create_polygon(730,0,100,500,200,500,800,400,800,0, fill="#4682B4")

lbl2text = """Frenos y
Embragues"""
lbl2 = Label(vent, text=lbl2text, font=("Tahoma", 15), bg="#4682B4")
lbl2.place(x=540, y=250)

base_path = pathlib.Path(__file__).parent.resolve()
image_filename = 'images\\Logo Luz 2.png'
image = Image.open(os.path.join(base_path, image_filename))
image = image.resize((150,150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(image)
lbl3 = Label(vent, image=img)
lbl3.place(x=635, y=80)

base_path3 = pathlib.Path(__file__).parent.resolve()
image_filename3 = 'images\\Logo ANFRA.png'
image3 = Image.open(os.path.join(base_path3, image_filename3))
image3 = image3.resize((100,50), Image.Resampling.LANCZOS)
img3 = ImageTk.PhotoImage(image3)
lbl5 = Label(vent, image=img3)
lbl5.place(x=630, y=430)
    
def lista():
    taro = Toplevel()
    taro.title("Menu de seleccion")
    Seleccion(taro)

btn = Button(vent, text="Analisis", command=lista, font=("tahoma", 10), bd=4)
btn.place(x=470, y=350)

btn2 = Button(vent, text="Diseño", font=("tahoma", 10), bd=4)
btn2.place(x=640, y=350)

    

if __name__ == "__main__":
    vent.mainloop()

    







