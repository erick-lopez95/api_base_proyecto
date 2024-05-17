class StructureJsonResponse:
  
  def __init__(self) -> None:
    pass
  
  def response(self, message, json=None, status=None):
    return {'response': {"message":message, "json": json}, "status": status}