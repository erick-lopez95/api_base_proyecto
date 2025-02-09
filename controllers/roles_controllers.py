from models.roles_models import RolesModel
from models.user_roles import UserRoles
import pdb
from structure_json_response import StructureJsonResponse

class RolesController:
  def __init__(self):
    self.roles_model = RolesModel()
    self.json_responder = StructureJsonResponse()
    self.user_roles = UserRoles()

  def save(self, json, current_user):
    try:
      if not "details" in json:
        return self.json_responder.response("El campo details es obligatorio", None, 422)
      if json["details"] is None:
        return self.json_responder.response("El campo details no puede estar en blanco",None,422)
      
      rol = RolesModel(None, json["details"],current_user["user_id"])
      rol.save()
      
      return self.json_responder.response("Registro exitoso", rol.__dict__,200)
    except Exception as e:
      return self.json_responder.response(str(e),None,400)
    
  def get_by_detail(self, detail):
    try:
      rol = self.roles_model.consultar_por_descripcion(detail)
      if rol is None:
        return self.json_responder.response(f"No se encontro rol con la descripcion '{detail}'", None, 422)
      
      return self.json_responder.response("Consulta exitosa", rol.__dict__, 200)
    except Exception as e:
      return self.json_responder.response(str(e),None,400)
    
  def update(self, json):
    try:
      if not "rol_id" in json:
        return self.json_responder.response("El campo rol_id es obligatorio",None,422)
      if json["rol_id"] is None:
        return self.json_responder.response("El campo rol_id no puede estar en blanco",None,422)
      if not "details" in json:
        return self.json_responder.response("El campo details es obligatorio",None,422)
      if json["details"] is None:
        return self.json_responder.response("El campo details no puede estar en blanco",None,422)
      
      rol_update = self.roles_model.update(json["rol_id"], json["details"])
      
      return self.json_responder.response("Actualizacion exitosa",rol_update.__dict__,200)
    except Exception as e:
      return self.json_responder.response(str(e,None,400))
    
  def delete(self, json):
    try:
      if not "rol_id" in json:
        return self.json_responder.response("El campo rol_id es obligatorio",None,422)
      if json["rol_id"] is None:
        return self.json_responder.response("El campo rol_id no puede estar en blanco",None,422)
      
      rol_delete = self.roles_model.delete(json["rol_id"])
      
      return self.json_responder.response("Se elimino el rol correctamente",rol_delete.__dict__,200)
    except Exception as e:
      return self.json_responder.response(str(e),None,400)
    
  def assign_role(self, json):
    try:
      if not "rol_id" in json:
        return self.json_responder.response("El campo rol_id es obligatorio")
      if json["rol_id"] is None:
        return self.json_responder.response("El campo rol_id no puede estar en blanco")
      if not "user_id" in json:
        return self.json_responder.response("El campo user_id es obligatorio")
      if json["user_id"] is None:
        return self.json_responder.response("El campo user_id no puede estar en blanco")
      
      exist = self.user_roles.get_by_user_and_rol(json["user_id"], json["rol_id"])
      if exist is not None:
        return self.json_responder.response(f"El usuario usuario con id {json['user_id']} ya cuenta con el rol {json['rol_id']}", None, 422)

      
      user_rol = self.roles_model.assign_role(json["rol_id"], json["user_id"])
      return self.json_responder.response("Se aigno el rol correctamente", user_rol.__dict__,200)
    except Exception as e:
      return self.json_responder.response(str(e), None, 400)
    
  def unassign_role(self, json):
    try:
      if not "rol_id" in json:
        return self.json_responder.response("El campo rol_id es obligatorio")
      if json["rol_id"] is None:
        return self.json_responder.response("El campo rol_id no puede estar en blanco")
      if not "user_id" in json:
        return self.json_responder.response("El campo user_id es obligatorio")
      if json["user_id"] is None:
        return self.json_responder.response("El campo user_id no puede estar en blanco")
      
      rol_assign = self.user_roles.get_by_user_and_rol(json["user_id"], json["rol_id"])
      if rol_assign is None:
        return self.json_responder.response(f"El usuario usuario con id {json['user_id']} no cuenta con el rol {json['rol_id'], None, 422}")
      
      self.user_roles.delete_by_userId_and_roleId(json["user_id"], json["rol_id"])
      
      return self.json_responder.response("Se aigno el rol correctamente", rol_assign.__dict__,200)
    except Exception as e:
      return self.json_responder.response(str(e), None, 400)