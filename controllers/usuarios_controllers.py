from models.usuarios_models import UsuarioModel
from flask import jsonify
import pdb

class UsuarioController:
  def __init__(self):
      self.usuario_model = UsuarioModel()

  def obtener_usuarios(self):
      return self.usuario_model.obtener_usuarios()
    
  def create_user(self, json_data):
    try:
      if json_data["password"] != json_data["confirm_password"]:
        raise ValueError("Las contraseñas no coinciden")
      
      nuevo_usuario = UsuarioModel(email=json_data["email"], nickname=json_data["nickname"], encrypted_password=json_data["password"])
      nuevo_usuario.save()
      
      return {'response': {"message":"registro exitoso", "json": nuevo_usuario.__dict__}, "status": 200}
    except Exception as e:
        return {'response': {"message": str(e), "json": None}, "status": 400}