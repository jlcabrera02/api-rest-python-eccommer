from flask import jsonify
from jwt import encode, decode, exceptions
from project.responses import Responses
from project.utils.operationDate import expire_date

res = Responses()


def write_token(data: dict):
  expira = expire_date(1)
  token = encode(
    payload={**data, "exp": expira},
    key="Ultaser",
    algorithm="HS256")
  return {"token": token, "expira": f"{expira.date() }", "statusText": "ok"}

def validate_token(token, output = False):
  try:
    tokenClr = token.replace("Bearer ", "")
    tken = decode(tokenClr, key="Ultaser", algorithms=["HS256"])
    if output:
      return {"valid": True, **tken, "statusText": "ok"}
    return {"valid": True, "statusText": "ok"}
  except exceptions.DecodeError:
    return {"valid": False, "msg": "Token Invalido", "statusText": "false"}
  except exceptions.ExpiredSignatureError:
    return {"valid": False, "msg": "Token expirado", "statusText": "false"}