import sqlite3
import os
import pathlib

base_path2 = pathlib.Path(__file__).parent.resolve()
nombre_bd = 'Tabla materiales de friccion.db'
dbfile = os.path.join(base_path2, nombre_bd) 

conexion = sqlite3.connect(dbfile)
cursor = conexion.cursor()

# cursor.execute('''
#     CREATE TABLE Ingles (
#         Material_de_friccion VARCHAR(30),
#         Presion_maxima FLOAT,
#         Coeficiente_de_friccion_minimo_humedo FLOAT,
#         Coeficiente_de_friccion_minimo_seco FLOAT,
#         Temperatura_maxima_instantanea FLOAT,
#         Temperatura_maxima_continua FLOAT,
#         Velocidad maxima FLOAT
#     )''')

cursor.execute("""
    INSERT INTO Ingles VALUES (
        "Papel resiliente",
        400,
        0.09,
        0.15,
        300,
        150,
        3600
    )""")

conexion.commit()
conexion.close()
