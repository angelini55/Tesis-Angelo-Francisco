from tkinter import *
from Frenos_tambor_zapata_interna_energizante_V3 import Application


class Seleccion(Frame):

    def __init__(self, master=None):
        super().__init__(master, width=500, height=500)
        self.master = master
        self.pack()
        self.create_widget()
    
    def create_widget(self):

        def menu1():
            taro = Toplevel()
            Application(taro)

        self.btn1 = Button(self, text="Frenos y embragues de tambor con zapata interna expansible", height=5,  command=menu1)
        self.btn2 = Button(self, text="Frenos y embragues de tambor con zapatas exteriores contractiles",height=5)
        self.btn3 = Button(self, text="Frenos y embragues de banda",height=5)
        self.btn4 = Button(self, text="Frenos y embragues de disco",height=5)
        self.btn5 = Button(self, text="Frenos y embragues de mordaza con zapata anular",height=5)
        self.btn6 = Button(self, text="Frenos y embragues de mordaza con zapata circular",height=5)
        self.btn7 = Button(self, text="Frenos y embragues conicos",height=5)

        self.btn1.grid(row=0, pady=10)
        self.btn2.grid(row=1, pady=10)
        self.btn3.grid(row=2, pady=10)
        self.btn4.grid(row=3, pady=10)
        self.btn5.grid(row=4, pady=10)
        self.btn6.grid(row=5, pady=10)
        self.btn7.grid(row=6, pady=10)

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