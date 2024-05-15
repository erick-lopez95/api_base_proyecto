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
      
      nuevo_usuario = UsuarioModel(email=json_data["email"], nickname=json_data["nickname"], encrypted_password=json_data["password"], cellphone=int(json_data["cellphone"]))
      nuevo_usuario.save()
      
      return self.json_responder.json_response("registro exitoso", nuevo_usuario.__dict__, 200)
    except Exception as e:
       return self.json_responder.json_response(str(e), None, 400)
     
  def update_user(self, current_user,  json):
    try:
      email = current_user["email"]
      nickname = current_user["nickname"]
      cellphone = current_user["cellphone"]
      
      if "email" in json and json["email"] is not None:
        email = json["email"]
      if "nickname" in json and json["nickname"] is not None:
        nickname = json["nickname"]
      if "cellphone" in json and json["cellphone"] is not None:
        cellphone = json["cellphone"]
      
      update_user = self.usuario_model.update(email, nickname, cellphone, current_user)
      
      return self.json_responder.json_response("Actualación exitosa", update_user.__dict__, 200)
    except Exception as e:
      return self.json_responder.json_response(str(e),None,400)
    
  def consultar_usuario(self, email):
    try:
      if email is None:
        return self.json_responder.json_response("El email es obligatorio", None, 422)
      
      user = self.usuario_model.consultar_usuario_por_email(email)
      return self.json_responder.json_response("Consulta exitosa", user.__dict__, 200)
    except Exception as e:
      return self.json_responder.json_response(str(e), None, 400)