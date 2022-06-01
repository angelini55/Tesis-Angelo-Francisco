from tkinter import *
from tkinter import ttk


class TablaMaterialesSI(Frame):

    def __init__(self, master=None, parent=None):
        super().__init__(master, width=1400, height=500)
        self.master = master
        self.parent = parent
        self.pack()
        self.create_widget()

    def create_widget(self):
        
        self.table = ttk.Treeview(self, columns=("col1","col2","col3","col4","col5","col6","col7"))

        self.table.column("#0", width=100)
        self.table.column("col1", width=90)
        self.table.column("col2", width=100)
        self.table.column("col3", width=100)
        self.table.column("col4", width=100)
        self.table.column("col5", width=100)
        self.table.column("col6", width=100)
        self.table.column("col7", width=130)

        self.table.heading("#0", text="Material de friccion", anchor=CENTER)
        self.table.heading("col1", text="Material del disco", anchor=CENTER)
        self.table.heading("col2", text="P maxima MPa", anchor=CENTER)
        self.table.heading("col3", text="µ minimo humedo", anchor=CENTER)
        self.table.heading("col4", text="µ minimo seco", anchor=CENTER)
        self.table.heading("col5", text="T maxima instantanea °C", anchor=CENTER)
        self.table.heading("col6", text="T maxima continua °C", anchor=CENTER)
        self.table.heading("col7", text="Velocidad maxima m/s", anchor=CENTER)

        list1 = ["Fundicion de hierro", "1.0","0.05","0.15","700","320","7.5"]
        list2 = ["Acero", "2.1","0.05","0.1","550","350","3.6"]
        list3 = ["Fundicion de hierro", "1.0","0.05","0.1","550","350","3.6"]
        list4 = ["Acero/Fundicion de hierro", "0.4","0.16","0.2","300","150","3.0"]
        list5 = ["Acero/Fundicion de hierro", "0.070","0.12","0.3","180","100","7.5"]
        list6 = ["Acero/Fundicion de hierro", "0.050","0.15","0.3","180","100","2"]
        list7 = ["Acero/Fundicion de hierro", "0.035","0.18","0.22","250","140","5"]
        list8 = ["Acero/Fundicion de hierro", "0.35","0.10","0.3","350","175","3.6"]
        list9 = ["Acero/Fundicion de hierro", "0.35","0.08","0.2","500","260","4.8"]
        list10 = ["Acero/Fundicion de hierro", "1.0","0.12","0.32","500","260","3.6"]
        list11 = ["Acero/Fundicion de hierro", "2.1","0.05","0.25","700","370","7.5"]
        list12 = ["Acero/Fundicion de hierro", "1.0","0.10","0.32","800","390","3.6"]
        list13 = ["Acero/Fundicion de hierro", "0.6","0.12","0.38","350","150","3.6"]
        list14 = ["Acero/Fundicion de hierro", "0.6","0.12","0.38","260","125","3.6"]
        list15 = ["Acero/Fundicion de hierro", "0.6","0.15","0.47","100","70","3.6"]
        list16 = ["Acero/Fundicion de hierro", "2.6","0.09","0.15","148","65","3.6"]
        self.table.insert("", END,text="Fundicion de Hierro", values=(list1))
        self.table.insert("", END,text="Metal sinterizado", values=(list2))
        self.table.insert("", END,text="Metal sinterizado", values=(list3))
        self.table.insert("", END,text="Madera", values=(list4))
        self.table.insert("", END,text="Cuero", values=(list5))
        self.table.insert("", END,text="Corcho", values=(list6))
        self.table.insert("", END,text="Fieltro", values=(list7))
        self.table.insert("", END,text="Asbesto tejido", values=(list8))
        self.table.insert("", END,text="Asbesto moldeado", values=(list9))
        self.table.insert("", END,text="Asbesto impregnado", values=(list10))
        self.table.insert("", END,text="Grafito de carbono", values=(list11))
        self.table.insert("", END,text="Cermet", values=(list12))
        self.table.insert("", END,text="Cuerda de asbesto arrollado", values=(list13))
        self.table.insert("", END,text="Tira de asbesto tejido", values=(list14))
        self.table.insert("", END,text="Algodon tejido", values=(list15))
        self.table.insert("", END,text="Papel resilente", values=(list16))      

        self.table.place(x=0, y=0, width=1400, height=400)

        def selectItem(event):
            curItem = self.table.focus()
            sas = self.table.item(curItem)
            a12 = sas.get("values")[1]
            self.txttabla.delete(0,"end")
            self.txttabla.insert(0,a12)
            
        self.table.bind('<ButtonRelease-1>', selectItem)

        self.lbl = Label(self,text='Pa')
        self.lbl.place(x=10, y=450, width=50, height=20)
        self.txttabla = Entry(self)
        self.txttabla.place(x=70, y=450, width=80, height=20)

        def set_mawp():
            mawp = self.txttabla.get()
            self.parent.txt18.insert(0, mawp)
            if mawp:
                self.master.destroy()
                return mawp

        self.submit = Button(self, text="Insertar", command=set_mawp)
        self.submit.place(x=160, y=450)



if __name__ == "__main__":
    root = Tk()
    root.wm_title("Tabla de materiales de friccion")
    TablaMaterialesSI(root).mainloop()