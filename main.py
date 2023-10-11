import os
import csv
import pandas as pd
import mysql.connector as mysql
from mysql.connector import Error

#Configurando la conexion a la base de datos
try:
    conexion=mysql.connect(
    host='localhost',
    user='root',
    password='1Gb=!db%',
    database='analisiscsv',
    port=33066
)

except Error as e:
        print("Ha ocurrido un error", e)

#Creamos una cursor para ejecutar las sentencias SQL
cursor=conexion.cursor()

class PracticaCSV:
    def LecturaCSV(self):
        #Ruta de la carpeta
        ruta_carpeta = './src/resources'

        #Extencion del archivo
        extencion_archivo = ".csv"

        #Lista para almacenar archivos con la extension
        archivos_con_extencion = []

        archivos_carpeta = os.listdir(ruta_carpeta)
        # print("Archivos en la carpeta")
        # print(archivos_carpeta)

        #For para iterar sobre todos los archivos en las carpetas
        for archivo in archivos_carpeta:
            #Comprobando si el archivo tiene la extension
            if archivo.endswith(extencion_archivo):
                archivos_con_extencion.append(archivo)
        #Se imprime la lista de archivos, pero con sus respectivos indices
        print(f"Archivos con la extension '{extencion_archivo}':")
        print(archivos_con_extencion)
        print()
        for indice, archivo in enumerate(archivos_con_extencion, start=1):
            print(f"{indice}. {archivo}")

        try:
            indice_seleccionado=int(input("Por favor, ingrese el numero del archivo a seleccionar: "))

            if 1<=indice_seleccionado <= len(archivos_con_extencion):
                archivo_seleccionado=archivos_con_extencion[indice_seleccionado-1]
                ruta_completa=os.path.join(ruta_carpeta, archivo_seleccionado)
                print(f"Has seleccionado el archivo: {ruta_completa}")

                with open(ruta_completa,'r') as archivo:
                #with open(ruta_completa) as archivo:
                    contenido=csv.reader(archivo, delimiter=',', quotechar=',',quoting=csv.QUOTE_MINIMAL)
                    #contenido=archivo.read()
                    for fila in contenido:
                       print(fila)
                #opcion=int(input(f"Deseas guardar: '{ruta_carpeta}', en la base de datos?"))
                #print(int("deseas fuaradar: '{arch}'"))
            else:
                print("Indice invalido. Por favor, ingrese un numero valido.")
        except ValueError:
            print("Indice invlaido,Por favor, ingresa un numero valido.")

        except Exception as e:
            print(f"Ocurrio un error: {e}")
            
        opcion=int(input(f"\n¿Guardar '{archivo_seleccionado}' en la base de datos? \n1. Si \n2. No \nRespuesta: "))
        if opcion==1:                  
            #Verificar si hay encabezados en el CSV
            
            print(f"\nEstamos trabajando con: '{archivo_seleccionado}'")
            encabezados=next(contenido, None)
            #if encabezados:
             #Crear la cadena de culsulta para inserta los datos del CSV    
            #cursor.execute= ("""DROP TABLE IF EXIST datos;""")
            consulta=("""INSERT INTO datos ({})
                                      VALUES ({})""")
            columnas=', '.join(encabezados)
            marcadores=', '.join(['%s']*len(encabezados))

                #Insertar los datos en la base de datos
            for filas in contenido:
                valores=tuple(filas)
                cursor.execute(consulta.format(columnas,marcadores), valores)

                    #Hacemos Commit y crerramos la conexion
                conexion.commit()
                    #Creabdo la coslta para el INSERT
                return f"Los datos de '{archivo_seleccionado}' estan insertados en la base de datos"
            else:
                return f"El archivo '{archivo_seleccionado}' no tiene encabezados \nVerifique si '{archivo_seleccionado}' tiene algun problema."
        else:
                return f"El archivo '{archivo_seleccionado}' no se guardo."

                #Obtener los encabezados del CSV
                                
                #pd.read_csv(ruta_carpeta)
    
        # nombre_archivo=input("Por favor, introduce el nombre del archivo incluyendo su extensión:")
app_main = PracticaCSV()
app_main.LecturaCSV()