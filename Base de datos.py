import sqlite3
import os
import pathlib

base_path2 = pathlib.Path(__file__).parent.resolve()
image_filename2 = 'Database.db'
dbfile = os.path.join(base_path2, image_filename2) 

conexion = sqlite3.connect(dbfile)
cursor = conexion.cursor()


user_Rr = 0.35

cursor.execute("SELECT * FROM Constantes")

table_data = cursor.fetchall()
list_Rr = []
list_α = []
list_ß = []
restas = []

for Rr, alpha, beta in table_data:
    list_Rr.append(Rr)
    list_α.append(alpha)
    list_ß.append(beta)
    restas.append((Rr - user_Rr) if ((Rr - user_Rr) > 0) else (Rr - user_Rr) * (-1))
    

p1 = min(restas)
c1 = restas.index(p1)
restas[c1] += 100


p2 = min(restas)
c2 = restas.index(p2)

x0 = list_Rr[c1]
y0 = list_α[c1]
x = user_Rr
x1 = list_Rr[c2]
y1 = list_α[c2]

y = y0 + (x-x0)*((y1-y0)/(x1-x0))


print(table_data)

conexion.close()