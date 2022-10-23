from flask import Blueprint, jsonify, request
from project import mysql
from project import responses
from project.utils.token import write_token
from project.controllers import obtenerUno

res = responses.Responses()
auth = Blueprint('auth', __name__, url_prefix="/auth")

# post -- /auth

@auth.route('/', methods=['POST'])
def login():
  try:
    sql = "SELECT id_usuario, nombres, apellido_paterno, apellido_materno, usuario, ultima_fecha_ingreso, rol FROM usuarios WHERE usuario = '{0}' AND password = MD5('{1}')".format(request.json["usuario"], request.json["password"])
    resp = obtenerUno(sql, request, msgError="Credenciales incorrectas", msgSuccess="Autenticado")

    if resp["statusText"] == "ok":
      resp["result"]["ultimaFechaIngreso"] = str(resp["result"]["ultimaFechaIngreso"])
      token = write_token(resp["result"])
      resp["result"]["token"] = token

    return jsonify(resp)
  except Exception as ex:
    print(ex)
    return jsonify(res.cod_404("Error al ingresar"))