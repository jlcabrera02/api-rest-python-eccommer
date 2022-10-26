from project.controllers import obtenerTodo, setData
from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
from flask_cors import CORS, cross_origin
from project.responses import Responses
#import ssl_context

app = Flask(__name__)
mysql = MySQL(app)
cors = CORS(app)

res = Responses()
#cors = CORS(app, resources={r"/api/*": {"origins": "*"}})
#logging.getLogger('flask_cors').level = logging.DEBUG

#Importando rutas
""" from project import routes
from project.routes import auth """

#allowOrigin = cross_origin
""" @app.route('/ada', methods=['POST'])
@cross_origin()
def index():
  try:
    print(request.json)
    return jsonify({"asd":request.json["nombres"]})
  except Exception as err:
    print(err)
    return err """

@app.route('/api/user', methods=['GET'])
@cross_origin()
def getUsers():
  try:
    sql = "SELECT id_usuario, nombres, apellido_paterno, apellido_materno, activo, usuario, fecha_registro, ultima_fecha_ingreso, rol FROM usuarios"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/user', methods=['POST'])
@cross_origin()
def postUsers():
  try:
    sql = "INSERT INTO usuarios (nombres, apellido_paterno, apellido_materno, activo, usuario, password, fecha_registro, ultima_fecha_ingreso, rol) VALUE ('{0}', '{1}', '{2}', 1, '{3}', MD5('{4}'), now(), now(), '{5}')".format(request.json['nombres'],
      request.json['apellidoPaterno'],
      request.json['apellidoMaterno'],
      request.json['usuario'],
      request.json['password'],
      request.json['rol'],
      )
    print(sql)
    resp = setData(mysql, sql, "No se pudo registrar usuario", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/user', methods=['PUT'])
@cross_origin()
def putUsers():
  try:
    sql = "UPDATE usuarios SET nombres ='{0}', apellido_paterno = '{1}',  apellido_materno = '{2}', password = MD5('{3}') WHERE usuario = '{4}' AND password = MD5('{5}')".format(
      request.json['nombres'],
      request.json['apellidoPaterno'],
      request.json['apellidoMaterno'],
      request.json['newPassword'],
      request.json['usuario'],
      request.json['password'],
    )
    print(sql)
    resp = setData(mysql, sql, "No se pudo actualizar usuario", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/user', methods=['DELETE'])
@cross_origin()
def delUsers():
  try:
    sql = f"DELETE FROM usuarios WHERE id_usuario = {request.json['id']} AND usuario = '{request.json['usuario']}'"

    resp = setData(mysql, sql, "No se pudo eliminar usuario", "Eliminado")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/cuentas', methods=['GET'])
@cross_origin()
def getCuenta():
  try:
    sql = "call eccomerce.getCuentas(null)"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/cuentas', methods=['POST'])
@cross_origin()
def postCuenta():
  try:
    sql = "call eccomerce.postCuentas('{0}','{1}','{2}','{3}',{4})".format(
        request.json['banco'],
        request.json['clabe'],
        request.json['nombreCuenta'],
        request.json['tipoCuenta'],
        request.json['idUsuario']
      )
    resp = setData(mysql, sql, "No se pudo registrar cuenta", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/cuentas', methods=['PUT'])
@cross_origin()
def putCuenta():
  try:
    sql = "call eccomerce.putCuentas('{0}','{1}','{2}','{3}',{4})".format(
        request.json['banco'],
        request.json['clabe'],
        request.json['nombreCuenta'],
        request.json['tipoCuenta'],
        request.json['idBanco']
      )
    resp = setData(mysql, sql, "No se pudo actualizar cuenta", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/cuentas', methods=['DELETE'])
@cross_origin()
def delCuenta():
  try:
    sql = "DELETE FROM cuenta WHERE id_banco = {0}".format(request.json["idBanco"])
    resp = setData(mysql, sql, "No se pudo borrar cuenta", "Se elimino cuenta correctamente")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address/ciudad/<int:idCiudad>', methods=['GET'])
@cross_origin()
def getDireccionesCiudad(idCiudad):
  try:
    sql = f"SELECT * from ciudades WHERE id_estado = {idCiudad}"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address/estado/<int:idEstado>', methods=['GET'])
@cross_origin()
def getDireccionesEstado(idEstado):
  try:
    sql = f"SELECT * from estados WHERE id_pais = {idEstado}"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address/paises/', methods=['GET'])
@cross_origin()
def getDireccionesPais():
  try:
    sql = "SELECT * from paises"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address', methods=['GET'])
@cross_origin()
def getDirecciones():
  try:
    sql = "call eccomerce.getAddress(null)"
    resp = obtenerTodo(mysql, sql, "Error al consultar", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address', methods=['POST'])
@cross_origin()
def postDireccion():
  try:
    sql = "call eccomerce.postDireccion('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '{7}')".format(
        request.json["calle"],
        request.json["colonia"],
        request.json["numInt"],
        request.json["numExt"],
        request.json["entreCalles"],
        request.json["referencia"],
        request.json["idUsuario"],
        request.json["idCiudad"]
      )
    resp = setData(mysql, sql, "No se pudo registrar direccion", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address', methods=['PUT'])
@cross_origin()
def putDireccion():
  try:
    sql = "call eccomerce.putDireccion('{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}')".format(
        request.json["calle"],
        request.json["colonia"],
        request.json["numInt"],
        request.json["numExt"],
        request.json["entreCalles"],
        request.json["referencia"],
        request.json["idDireccion"],
      )
    resp = setData(mysql, sql, "No se pudo actualizar direccion", "Correcto")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())

@app.route('/api/address', methods=['DELETE'])
@cross_origin()
def delDireccion():
  try:
    sql = f"DELETE FROM direcciones WHERE id_direccion = {request.json['idDireccion']}"
    resp = setData(mysql, sql, "No se pudo eliminar direccion", "Eliminar direccion exitosa")
    return jsonify(resp)
  except Exception as err:
    return jsonify(res.cod_400())



if __name__ == '__main__':
  app.config.from_object(config['development'])
  """ app.register_blueprint(routes.main)
  app.register_blueprint(auth.auth) """
  #context = ('project.cert.pem', 'project.key.pem')
  app.run()