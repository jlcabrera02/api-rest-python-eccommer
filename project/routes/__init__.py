from flask import Blueprint
from flask_cors import CORS
from project.routes import usuariosRoutes, direccionesRoutes, cuentasRoutes, productosRoutes

main = Blueprint('main', __name__, url_prefix="/api")


main.register_blueprint(usuariosRoutes.user, url_prefix="/user")
main.register_blueprint(direccionesRoutes.address)
main.register_blueprint(cuentasRoutes.cuenta)
main.register_blueprint(productosRoutes.producto)