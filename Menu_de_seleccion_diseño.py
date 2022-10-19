from tkinter import *
from tkinter import messagebox
from views_diseño.diseño_freno_zapata_interna import ZapataInternaWindow_diseño
from views_diseño.diseño_freno_zapata_externa import ZapataExternaWindow_diseño
from views_diseño.diseño_zapata_externa_simetrica import ZapataExternaSimetricaWindow_diseño
from views_diseño.diseño_freno_banda import FrenoBandaWindow_diseño
from views_diseño.diseño_freno_disco import FrenoDiscoWindow_diseño
from views_diseño.diseño_freno_zapata_anular import FrenoZapataAnularWindow_diseño
from views_diseño.diseño_freno_conico import FrenoConicoWindow_diseño
from views_diseño.diseño_freno_zapata_circular import FrenoZapataCircularWindow_diseño

def track_active_window(menu_func):
    def inner(*args):
        if not args[0].active_window:
            args[0].active_window = menu_func(args[0])
            args[0].active_window.protocol("WM_DELETE_WINDOW", args[0].on_close_window)
    return inner

class SeleccionDiseño(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=1000)
        self.master = master
        self.pack()
        self.create_widget()
        self.active_window = None

    def info(self):
        self.mensaje = """Programa que resuelve casos generales tomando en cuenta cada zapata individualmente,
sobre las cuales actuan unicamente fuerzas horizontales o verticales; para posteriormente calcular el torque de frenado,
Con un sistema de referencia que coincide con el pasador"""
        messagebox.showinfo(title="Aclaratoria", message=self.mensaje)

    def on_close_window(self):
        self.active_window.destroy()
        self.active_window = None


    @track_active_window
    def menu1(self):
        self.active_window = Toplevel()
        ZapataInternaWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu2(self):
        self.active_window = Toplevel()
        ZapataExternaWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu2_5(self):
        self.active_window = Toplevel()
        ZapataExternaSimetricaWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu3(self):
        self.active_window = Toplevel()
        FrenoBandaWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window   
    def menu4(self):
        self.active_window = Toplevel()
        FrenoDiscoWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu5(self):
        self.active_window = Toplevel()
        FrenoZapataAnularWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window
    
    @track_active_window
    def menu6(self):
        self.active_window = Toplevel()
        FrenoZapataCircularWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window    
    def menu7(self):
        self.active_window = Toplevel()
        FrenoConicoWindow_diseño(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    
    def create_widget(self):

        self.btn1 = Button(self, text="Frenos y embragues de tambor con zapata interna expansible", command=self.menu1, width=100)
        self.btn2 = Button(self, text="Frenos y embragues de tambor con zapatas exteriores contractiles", command=self.menu2, width=100)
        self.btn2_5 = Button(self, text="Caso especial: pivote simetrico", command=self.menu2_5, width=100)
        self.btn3 = Button(self, text="Frenos y embragues de banda", command=self.menu3, width=100)
        self.btn4 = Button(self, text="Frenos y embragues de disco", command=self.menu4, width=100)
        self.btn5 = Button(self, text="Frenos y embragues de mordaza con zapata anular", command=self.menu5, width=100)
        self.btn6 = Button(self, text="Frenos y embragues de mordaza con zapata circular", command=self.menu6, width=100)
        self.btn7 = Button(self, text="Frenos y embragues conicos", command=self.menu7, width=100)

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

        self.btn_info = Button(self, text="!", command=self.info, width=2, bg="yellow")
        self.btn_info.grid(row=0, column=1, padx=10)


if __name__ == "__main__":
    raiz = Tk()
    raiz.wm_title("Menu de seleccion")
    SeleccionDiseño(raiz).mainloop()
