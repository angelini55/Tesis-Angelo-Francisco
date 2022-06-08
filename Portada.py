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
vent.iconbitmap(r'C:\Users\angel\Desktop\Codigo_python\Logo_LUZ.ico')

txtlbl = """Universidad del Zulia
Facultad de Ingenieria
Escuela de ingenieria mecanica
Departamento de diseño y construcciones mecanicas"""

lbl = Label(vent, text=txtlbl, font=("Tahoma", 15))
lbl.place(x=170, y=50)

lbl2 = Label(vent, text="Programa para el analisis y diseño de frenos y embragues", font=("Tahoma", 15))
lbl2.place(x=170, y=250)

base_path = pathlib.Path(__file__).parent.resolve()
image_filename = 'Logo_LUZ.png'
image = Image.open(os.path.join(base_path, image_filename))
image = image.resize((150,150), Image.Resampling.LANCZOS)
img = ImageTk.PhotoImage(image)
lbl3 = Label(vent, image=img)
lbl3.place(x=1, y=1)
    
def lista():
    taro = Toplevel()
    Seleccion(taro)

btn = Button(vent, text="Analisis", command=lista)
btn.place(x=170, y=350)

btn2 = Button(vent, text="Diseño")
btn2.place(x=620, y=350)

    

if __name__ == "__main__":
    vent.mainloop()

    







