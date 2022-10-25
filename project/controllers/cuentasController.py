from project import responses
from flask import jsonify, request
from project.controllers import obtenerTodo, setData

res = responses.Responses()

class CuentasController:
  def getCuentas(self):
    try:
      sql = "call eccomerce.getCuentas(null)"
      resp = obtenerTodo(sql,request, None, "No se encontro resultado en cuentas")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener las cuentas"))
  
  def getCuenta(self, idUsuario):
    try:
      sql = f"call eccomerce.getCuentas({idUsuario})"
      resp = obtenerTodo(sql,request, None, "El usuario no tiene cuentas aún")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener la cuenta"))
  
  def postCuenta(self):
    try:
      sql = "call eccomerce.postCuentas('{0}','{1}','{2}','{3}',{4})".format(
        request.json['banco'],
        request.json['clabe'],
        request.json['nombreCuenta'],
        request.json['tipoCuenta'],
        request.json['idUsuario']
      )
      resp = setData(sql,request, "Se agrego correctamente la cuenta para el usuario")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al establecer la cuenta"))
  
  def putCuenta(self):
    try:
      sql = "call eccomerce.putCuentas('{0}','{1}','{2}','{3}',{4})".format(
        request.json['banco'],
        request.json['clabe'],
        request.json['nombreCuenta'],
        request.json['tipoCuenta'],
        request.json['idBanco']
      )
      resp = setData(sql,request, "Se actualizo la cuenta para el usuario")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al actulizar la cuenta"))
  
  def deleteCuenta(self):
    try:
      sql = "DELETE FROM cuenta WHERE id_banco = {0}".format(request.json["idBanco"])
      resp = setData(sql,request, "Se elimino la cuenta para el usuario")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al eliminar la cuenta"))