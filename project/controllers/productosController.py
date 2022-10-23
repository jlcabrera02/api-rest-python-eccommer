from project import responses
from flask import jsonify, request
from project.controllers import obtenerTodo, setData
from project.utils.token import validate_token

res = responses.Responses()

class ProductosController:
  def getProductos(self):
    try:
      sql = "call eccomerce.getProductos()"
      resp = obtenerTodo(sql,request, msgError="No se encontro resultado para productos")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los productos"))
  
  def getProductosxSubcategory(self, idSubcategoria):
    try:
      sql = f"call eccomerce.getProductosxSubCategory({idSubcategoria})"
      resp = obtenerTodo(sql,request, msgError="Sin resultados")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los productos"))
  
  def getProductosxCategory(self, idCategoria):
    try:
      sql = f"call eccomerce.getProductosxCategoria({idCategoria})"
      resp = obtenerTodo(sql,request, msgError="Sin resultados")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los productos"))
  
  def getMyProducts(self, idUsuario):
    try:
      sql = f"call eccomerce.getProduct({idUsuario}, 'xve')"
      resp = obtenerTodo(sql,request, 'simple', msgError="El usuario no tiene productos aún")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener los productos del usuario"))

  def getProduct(self, idProduct):
    try:
      sql = f"call eccomerce.getProduct({idProduct}, 'xid')"
      resp = obtenerTodo(sql,request, msgError="No existe el producto")
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al obtener producto"))

  
  def postProducto(self):
    try:
      sql = "call eccomerce.postProducto('{0}','{1}',{2},'{3}',{4}, {5})".format(
        request.json['nombreProducto'],
        request.json['descripcion'],
        request.json['precio'],
        request.json['marca'],
        request.json['idVendedor'],
        request.json['idSubcategoria']
      )

      token = validate_token(request.headers["Authorization"], True)

      if token['idUsuario'] == request.json['idVendedor']:
        resp = setData(sql,request, "Se agrego correctamente la cuenta para el usuario", 'simple')
      else:
        resp = res.cod_400("El id no coincide con las ")
        
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al establecer la cuenta"))
  
  def putProducto(self):
    try:
      sql = "call eccomerce.postProducto('{0}','{1}',{2},'{3}',{4}, {5})".format(
        request.json['nombreProducto'],
        request.json['descripcion'],
        request.json['precio'],
        request.json['marca'],
        request.json['idVendedor'],
        request.json['idSubcategoria']
      )

      token = validate_token(request.headers["Authorization"], True)

      if token['idUsuario'] == request.json['idVendedor']:
        resp = setData(sql,request, "Se agrego correctamente la cuenta para el usuario", 'simple')
      else:
        resp = res.cod_400("El id no coincide con las ")
        
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al establecer la cuenta"))
  
  def deleteProducto(self):
    try:
      sql = "DELETE FROM productos WHERE id_producto = {0}".format(request.json["idProducto"])
      resp = setData(sql,request, "Se elimino el producto", 'simple')
      return jsonify(resp)
    except Exception as err:
      return jsonify(res.cod_404("Error al eliminar producto"))