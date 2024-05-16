from models.usuarios_models import UsuarioModel
from flask import jsonify
import pdb
from structure_json_response import StructureJsonResponse
from utils.bcrypt_utils import check_password, encrypt_password

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
    
  def eliminar_usuario(self, user_id):
    try:
      if user_id is None:
        return self.json_responder.json_response("El id del usuario es obligatorio", None, 422)
      
      result = self.usuario_model.eliminar_usuario(user_id)
      return self.json_responder.json_response("Se elimino usuario correctamente", result.__dict__, 200)
    except Exception as e:
      return self.json_responder.json_response(str(e), None, 400)
    
  def actualizar_contra(self, json, current_user):
    try:
      if not check_password(json["password"], current_user["encrypted_password"].encode('utf-8')):
        return {'response': {"message":"La contraseña actual no coincide con la contraseña recibida", "json": None}, "status": 422}
      
      if json["new_password"] != json["confirm_password"]:
        return {'response': {"message":"La contraseña nueva contraseña no coinciden", "json": None}, "status": 422}

      
      password = encrypt_password(json["new_password"])
      
      user = self.usuario_model.actualizar_contra(password, current_user["user_id"])
      
      return self.json_responder.json_response("Constraseña actualizada", user.__dict__, 200)
    except Exception as e:
      return self.json_responder.json_response(str(e),None,400)