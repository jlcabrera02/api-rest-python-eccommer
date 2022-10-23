from flask import Blueprint
from project import responses
from project.controllers import cuentasController

res = responses.Responses()

cuenta = Blueprint('cuentas', __name__, url_prefix="/cuentas")
direcciones = cuentasController.CuentasController()

# get -- api/cuentas/
@cuenta.route('/', methods=["GET"])
def getCuentas(): return direcciones.getCuentas()

# get -- api/cuentas/<int>
@cuenta.route('/<int:idUsuario>', methods=["GET"])
def getCuenta(idUsuario): return direcciones.getCuenta(idUsuario)

# POST -- api/cuentas
@cuenta.route('/', methods=["POST"])
def postCuenta(): return direcciones.postCuenta()

# PUT -- api/cuentas/
@cuenta.route('/', methods=["PUT"])
def putCuenta(): return direcciones.putCuenta()

# DELETE -- api/cuentas/
@cuenta.route('/', methods=["DELETE"])
def deleteCuenta(): return direcciones.deleteCuenta()
