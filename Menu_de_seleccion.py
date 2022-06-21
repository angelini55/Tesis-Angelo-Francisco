from tkinter import *
from tkinter import messagebox
from Frenos_tambor_zapata_interna import ZapataInternaWindow
from Frenos_Tambor_zapata_externa import ZapataExternaWindow
from Zapata_Externa_Simetrica import ZapataESimetricaWindow
from Frenos_Banda import BandaWindow
from Frenos_Disco import DiscoWindow
from Frenos_Zapata_Anular import ZapataAnularWindow
from Freno_Conico import ConicoWindow

def track_active_window(menu_func):
    def inner(*args):
        if not args[0].active_window:
            args[0].active_window = menu_func(args[0])
            args[0].active_window.protocol("WM_DELETE_WINDOW", args[0].on_close_window)
    return inner

class Seleccion(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=500, height=500)
        self.master = master
        self.pack()
        self.create_widget()
        self.active_window = None

    def on_close_window(self):
        self.active_window.destroy()
        self.active_window = None


    @track_active_window
    def menu1(self):
        self.active_window = Toplevel()
        ZapataInternaWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu2(self):
        self.active_window = Toplevel()
        ZapataExternaWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu2_5(self):
        self.active_window = Toplevel()
        ZapataESimetricaWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu3(self):
        self.active_window = Toplevel()
        BandaWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window   
    def menu4(self):
        self.active_window = Toplevel()
        DiscoWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window
    def menu5(self):
        self.active_window = Toplevel()
        ZapataAnularWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    @track_active_window    
    def menu7(self):
        self.active_window = Toplevel()
        ConicoWindow(self.active_window)
        self.active_window.resizable(0,0)
        return self.active_window

    
    def create_widget(self):

        self.btn1 = Button(self, text="Frenos y embragues de tambor con zapata interna expansible", height=5,  command=self.menu1)
        self.btn2 = Button(self, text="Frenos y embragues de tambor con zapatas exteriores contractiles", height=5, command=self.menu2)
        self.btn2_5 = Button(self, text="Caso especial: pivote simetrico", height=5, command=self.menu2_5)
        self.btn3 = Button(self, text="Frenos y embragues de banda", height=5, command=self.menu3)
        self.btn4 = Button(self, text="Frenos y embragues de disco", height=5, command=self.menu4)
        self.btn5 = Button(self, text="Frenos y embragues de mordaza con zapata anular", height=5, command=self.menu5)
        self.btn6 = Button(self, text="Frenos y embragues de mordaza con zapata circular", height=5)
        self.btn7 = Button(self, text="Frenos y embragues conicos", height=5, command=self.menu7)

        self.btn1.config(height=1)
        self.btn2.config(height=1)
        self.btn2_5.config(height=1)
        self.btn3.config(height=1)
        self.btn4.config(height=1)
        self.btn5.config(height=1)
        self.btn6.config(height=1)
        self.btn7.config(height=1)

        self.btn1.grid(row=0, pady=5)
        self.btn2.grid(row=1, pady=10)
        self.btn2_5.grid(row=2, pady=10)
        self.btn3.grid(row=3, pady=10)
        self.btn4.grid(row=4, pady=10)
        self.btn5.grid(row=5, pady=10)
        self.btn6.grid(row=6, pady=10)
        self.btn7.grid(row=7, pady=10)

        #self.btn1.place(x=70, y=10, width=400, height=50)
        #self.btn2.place(x=230, y=70, width=100, height=50)
        #self.btn3.place(x=230, y=130, width=100, height=50)
        #self.btn4.place(x=230, y=190, width=100, height=50)
        #self.btn5.place(x=230, y=250, width=100, height=50)
        #self.btn6.place(x=230, y=310, width=100, height=50)
        #self.btn7.place(x=230, y=370, width=100, height=50)

if __name__ == "__main__":
    raiz = Tk()
    raiz.wm_title("Menu de seleccion")
    Seleccion(raiz).mainloop()
