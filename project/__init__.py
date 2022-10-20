from flask import Flask, jsonify, request
from flask_mysqldb import MySQL
from config import config
from flask_cors import CORS

app = Flask(__name__)
mysql = MySQL(app)
cors = CORS(app)

#Importando rutas
from project import routes
from project.routes import auth

if __name__ == '__main__':
  app.config.from_object(config['development'])
  app.register_blueprint(routes.main)
  app.register_blueprint(auth.auth)
  app.run(host='0.0.0.0')