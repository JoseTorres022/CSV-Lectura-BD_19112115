import os
import csv
class ListDirs:
    def listandoConListDir(self):
        ruta_carpeta='./src'
        archivos_carpeta=os.listdir(ruta_carpeta)
        print("Archivos en la carpeta")
        print(archivos_carpeta)

        nombre_archivo=input("Por favor, introduce el nombre del archivo incluyendo su extensión:") 

        if nombre_archivo in archivos_carpeta:
            ruta_carpeta=os.path.join(ruta_carpeta, nombre_archivo)
            print(f"Has seleccionado el archivo:{ruta_carpeta}")
        else:
            print("El archivo no exite en la carpeta")

listadoDir=ListDirs()
listadoDir.listandoConListDir()

class PathJoins:
    def listandoConPathJoin(self):
        nombreCarpeta='./src'
        contenido=os.listdir('./src')
        for listado in contenido:
            print(os.path.join(nombreCarpeta, listado))

class EsFileOEsDir:
    def listandoConIsFile(self):
        nombreCarpeta='./src'
        contenido=os.listdir('./src')
        print("Arhcivos de >>>| {nombreCarpeta} |<<< son:")
        for elemento in contenido:
            ruta_completa=os.path.join(nombreCarpeta,elemento)
            if os.path.isfile(ruta_completa): #vemos si es un archivo/ficero
                print(elemento,ruta_completa, sep=', ') #mostramos el nombre le elementeo y la ruta completa
        print()

        print("Las carpetas de >>>| {nombreCarpeta} |<<< son:")
        for elemento in contenido:
            ruta_completa=os.path.join(nombreCarpeta,elemento)
            if os.path.isdir(ruta_completa): #vemos si es una carpeta
                print(elemento, ruta_completa,sep=", ") #mostramos el nombre del elemtno y la ruta compelta

class EscaneandoDir:
    def lsitandoConScanDir(self):
        nombreCarpeta='./src'
        #archivos_carpeta=os.scandir(nombre_archivo) as ficheros
        with os.scandir(nombreCarpeta) as ficheros:
            for ficheros in ficheros:
                print(ficheros.name)
            nombre_archivo=input("Por favor, introduce el nombre el archivo")
            if nombre_archivo in ficheros:
                nombreCarpeta=os.path.join(nombreCarpeta, ficheros)
                print("ss")

'''print("Lista de archivos")
listandoScanDir=EscaneandoDir()
listandoScanDir.lsitandoConScanDir()'''
#Instanciando clases
print("ListDir")
'''listadoDir=ListDirs()
listadoDir.listandoConListDir()'''

'''print()
print("Path Joins")
listandoDir2=PathJoins()
listandoDir2.listandoConPathJoin()

print()
print("Isfile y IsDir")
listandoIsfileIsDir=EsFileOEsDir()
listandoIsfileIsDir.listandoConIsFile()

print()
print("ScanDir")
listandoScanDir=EscaneandoDir()
listandoScanDir.lsitandoConScanDir()'''