from project import responses
from flask import jsonify, request
from project.controllers import obtenerTodo, obtenerUno, setData, validarPermisosAdmin
from project.utils.operationDate import diferenciaTiempo, formatearTiempo

res = responses.Responses()

class UsuariosController:
  def getAll(self, activoStatus):
    try:
      sql = "SELECT id_usuario, nombres, apellido_paterno, apellido_materno, activo, usuario, fecha_registro, ultima_fecha_ingreso, rol FROM usuarios"
      if activoStatus != None:
        sql += f" WHERE activo = '{activoStatus}'"
      resp = obtenerTodo(sql,request,"admin")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los datos"))
  
  def getOne(self, id):
    try:
      sql = f"SELECT id_usuario, nombres, apellido_paterno, apellido_materno, activo, usuario, fecha_registro, ultima_fecha_ingreso, rol FROM usuarios WHERE id_usuario = {id}"

      resp = obtenerUno(sql,request,'simple', msgError=f"No se encontro un usuario con el id {id}", msgSuccess="Usuario encontrado")
      
      return jsonify(resp)
    except Exception as err:
      print(err)
      return jsonify(res.cod_404("Error al consultar datos"))
  
  def getForWeeks(self, semanas, orden):
    try:
      sql =f"SELECT  id_usuario, nombres, apellido_paterno, apellido_materno, activo, usuario, fecha_registro, ultima_fecha_ingreso, rol  FROM usuarios WHERE ultima_fecha_ingreso < '{formatearTiempo(semanas)}' ORDER BY ultima_fecha_ingreso {orden}"

      resp = obtenerTodo(sql,request,'admin')
      if resp["statusText"] == 'false':
        return jsonify(resp)

      for filas in resp['result']:
        filas["semanasInactivo"] = diferenciaTiempo(filas["ultimaFechaIngreso"])

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al consultar datos"))

  def post(self):
    try:
      user="user"
      if "rol" in request.json:
        auth = validarPermisosAdmin(request)
        if auth != True:
          return auth
        else:
          if request.json['rol'] != "admin" :
            return res.cod_400("Tipo de rol no admitido, los roles admitidos son ['user', 'admin']")
          user = request.json['rol']

      sql = "INSERT INTO usuarios (nombres, apellido_paterno, apellido_materno, activo, usuario, password, fecha_registro, ultima_fecha_ingreso, rol) VALUE ('{0}', '{1}', '{2}', 1, '{3}', MD5('{4}'), now(), now(), '{5}')".format(request.json['nombres'],
      request.json['apellidoPaterno'],
      request.json['apellidoMaterno'],
      request.json['usuario'],
      request.json['password'],
      user
      )

      resp = setData(sql, request, "Usuario creado correctamente")
      return jsonify(resp)
    except Exception as ex:
      return jsonify(res.cod_404("Error al registrar usuario"))

  def putUser(self):
    try:
      sql = "UPDATE usuarios SET nombres ='{0}', apellido_paterno = '{1}',  apellido_materno = '{2}', password = MD5('{3}') WHERE usuario = '{4}' AND password = MD5('{5}')".format(
      request.json['nombres'],
      request.json['apellidoPaterno'],
      request.json['apellidoMaterno'],
      request.json['newPassword'],
      request.json['usuario'],
      request.json['password'],
    )

      resp = setData(sql, request, "Usuario actualizado correctamente", "simple")

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al actualizar usuario"))

  def putStatusActivo(self):
    try:
      index = 0
      sql = ""
      for r in request.json:
        if index < 1:
           sql += f"UPDATE usuarios SET activo = {r['activo']} WHERE id_usuario = {r['id']}"
        else:
          sql += f" OR id_usuario = {r['id']}"
        index = index + 1
      
      resp = setData(sql, request, f"{len(request.json)} usuarios afectados", "admin")

      return jsonify(resp)
    except:
      return jsonify(res.cod_404("Error al modificar usuarios"))

  def eliminarUsuario(self):
    try:
      sql = f"DELETE FROM usuarios WHERE id_usuario = {request.json['id']} AND usuario = '{request.json['usuario']}'"

      resp = setData(sql, request, f'El usuario con id {request.json["id"]} se elimino con éxito', 'admin')

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al eliminar usuario"))