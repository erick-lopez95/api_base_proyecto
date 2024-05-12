import pymysql
from config import DATABASE_CONFIG

class UsuarioModel:
    def __init__(self):
    #     self.connection = pymysql.connect(**DATABASE_CONFIG)
      self.nombre = ""
    

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