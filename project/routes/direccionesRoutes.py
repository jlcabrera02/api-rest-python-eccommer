from flask import Blueprint
from project import responses
from project.controllers import direccionesController

res = responses.Responses()

address = Blueprint('address', __name__, url_prefix="/address")
direcciones = direccionesController.DireccionesController()

# get -- api/address/
@address.route('/', methods=["GET"])
def getAll(): return direcciones.getAll()

# get -- api/address/<int>
@address.route('/<int:idUsuario>', methods=["GET"])
def getxidUsuario(idUsuario): return direcciones.getxidUsuario(idUsuario)

# get -- api/address/pais
@address.route('/pais', methods=["GET"])
def getPaises(): return direcciones.getPaises()

# get -- api/address/estado/<int>
@address.route('/estado/<int:idPais>', methods=["GET"])
def getEstado(idPais): return direcciones.getEstado(idPais)

# get -- api/address/ciudad/<int>
@address.route('/ciudad/<int:idEstado>', methods=["GET"])
def getCiudad(idEstado): return direcciones.getCiudad(idEstado)

# POST -- api/address/pais/
@address.route('/pais', methods=["POST"])
def postPais(): return direcciones.postPais()

# POST -- api/address/estado/
@address.route('/estado/', methods=["POST"])
def postEstado(): return direcciones.postEstado()

# POST -- api/address/ciudad/
@address.route('/ciudad/', methods=["POST"])
def postCiudad(): return direcciones.postCiudad()

# POST -- api/address/
@address.route('/', methods=["POST"])
def postDireccion(): return direcciones.postDireccion()

# PUT -- api/address/
@address.route('/', methods=["PUT"])
def putDireccion(): return direcciones.putDireccion()

# DELETE -- api/address/
@address.route('/', methods=["DELETE"])
def deleteDireccion(): return direcciones.deleteDireccion()
