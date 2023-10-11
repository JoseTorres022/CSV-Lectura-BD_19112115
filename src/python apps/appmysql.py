import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error
datos=pd.read_csv("./src/repairoperator.csv", index_col=False)
datos.head()

try:
    conexionSQL=mysql.connect(
    host='localhost',
    user='root',   
    password='1Gb=!db%',
    port=33066)

    if conexionSQL.is_connected():
        cursor = conexionSQL.cursor()

        # Crear la base de datps
        cursor.execute("""CREATE DATABASE analisiscsv;""")
        print("Base de datos ha sido creada correctamente")

except Error as e:
    print("Algo paso!")

try:
    conexionSQL = mysql.connect(
        host='localhost',
        database='analisiscsv',
        user='root',
        password='1Gb=!db%',
        port=33066)

    if conexionSQL.is_connected():
        cursor = conexionSQL.cursor()

        # Seleccionar la base de datos
        cursor.execute("""SELECT database();""")
        record = cursor.fetchone()
        print("Estas conectada a la base de datos", record)
        
        # Crear la tabla en la base de datos,
        cursor.execute("""DROP TABLE IF EXISTS datos;""")
        print("Creando tabla(s)....")

        cursor.execute("""CREATE TABLE datos(
                        Layer INT,
                        Component VARCHAR(8),
                        Pin VARCHAR(4),
                        Status CHAR(2),
                        Comment VARCHAR(150),
                        Defect VARCHAR(150),
                        JointType VARCHAR(150),
                        Subtype VARCHAR(40),
                        XLoc TINYINT,
                        YLoc TINYINT
                        );""")
        for i, row in datos.iterrows():
             datosSQL= ("""INSERT INTO analisiscsv.datos (Layer,Component,Pin,Status,Comment,Defect,JointType,Subtype,XLoc,YLoc) 
                        VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
        cursor.execute(datosSQL,tuple(row))
        print("DAtos insertados correctamente")
        conexionSQL.commit()

except Error as e:
    print("Algo paso!")
