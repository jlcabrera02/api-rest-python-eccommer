from flask import Blueprint
from project import responses
from project.controllers import productosController

res = responses.Responses()

producto = Blueprint('productos', __name__, url_prefix="/productos")
direcciones = productosController.ProductosController()

# get -- api/productos/
@producto.route('/', methods=["GET"])
def getProductos(): return direcciones.getProductos()

# get -- api/productos/<int>
@producto.route('/<int:idProducto>', methods=["GET"])
def getProduct(idProducto): return direcciones.getProduct(idProducto)

# get -- api/productos/subcategory/<int>
@producto.route('/subcategory/<int:idsubcategory>', methods=["GET"])
def getProductosxSubcategory(idsubcategory): return direcciones.getProductosxSubcategory(idsubcategory)

# get -- api/productos/category/<int>
@producto.route('/category/<int:idcategory>', methods=["GET"])
def getProductosxCategory(idcategory): return direcciones.getProductosxCategory(idcategory)

# get -- api/productos/myproducts/<int>
@producto.route('/myproducts/<int:idUsuario>', methods=["GET"])
def getMyProducts(idUsuario): return direcciones.getMyProducts(idUsuario)

# POST -- api/productos
@producto.route('/', methods=["POST"])
def postProducto(): return direcciones.postProducto()

# PUT -- api/productos/
@producto.route('/', methods=["PUT"])
def putProducto(): return direcciones.putProducto()

# DELETE -- api/productos/
@producto.route('/', methods=["DELETE"])
def deleteProducto(): return direcciones.deleteProducto()
