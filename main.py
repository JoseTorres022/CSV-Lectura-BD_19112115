import os
import csv
import pandas as pd


class ListDirs:
    def listandoConListDir(self):
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
                #print(f"\nContenido del archivo'{archivo_seleccionado}': \n{contenido}")
                #pd.read_csv(ruta_carpeta)
            else:
                print("Indice invalido. Por favor, ingrese un numero valido.")
        except ValueError:
            print("Indice invlaido,Por favor, ingresa un numero valido.")

        except Exception as e:
            print(f"Ocurrio un error: {e}")
        # nombre_archivo=input("Por favor, introduce el nombre del archivo incluyendo su extensión:")

        '''if indice in archivos_carpeta:
            ruta_carpeta=os.path.join(ruta_carpeta, nombre_archivo)
            print(f"Has seleccionado el archivo:{ruta_carpeta}")

        else:
            print("El archivo no exite en la carpeta")'''


listadoDir = ListDirs()
listadoDir.listandoConListDir()
