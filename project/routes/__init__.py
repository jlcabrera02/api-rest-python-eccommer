from flask import Blueprint
from project.routes import usuariosRoutes

main = Blueprint('main', __name__, url_prefix="/api")

main.register_blueprint(usuariosRoutes.user)