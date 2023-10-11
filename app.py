from flask import Flask, request
import csv
import mysql.connector

#Construimos la aplicación
app = Flask(__name__)


#Configuracion de la base de datos
conexion=mysql.connector.connect(
    host='localhost',
    user='root',
    password='1Gb=!db%',
    database='analisisdatos',
    port='33066'
    )

#Se crear un cursor, este sera para ejecutar sentencias SQL
cursor=conexion.cursor()

#Creamos una ruta para la carga del CSV
#POST
@app.route('/carga_csv', methods=['POST'])
def carga():
    print()