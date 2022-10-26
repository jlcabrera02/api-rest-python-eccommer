from flask import Blueprint
from flask_cors import cross_origin
from project import responses
from project.controllers import cuentasController

res = responses.Responses()

cuenta = Blueprint('cuentas', __name__, url_prefix="/cuentas")
direcciones = cuentasController.CuentasController()

# get -- api/cuentas/
@cuenta.route('/', methods=["GET"])
@cross_origin()
def getCuentas(): return direcciones.getCuentas()

# get -- api/cuentas/<int>
@cuenta.route('/<int:idUsuario>', methods=["GET"])
@cross_origin()
def getCuenta(idUsuario): return direcciones.getCuenta(idUsuario)

# POST -- api/cuentas
@cuenta.route('/', methods=["POST"])
@cross_origin()
def postCuenta(): return direcciones.postCuenta()

# PUT -- api/cuentas/
@cuenta.route('/', methods=["PUT"])
@cross_origin()
def putCuenta(): return direcciones.putCuenta()

# DELETE -- api/cuentas/
@cuenta.route('/', methods=["DELETE"])
@cross_origin()
def deleteCuenta(): return direcciones.deleteCuenta()
