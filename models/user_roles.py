from utils.execute_query import execute_query, execute_query_fetchone, execute_query_fetchall

class UserRoles:
  def __init__(self, id=None, userId=None, rolId=None):
    self.id = id
    self.userId = userId
    self.rolId = rolId
    
  def get_by_user_and_rol(self, user_id, rol_id):
    sql = "SELECT * FROM user_roles where userId = %s AND roleId = %s"
    values = (user_id, rol_id)
    result = execute_query_fetchone(sql, values)
    
    if result is None:
      return None
      
    rol = UserRoles(None, result[0], result[1])
    return rol
  
  def delete_by_userId_and_roleId(self, userId, roleId):
    try:
      sql = "DELETE FROM user_roles WHERE userId = %s AND roleId = %s"
      values = (userId, roleId)
      result = execute_query(sql,values)
      return result
    except Exception as e:
      raise ValueError("Error al eliminar el rol: ", e)