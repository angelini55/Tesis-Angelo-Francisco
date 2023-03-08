import os
import pathlib
from tkinter import *
from tkinter import messagebox
from PIL import Image, ImageTk
from views_analisis.Frenos_tambor_zapata_interna_dos import ZapataInternaWindow
from views_analisis.Frenos_Tambor_zapata_externa import ZapataExternaWindow
from views_analisis.Zapata_Externa_Simetrica import ZapataESimetricaWindow
from views_analisis.Frenos_Banda import BandaWindow
from views_analisis.Frenos_Disco import DiscoWindow
from views_analisis.Frenos_Zapata_Anular import ZapataAnularWindow
from views_analisis.Freno_Conico import ConicoWindow
from views_analisis.Frenos_Zapata_Circular import CircularWindow
from app_path import resource_path_prymary

def track_active_window(menu_func):
    def inner(*args):
        if not args[0].active_window:
            args[0].active_window = menu_func(args[0])
            args[0].active_window.protocol("WM_DELETE_WINDOW", args[0].on_close_window)
    return inner

class Seleccion(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1020)
        self.master = master
        self.pack()
        self.create_widget()
        self.active_window = None

    def info(self):
        self.mensaje = """Programa que resuelve casos generales, tomando en
cuenta cada zapata individualmente, sobre las cuales actúan
unicamente fuerzas horizontales o verticales; para
posteriormente calcular el torque de frenado, con un sistema
de referencia que coincide con el pasador"""
        messagebox.showinfo(title="Aclaratoria", message=self.mensaje, parent=self)


    def on_close_window(self):
        self.active_window.destroy()
        self.active_window = None


    @track_active_window
    def menu1(self):
        self.active_window = Toplevel()
        ZapataInternaWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de zapata interna")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window
    def menu2(self):
        self.active_window = Toplevel()
        ZapataExternaWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de zapata externa")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window
    def menu2_5(self):
        self.active_window = Toplevel()
        ZapataESimetricaWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de zapata externa simetrica")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window
    def menu3(self):
        self.active_window = Toplevel()
        BandaWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de banda")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window   
    def menu4(self):
        self.active_window = Toplevel()
        DiscoWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de disco")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window
    def menu5(self):
        self.active_window = Toplevel()
        ZapataAnularWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de mordaza con zapata anular")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window
    
    @track_active_window
    def menu6(self):
        self.active_window = Toplevel()
        CircularWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues de mordaza con zapata circular")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    @track_active_window    
    def menu7(self):
        self.active_window = Toplevel()
        ConicoWindow(self.active_window)
        self.active_window.resizable(0,0)
        self.active_window.title("Cálculos de validación para frenos y embragues conicos")
        self.active_window.update()
        w = self.active_window.winfo_width()
        h = self.active_window.winfo_height()
        ws = self.active_window.winfo_screenwidth()
        hs = self.active_window.winfo_screenheight()
        x = int((ws/2) - (w/2))
        y = int((hs/2) - (h/2))
        self.active_window.geometry(f"{w}x{h}+{x}+{y}")
        return self.active_window

    
    def create_widget(self):

        self.image_filename = resource_path_prymary('images\\Zapata interna diseño.png')
        self.base_path = pathlib.Path(__file__).parent.resolve()
        self.image = Image.open(os.path.join(self.base_path, self.image_filename))
        self.image = self.image.resize((50,50), Image.Resampling.LANCZOS)
        self.img = ImageTk.PhotoImage(self.image)

        self.image_filename2 = resource_path_prymary('images\\Zapata externa real.png')
        self.base_path2 = pathlib.Path(__file__).parent.resolve()
        self.image2 = Image.open(os.path.join(self.base_path2, self.image_filename2))
        self.image2 = self.image2.resize((50,50), Image.Resampling.LANCZOS)
        self.img2 = ImageTk.PhotoImage(self.image2)

        self.image_filename3 = resource_path_prymary('images\\Freno Zapata Externa Simetrica.png')
        self.base_path3 = pathlib.Path(__file__).parent.resolve()
        self.image3 = Image.open(os.path.join(self.base_path3, self.image_filename3))
        self.image3 = self.image3.resize((50,50), Image.Resampling.LANCZOS)
        self.img3 = ImageTk.PhotoImage(self.image3)

        self.image_filename4 = resource_path_prymary('images\\Freno banda diseño.png')
        self.base_path4 = pathlib.Path(__file__).parent.resolve()
        self.image4 = Image.open(os.path.join(self.base_path4, self.image_filename4))
        self.image4 = self.image4.resize((50,50), Image.Resampling.LANCZOS)
        self.img4 = ImageTk.PhotoImage(self.image4)

        self.image_filename5 = resource_path_prymary('images\\Freno disco diseño.png')
        self.base_path5 = pathlib.Path(__file__).parent.resolve()
        self.image5 = Image.open(os.path.join(self.base_path5, self.image_filename5))
        self.image5 = self.image5.resize((50,50), Image.Resampling.LANCZOS)
        self.img5 = ImageTk.PhotoImage(self.image5)

        self.image_filename6 = resource_path_prymary('images\\Freno zapata anular diseño.png')
        self.base_path6 = pathlib.Path(__file__).parent.resolve()
        self.image6 = Image.open(os.path.join(self.base_path6, self.image_filename6))
        self.image6 = self.image6.resize((50,50), Image.Resampling.LANCZOS)
        self.img6 = ImageTk.PhotoImage(self.image6)

        self.image_filename7 = resource_path_prymary('images\\Freno Zapata Circular.png')
        self.base_path7 = pathlib.Path(__file__).parent.resolve()
        self.image7 = Image.open(os.path.join(self.base_path7, self.image_filename7))
        self.image7 = self.image7.resize((50,50), Image.Resampling.LANCZOS)
        self.img7 = ImageTk.PhotoImage(self.image7)

        self.image_filename8 = resource_path_prymary('images\\Freno conico diseño.png')
        self.base_path8 = pathlib.Path(__file__).parent.resolve()
        self.image8 = Image.open(os.path.join(self.base_path8, self.image_filename8))
        self.image8 = self.image8.resize((50,50), Image.Resampling.LANCZOS)
        self.img8 = ImageTk.PhotoImage(self.image8)

        self.btn1 = Button(self, text="Frenos y embragues de tambor con zapata interna expansible", command=self.menu1, width=80)
        self.btn2 = Button(self, text="Frenos y embragues de tambor con zapatas exteriores contráctiles", command=self.menu2, width=80)
        self.btn2_5 = Button(self, text="Caso especial: Freno y embrague de tambor con zapata externa de pivote simétrico", command=self.menu2_5, width=80)
        self.btn3 = Button(self, text="Frenos y embragues de banda", command=self.menu3, width=80)
        self.btn4 = Button(self, text="Frenos y embragues de disco", command=self.menu4, width=80)
        self.btn5 = Button(self, text="Frenos y embragues de mordaza con zapata anular", command=self.menu5, width=80)
        self.btn6 = Button(self, text="Frenos y embragues de mordaza con zapata circular", command=self.menu6, width=80)
        self.btn7 = Button(self, text="Frenos y embragues cónicos", command=self.menu7, width=80)

        self.img_button1 = Button(self, image=self.img, width=50, height=50)
        self.img_button1.grid(row=0, column=1, pady=5)

        self.img_button2 = Button(self, image=self.img2, width=50, height=50)
        self.img_button2.grid(row=1, column=1, pady=5)

        self.img_button3 = Button(self, image=self.img3, width=50, height=50)
        self.img_button3.grid(row=2, column=1, pady=5)

        self.img_button4 = Button(self, image=self.img4, width=50, height=50)
        self.img_button4.grid(row=3, column=1, pady=5)

        self.img_button5 = Button(self, image=self.img5, width=50, height=50)
        self.img_button5.grid(row=4, column=1, pady=5)

        self.img_button6 = Button(self, image=self.img6, width=50, height=50)
        self.img_button6.grid(row=5, column=1, pady=5)

        self.img_button7 = Button(self, image=self.img7, width=50, height=50)
        self.img_button7.grid(row=6, column=1, pady=5)

        self.img_button8 = Button(self, image=self.img8, width=50, height=50)
        self.img_button8.grid(row=7, column=1, pady=5)

        self.btn1.config(height=3, font=("tahoma", 10))
        self.btn2.config(height=3, font=("tahoma", 10))
        self.btn2_5.config(height=3, font=("tahoma", 10))
        self.btn3.config(height=3, font=("tahoma", 10))
        self.btn4.config(height=3, font=("tahoma", 10))
        self.btn5.config(height=3, font=("tahoma", 10))
        self.btn6.config(height=3, font=("tahoma", 10))
        self.btn7.config(height=3, font=("tahoma", 10))

        self.btn1.grid(row=0, pady=5)
        self.btn2.grid(row=1, pady=10)
        self.btn2_5.grid(row=2, pady=10)
        self.btn3.grid(row=3, pady=10)
        self.btn4.grid(row=4, pady=10)
        self.btn5.grid(row=5, pady=10)
        self.btn6.grid(row=6, pady=10)
        self.btn7.grid(row=7, pady=10)

        self.btn_info = Button(self, text="Nota", command=self.info, width=4, bg="yellow")
        self.btn_info.grid(row=0, column=2, padx=10)


if __name__ == "__main__":
    raiz = Tk()
    raiz.wm_title("Menu de seleccion")
    Seleccion(raiz).mainloop()
