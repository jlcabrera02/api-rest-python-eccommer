from flask import Blueprint
from project import responses
from project.controllers import usuariosController

res = responses.Responses()

user = Blueprint('user', __name__, url_prefix="/user")
usuariosC = usuariosController.UsuariosController()

# get -- api/user
# get -- api/user/<int: activo>
@user.route('/', methods=["GET"])
@user.route('/<int:activoStatus>', methods=["GET"])
def getAll(activoStatus = None): return usuariosC.getAll(activoStatus)

# get -- api/user/int
@user.route('/<int:id>')
def getOne(id): return usuariosC.getOne(id)

# GET -- api/user/semanas/<int>
@user.route('/inactivos/<int:semanas>')
@user.route('/inactivos/<int:semanas>/<orden>')
def getForWeeks(semanas, orden = "ASC"): return usuariosC.getForWeeks(semanas, orden)

# POST -- api/user
@user.route('/', methods=['POST'])
def post(): return usuariosC.post()

# PUT -- api/user/actualizar
@user.route('/actualizar', methods=['PUT'])
def putUser(): return usuariosC.putUser()

# PUT -- api/user/toogle-activo
@user.route('/toogle-activo', methods=['PUT'])
def putStatusActivo(): return usuariosC.putStatusActivo()

#DELETE -- api/user/
@user.route('/eliminar', methods=['DELETE'])
def eliminarUsuario(): return usuariosC.eliminarUsuario()