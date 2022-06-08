from tkinter import *
from tkinter import ttk


class TablaMaterialesIngles(Frame):

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
        self.table.heading("col2", text="P maxima PSI", anchor=CENTER)
        self.table.heading("col3", text="µ minimo humedo", anchor=CENTER)
        self.table.heading("col4", text="µ minimo seco", anchor=CENTER)
        self.table.heading("col5", text="T maxima instantanea °F", anchor=CENTER)
        self.table.heading("col6", text="T maxima continua °F", anchor=CENTER)
        self.table.heading("col7", text="Velocidad maxima pie/min", anchor=CENTER)

        list1 = ["Fundicion de hierro", "150","0.05","0.15","1290","600","7500"]
        list2 = ["Acero", "300","0.05","0.1","1020","660","3600"]
        list3 = ["Fundicion de hierro", "150","0.05","0.1","1020","660","3600"]
        list4 = ["Acero/Fundicion de hierro", "60","0.16","0.2","570","300","3000"]
        list5 = ["Acero/Fundicion de hierro", "10","0.12","0.3","350","200","7500"]
        list6 = ["Acero/Fundicion de hierro", "8","0.15","0.3","350","200","2000"]
        list7 = ["Acero/Fundicion de hierro", "5","0.18","0.22","480","280","5000"]
        list8 = ["Acero/Fundicion de hierro", "50","0.10","0.3","660","350","3600"]
        list9 = ["Acero/Fundicion de hierro", "50","0.08","0.2","930","500","4800"]
        list10 = ["Acero/Fundicion de hierro", "150","0.12","0.32","930","500","3600"]
        list11 = ["Acero/Fundicion de hierro", "300","0.05","0.25","1290","700","7500"]
        list12 = ["Acero/Fundicion de hierro", "150","0.10","0.32","1500","750","3600"]
        list13 = ["Acero/Fundicion de hierro", "100","0.12","0.38","660","300","3600"]
        list14 = ["Acero/Fundicion de hierro", "100","0.12","0.38","500","260","3600"]
        list15 = ["Acero/Fundicion de hierro", "100","0.15","0.47","230","170","3600"]
        list16 = ["Acero/Fundicion de hierro", "400","0.09","0.15","300","150","3600"]
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
            material = sas.get("text")
            self.lbl2.config(text=material)

        self.table.bind('<ButtonRelease-1>', selectItem)

        self.lbl = Label(self,text='Pa')
        self.lbl.place(x=10, y=450, width=50, height=20)
        self.lbl2 = Label(self)
        self.lbl2.place(x=10, y=420, width=150, height=20)
        self.txttabla = Entry(self)
        self.txttabla.place(x=70, y=450, width=80, height=20)

        def set_mawp():
            mawp = float(self.txttabla.get())
            material = self.lbl2["text"]
            self.parent.txt18.delete(0,"end")
            self.parent.txt18.insert(0, mawp)
            self.parent.lbl36.config(text=material)
            if mawp:
                self.master.destroy()
                return mawp 

        self.submit = Button(self, text="Insertar", command=set_mawp)
        self.submit.place(x=160, y=450)



if __name__ == "__main__":
    root = Tk()
    root.wm_title("Tabla de materiales de friccion")
    TablaMaterialesIngles(root).mainloop()