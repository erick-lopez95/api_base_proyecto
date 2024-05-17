from utils.execute_query import execute_query, execute_query_fetchone, execute_query_fetchall
import pdb
from datetime import datetime
# from models.user_roles import UserRolesModel

class RolesModel:
  def __init__(self, id=None, details=None, user_id=None, updated_at=None):
    self.details = details
    self.id = id
    self.user_id = user_id
    self.created_at = datetime.now()
    if updated_at is None:
      self.updated_at = datetime.now()
    else:
      self.updated_at = updated_at
    
  def consultar_por_descripcion(self, details):
    sql = "SELECT * FROM roles where details = %s"
    values = details
    result = execute_query_fetchone(sql, values)
    
    if result is None:
      return None
      
    rol = RolesModel(result[0], result[1])
    return rol
  
  def consultar_por_id(self, id):
    sql = "SELECT * FROM roles where id = %s"
    values = id
    result = execute_query_fetchone(sql, values)
    
    if result is None:
      raise ValueError(f"No se encontro el rol con el detalle {id}")
      
    rol = RolesModel(result[0], result[1])
    return rol
    
  def save(self):
    existe = self.consultar_por_descripcion(self.details)
    if existe is not None:
      raise ValueError("Ya existe un rol con esta descripcion")
    
    try:
      sql = "INSERT INTO roles (details, created_at, updated_at, user_id) VALUES (%s, %s, %s, %s)"
      values = (self.details, self.created_at, self.updated_at, self.user_id)
      return execute_query(sql,values)
    except Exception as e:
      raise ValueError(f"Error al guarda el rol: {e}")
    
  def update(self, id, details):
    try:
      sql = "UPDATE roles SET details = %s, updated_at = %s WHERE id = %s"
      values = (details, datetime.now, id)
      execute_query(sql, values)
      rol = self.consultar_por_id(id)
      return rol
    except Exception as e:
      raise ValueError(f"Error al actualizar rol: {e}")
    
  def delete(self, id):
    try:
      rol = self.consultar_por_id(id)
      sql = "DELETE FROM roles WHERE id = %s"
      values = id
      execute_query(sql, values)
      return rol
    except Exception as e:
      raise ValueError(f"Error al eliminar rol: {e}")
    
  def assign_role(self, rol_id, user_id):
    try:
        sql = "INSERT INTO user_roles(userId, roleId) VALUES(%s, %s)"
        values = (user_id, rol_id)
        execute_query(sql, values)  
        
        from models.user_roles import UserRoles
        
        user_role = UserRoles(userId=user_id, rolId=rol_id)
        return user_role
    except Exception as e:
      raise ValueError(f"Error al asignar rol: {e}")