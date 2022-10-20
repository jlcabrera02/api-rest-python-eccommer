from project.utils.token import validate_token
from flask import jsonify
from project import mysql
from project import responses


res = responses.Responses()

#Para evitar que salga id_usuario y salga idUsuario
def formatText(text):
  index = text.find('_')
  if index == -1:
    return text
  extractWord = text[index + 1:index + 2]
  newText = str(text.replace(f"_{extractWord}", extractWord.upper()))
  newMatch = newText.find("_")
  if newMatch != -1:
    return formatText(newText)
  return newText


def obtenerTodo(sql, request, nivelValidation = None):
  try:
    if nivelValidation == "admin":
      auth = validarPermisosAdmin(request)
      if auth != True:
        return auth
    if nivelValidation == "simple":
      auth = validacionSimple(request)
      if auth != True:
        return auth

    cur = mysql.connection.cursor()
    cur.execute(sql)

    consult = cur.fetchall()
    columnaMain = cur.description

    numFilas = len(consult)
    numColumnas = len(columnaMain)

    results = []

    for i in range(0, numFilas):
      result = {}
      for j in range(0, numColumnas):
        key = formatText(columnaMain[j][0])
        result[f"{key}"] = consult[i][j]
      results.append(result)
    if results:
      return res.cod_200(results)
    return res.cod_404("No se encontro resultado para esta búsqueda")
  except Exception as err:
    return err

def obtenerUno(sql, request, nivelValidation = None, id=0):
  try:
    if nivelValidation == "admin":
      auth = validarPermisosAdmin(request)
      if auth != True:
        return auth
    if nivelValidation == "simple":
      auth = validacionSimple(request)
      if auth != True:
        return auth

    cur = mysql.connection.cursor()
    cur.execute(sql)
    consult = cur.fetchone()


    if consult != None:
      columnaMain = cur.description
      numColumnas = len(columnaMain)
      result = {}
      for i in range(0, 1):
        for j in range(0, numColumnas):
          key = formatText(columnaMain[j][0])
          result[f"{key}"] = consult[j]
      return res.cod_200(result)

    return res.cod_406(f"No se encontro un usuario con el id {id}")
  except Exception as err:
    return err

def setData(sql, request, msgPer ,nivelValidation = None):
  try:
    if nivelValidation == "admin":
      auth = validarPermisosAdmin(request)
      if auth != True:
        return auth
    if nivelValidation == "simple":
      auth = validacionSimple(request)
      if auth != True:
        return auth

    cur = mysql.connection.cursor()
    affect = cur.execute(sql)
    mysql.connection.commit()
    if affect:
      return res.cod_200(msgPer)
    raise Exception
  except Exception as err:
    return err


#NivelValidacion: admin
def validarPermisosAdmin(request):
  if "Authorization" not in request.headers:
    return res.cod_403()

  validacion = validate_token(request.headers["Authorization"], True)

  if validacion['valid'] == False:
    return validacion

  if validacion["rol"] != "admin":
    return res.cod_403("No posees los permisos de administrador para esta acción")

  return True

#NivelValidacion: simple
def validacionSimple(request):
  if "Authorization" not in request.headers:
    return res.cod_403()
  validacion = validate_token(request.headers["Authorization"])
  if validacion['valid'] == False:
    return validacion
  return True
