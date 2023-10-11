#Importamos los modulos o librerias a usar
from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow

#Construimos la aplicacion
app=Flask(__name__)

#Cadena de conexion a la base de daatos con MySQL
app.config['SQLALCHEMY_DATABASE_URI']='mysql+pymysql://root:1Gb=!db%@localhost:33066/practicaRLE'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False
db=SQLAlchemy(app)
ma=Marshmallow(app)

#Clases para la manipulacion basica en una base de datos
#Seran operacion basiscas CRUD en la bases de datos

#Definicmos y modelamos las tablas en la base de datos
class Analisis(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    Layer=db.Column(db.String(30))
    Component=db.Column(db.String(60))
    Pin=db.Column(db.String(1))
    Status=db.Column(db.String(30))
    Comment=db.Column(db.String(60))
    Defect=db.Column(db.String(60))
    JointType=db.Column(db.String(60))
    Subtype=db.Column(db.String(60))
    XLoc=db.Column(db.String(60))
    YLoc=db.Column(db.String(60))

    def __init__(self,Layer,Component,Pin,Status,Comment,Defect,JointType,Subtype,XLoc,YLoc):
        self.Layer=Layer
        self.Component=Component
        self.Pin=Pin
        self.Status=Status
        self.Comment=Comment
        self.Defect=Defect
        self.JointType=JointType
        self.Subtype=Subtype
        self.XLoc=XLoc
        self.YLoc=YLoc

#Creando las tablas
with app.app_context():
    db.create_all()

#Creamos un esquema en la base de datos
#El esquema funciona para organizar loda tos dentro de la base de datps.
class RLEShema(ma.Schema):
    class Meta:
        fields=('Layer','Component','Pin','Status','Comment','Defect','JointType','Subtype','XLoc','YLoc')

#Crear una sola fila
RLE_shema=RLEShema()

#Crear multiples lineas
RLEs_shema=RLEShema(many=True)

#Creamos las rutas de la aplicacion
#POST
@app.route('/entradas',methods=['POST'])
def crear_RLE():
    Layer=request.json['Layer']
    Component=request.json['Component']
    Pin=request.json['Pin']
    Status=request.json['Status']
    Comment=request.json['Comment']
    Defect=request.json['Defect']
    JointType=request.json['JointType']
    Subtype=request.json['Subtype']
    XLoc=request.json['XLoc']
    YLoc=request.json['YLoc']

    nueva_entrada=Analisis(Layer,Component,Pin,Status,Comment,Defect,JointType,Subtype,XLoc,YLoc)
    
    #Guardar en la base de datos
    db.session.add(nueva_entrada)
    db.session.commit()

    return RLE_shema.jsonify(nueva_entrada)

    #print(request.json)
    #return 'Recibido, trabajando correctamente

#Obtener todos los datos del RLE
#GET
@app.route('/entradas',methods=['GET'])
def obtener_RLE():
    todos_los_datos=Analisis.query.all()
    resultado=RLEs_shema.dump(todos_los_datos)
    return jsonify(resultado)

#Obtener un datos por su ID
#GET
@app.route('/entradas/<id>', methods=['GET'])
def obtener_dato(id):
    dato=Analisis.query.get(id)
    return RLE_shema.jsonify(dato)

#Actualziar los datos
#PUT
@app.route('/entradas/<id>', methods=['PUT'])
def actualzar_dato(id):
    datoUP=Analisis.query.get(id)
    
    Layer=request.json['Layer']
    Component=request.json['Component']
    Pin=request.json['Pin']
    Status=request.json['Status']
    Comment=request.json['Comment']
    Defect=request.json['Defect']
    JointType=request.json['JointType']
    Subtype=request.json['Subtype']
    XLoc=request.json['XLoc']
    YLoc=request.json['YLoc']

    datoUP.Layer=Layer
    datoUP.Component=Component
    datoUP.Pin=Pin
    datoUP.Status=Status
    datoUP.Comment=Comment
    datoUP.Defect=Defect
    datoUP.JointType=JointType
    datoUP.Subtype=Subtype
    datoUP.XLoc=XLoc
    datoUP.YLoc=YLoc

    db.session.commit()
    return RLE_shema.jsonify(datoUP)

#Borrar un dato
#DELETE
@app.route('/entradas/<id>',methods=['DELETE'])
def borrar_dato(id):
    datoDEL=Analisis.query.get(id)
    db.session.delete(datoDEL)
    db.session.commit()

    return RLE_shema.jsonify(datoDEL)

#Crearmos una ruta principal (index) con mensaje
@app.route('/',methods=['GET'])
def index():
    return jsonify({'message': 'Bienvenido a mi API REST x Flask & SQLAlchemy, para clase Análisis Inteligente de Datos'})

#Creamos un debbugger para actualziar y reinicie la app
#Esto para que cada cambio nuevo surta efecto
if __name__=="__main__":
    app.run(debug=True)