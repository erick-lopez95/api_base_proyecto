from models.usuarios_models import UsuarioModel
from flask import jsonify
import pdb
from structure_json_response import StructureJsonResponse

class UsuarioController:
  def __init__(self):
      self.usuario_model = UsuarioModel()
      self.json_responder = StructureJsonResponse()

  def obtener_usuarios(self,current_user):
      return self.usuario_model.obtener_usuarios()
    
  def create_user(self, json_data):
    try:
      if json_data["password"] != json_data["confirm_password"]:
        return self.json_responder.json_response("Las contraseñas no coinciden", None, 422)
      
      nuevo_usuario = UsuarioModel(email=json_data["email"], nickname=json_data["nickname"], encrypted_password=json_data["password"])
      nuevo_usuario.save()
      
      return self.json_responder.json_response("registro exitoso", nuevo_usuario.__dict__, 200)
    except Exception as e:
       return self.json_responder.json_response(str(e), None, 400)