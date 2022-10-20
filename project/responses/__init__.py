class Responses:
  response = {
    "statusCode": 200,
    "statusText": "false",
    "message": "pending"
  }

  def cod_200(self, result = None, msg = "ok"):
    objecto =  self.response
    if result:
      objecto = {**objecto, "result": result}
    objecto["statusText"] = "ok"
    objecto["message"] = msg
    return objecto

  def cod_400(self, msg = "Error con la solicitud"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 400
    return objecto

  def cod_401(self, msg = "Nesesitas credenciales"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 401
    return objecto
  
  def cod_403(self, msg = "No posees los permisos"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 403
    return objecto
  
  def cod_404(self, msg = "Recurso no encontrado"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 404
    return objecto
  
  def cod_406(self, msg = "No se encontro resultados"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 406
    return objecto
  
  def cod_500(self, msg = "Error interno del servidor"):
    objecto = self.response
    objecto["message"] = msg
    objecto["statusCode"] = 500
    return objecto

  def token_expirado(self, obj, msg = "Token expirado o invalido"):
    objecto = self.response
    objecto["statusCode"] = 400
    objecto["message"] = msg
    return {**objecto, **obj}
