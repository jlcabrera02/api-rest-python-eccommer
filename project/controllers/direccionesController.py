from project import responses
from flask import jsonify, request
from project.controllers import obtenerTodo, setData

res = responses.Responses()

class DireccionesController:
  def getAll(self):
    try:
      sql = "call eccomerce.getAddress(null)"
      resp = obtenerTodo(sql,request, None)
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los datos"))
  
  def getxidUsuario(self, idUsuario):
    try:
      sql = f"call eccomerce.getAddress({idUsuario})"

      resp = obtenerTodo(sql,request,None, msgError="Direcciones no encontradas para este usuario")
      
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al consultar datos"))
  
  def getPaises(self):
    try:
      sql =f"SELECT * from paises"

      resp = obtenerTodo(sql,request)

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al consultar paises"))
  
  def getEstado(self, idPais):
    try:
      sql =f"SELECT * from estados WHERE id_pais = {idPais}"

      resp = obtenerTodo(sql,request)

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al consultar estados"))
  
  def getCiudad(self, idEstado):
    try:
      sql =f"SELECT * from ciudades WHERE id_estado = {idEstado}"

      resp = obtenerTodo(sql,request, msgError="No hay resultado")

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al consultar ciudades"))
  
  def postCiudad(self):
    try:
      sql = "INSERT INTO ciudades (ciudad, id_estado) VALUE ('{0}', '{1}')".format(request.json['ciudad'],
      request.json['idEstado'])

      resp = setData(sql, request, "ciudad agregada correctamente", None)
      return jsonify(resp)
    except Exception as ex:
      return jsonify(res.cod_404("Error al registrar ciudad"))
  
  def postEstado(self):
    try:
      sql = "INSERT INTO estados (estado, id_pais) VALUE ('{0}', '{1}')".format(request.json['estado'],
      request.json['idPais'])

      resp = setData(sql, request, "estado agregado correctamente", None)
      return jsonify(resp)
    except Exception as ex:
      return jsonify(res.cod_404("Error al registrar estado"))
  
  def postPais(self):
    try:
      sql = "INSERT INTO paises (pais) VALUE ('{0}')".format(request.json['pais'])

      resp = setData(sql, request, "pais agregado correctamente", None)
      return jsonify(resp)
    except Exception as ex:
      return jsonify(res.cod_404("Error al registrar pais"))
  
  def postDireccion(self):
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

      resp = setData(sql, request, "dirección agregada correctamente")
      return jsonify(resp)
    except Exception as ex:
      return jsonify(res.cod_404("Error al registrar dirección"))

  def putDireccion(self):
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

      resp = setData(sql, request, msgPer="Direccion actualizada correctamente")

      return jsonify(resp)
    except Exception as err:
      print(err)
      return jsonify(res.cod_404("Error al actualizar direccion"))

  def deleteDireccion(self):
    try:
      sql = f"DELETE FROM direcciones WHERE id_direccion = {request.json['idDireccion']}"

      resp = setData(sql, request, f'La direccion con id {request.json["idDireccion"]} se elimino con éxito')

      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al eliminar dirección"))