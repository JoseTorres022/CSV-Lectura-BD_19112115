# Importamos los modulos o librerias
import pandas as pd
import mysql.connector as mysql
import csv
from mysql.connector import Error
import os

# Creamos una cadena de conexion
# Esto es para el CSV
#datos = pd.read_csv('./src/resources/repairoperator.csv', index_col=False)
# datos=pd.read_csv('./resources/ArchivoRLE_CSV.csv')
#datos.head()

# Creando la Conexion en tre Python y MySQL
try:
    # Conexion con la DB
    conexionSQL = mysql.connect(
        host='localhost',
        user='root',
        password='1Gb=!db%',
        port=33066)
    # )

    if conexionSQL.is_connected():
        cursor = conexionSQL.cursor()

        # Crear la base de datps
        cursor.execute("""CREATE DATABASE analisiscsv;""")
        print("Base de datos ha sido creada correctamente")

except Error as e:
    print(">> Algo a pasado, no se conecto con MySQL <<", e)

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
        cursor.execute("""DROP TABLE IF EXISTS entradas;""")
        print("Creando tabla(s)....")

        cursor.execute("""CREATE TABLE entradas(
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
    print("Tablas creada correctamente")

    #fname = input('Introduce un nombre para el CSV:')
    #if len(fname) < 1:
        #fname = "/src/resources/repairoperator.csv"

    with open('./src/repairoperator.csv','r') as csv_file:
        csvreader = csv.reader(csv_file, delimiter=',')
        todos_los_datos=[]
        for row in csvreader:
            value= (row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8],row[9])
            todos_los_datos.append(value)

    datoSQL=("""INSERT INTO analisiscsv.entradas (Layer,Component,Pin,Status,Comment,Defect,JointType,Subtype,XLoc,YLoc) 
                           VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""")
    cursor.executemany(datoSQL, todos_los_datos)
    conexionSQL.commit()                  #print(row)
            #Layer = row[0]
            #Component = row[1]
            #Pin = row[2]
            #Status = row[3]
            #Comment = row[4]
            #Defect = row[5]
            #JointType = row[6]
            #Subtype = row[7]
            #XLoc = row[8]
            #YLoc = row[9]

            #cursor.execute("""INSERT INTO analisiscsv.entradas (Layer,Component,Pin,Status,Comment,Defect,JointType,Subtype,XLoc,YLoc) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)""", (Layer, Component, Pin, Status, Comment, Defect, JointType, Subtype, XLoc, YLoc))

    # for i, row in datos.iterrows():
        # datosSQL= ("""INSERT INTO analisiscsv.entradas VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s);""")
        # encabezado={row['Layer'],row['Component'],row['Pin'],row['Status'],row['Comment'],row['Defect'],row['JointType'],row['Subtype'],row['XLoc'],row['YLoc']}
        # cursor.execute(datosSQL,tuple(row))

        #print("Valores insertados en la base de datos")
        #conexionSQL.commit()
    print("Datos guardados en la base de datos")
except Error as e:
    print(">> Algo a pasado, no se conecto con MySQL <<", e)

# ConsultaSQL=("""SELECT * FROM analisisCSV.entradas""")
# cursor.execute(ConsultaSQL)
# resultado=cursor.fetchall()

# for i in resultado:
 #   print(i)

    # Creando la tabla
    # crear_tabla_query="""CREATE TABLE entradas (
    # id INT AUTO_INCREMENT,
    # Layer TINYINT,
    # Component VARCHAR(8),
    # Pin TINYINT,
   # Status CHAR,
   # Comment VARCHAR(150),
   # Defect VARCHAR(150),
    # JointType VARCHAR(150),
    # Subtype VARCHAR(40),
   # XLoc TINYINT,
    # YLoc TINYINT,
    # PRIMARY KEY(id)
    # )"""

# Creamos una cadena de conexion
# Esto es para el CSV
# datos=pd.read_csv('./src/resources/ArchivoRLE_CSV.csv',index_col=False, delimiter=',')
# datos.head()
