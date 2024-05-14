import pymysql
from config import DATABASE_CONFIG
from datetime import datetime

class UsuarioModel:
    def __init__(self, email=None, nickname=None, encrypted_password=None):
    #     self.connection = pymysql.connect(**DATABASE_CONFIG)
      self.email = email
      self.nickname = nickname
      self.encrypted_password = encrypted_password
      self.created_at = datetime.now()
      self.updated_at = datetime.now()
    
    def save(self):
      try:
          connection = pymysql.connect(**DATABASE_CONFIG)
          with connection.cursor() as cursor:
              # Sentencia SQL para insertar un nuevo usuario en la tabla users
              sql = "INSERT INTO users (email, nickname, encrypted_password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s)"
              
              # Valores a insertar
              values = (self.email, self.nickname, self.encrypted_password, self.created_at, self.updated_at)
              
              # Ejecutar la sentencia SQL
              cursor.execute(sql, values)
              
          # Confirmar la transacción
          connection.commit()
          
          # Imprimir mensaje de éxito
          return self

      except Exception as e:
          # Imprimir mensaje de error en caso de fallo
          raise ValueError("Error al crear usuario:", e)

      finally:
          # Cerrar la conexión con la base de datos
          connection.close()

    def obtener_usuarios(self):
        try:
            connection = pymysql.connect(**DATABASE_CONFIG)
            with connection.cursor() as cursor:
                sql = "SELECT * FROM pokemon"
                cursor.execute(sql)
                usuarios = cursor.fetchall()
                return usuarios
        finally:
            connection.close()