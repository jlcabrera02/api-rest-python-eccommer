from flask import Blueprint, jsonify, request
from project import mysql
from project import responses
from project.utils.token import write_token

res = responses.Responses()
auth = Blueprint('auth', __name__, url_prefix="/auth")

# post -- /auth

@auth.route('/', methods=['POST'])
def login():
  try:
    cur = mysql.connection.cursor()
    sql = "SELECT id_usuario, nombres, apellido_paterno, apellido_materno, usuario, rol, ultima_fecha_ingreso FROM usuarios WHERE usuario = '{0}' AND password = MD5('{1}')".format(request.json["usuario"], request.json["password"])
    cur.execute(sql)
    consult = cur.fetchone()
    if consult != None:
      result = {
        "id": consult[0],
        "nombres": consult[1],
        "apellidoPaterno": consult[2],
        "apellidoMaterno": consult[3],
        "usuario": consult[4],
        "rol": consult[5],
        "ultimoIngreso": f"{consult[6]}",
        }
      token = write_token(result)
      obj = {"token": token, **result}

      return jsonify(res.cod_200(obj, "Autenticado correctamente"))
    else:
      return jsonify(res.cod_401(None, "Credenciales incorrectas"))
  except Exception as ex:
    print(ex)
    return jsonify(res.cod_404("Error al ingresar"))


