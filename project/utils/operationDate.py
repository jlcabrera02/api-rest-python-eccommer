from datetime import datetime, timedelta

# Para saber cuanto tiempo paso de tal fecha hasta la acual y devolverla en formato "yyyy-mm-dd"
def formatearTiempo(semanas):
  today = datetime.now()
  oldDate = timedelta(weeks=semanas)
  fechaFind = today - oldDate
  return f"{fechaFind.year}-{fechaFind.month}-{fechaFind.day}"

# Para saber cuanto tiempo ha transcurrido en dias la fecha actual con la que le pasemos de parametro en semanas
def diferenciaTiempo(date: datetime):
  today = datetime.now()
  timeElapsed = today - date
  semanas = timeElapsed.total_seconds() / 604800
  return round(semanas)

# Para calcular el tiempo que se le da a un token para que expire en dias
def expire_date(days: int):
  now = datetime.now()
  new_date=now + timedelta(days)
  return new_date