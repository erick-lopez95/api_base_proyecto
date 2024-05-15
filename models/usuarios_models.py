import pymysql
from config import DATABASE_CONFIG
from datetime import datetime
from utils.bcrypt_utils import encrypt_password, check_password
from utils.execute_query import execute_query, execute_query_fetchone, execute_query_fetchall
import pdb

class UsuarioModel:
    def __init__(self, id=None, email=None, nickname=None, encrypted_password=None, cellphone=None, reset_passwrod=None, reset_password_send_at=None, created_at=None, updated_at=None):
      self.id = id
      self.email = email
      self.nickname = nickname
      self.cellphone = cellphone
      self.reset_passwrod = reset_passwrod
      self.encrypted_password = encrypted_password
      self.reset_passwrod_send_at = reset_password_send_at
      if created_at is not None:
        self.created_at = created_at
      else:
        self.created_at = datetime.now()
      
      if updated_at is not None:
        self.updated_at = updated_at
      else:
        self.updated_at = datetime.now()
    
    def save(self):
      existe = self.consultar_usuario_por_email(self.email)
      if existe is not None:
        raise ValueError("Ya existe un usuario con este correo electrónico.")
      
      if self.consultar_nickname(self.nickname) is not None:
        raise ValueError("Ya existe un usuario con este nickname.")
      
      try:    
          sql = "INSERT INTO users (email, nickname, cellphone, encrypted_password, created_at, updated_at) VALUES (%s, %s, %s, %s, %s, %s)"
          values = (self.email, self.nickname, self.cellphone, encrypt_password(self.encrypted_password), self.created_at, self.updated_at)
          return execute_query(sql,values)

      except Exception as e:
          raise ValueError("Error al crear usuario:", e)
          
    def consultar_usuario_por_email(self, email):
      try:
        sql = "SELECT * FROM users where email = %s"
        values = (email,)
        return execute_query_fetchone(sql, values)
      
      except Exception as e:
          raise ValueError("Error al consultar usuario:", e)
        
    def consultar_nickname(self, nickname):
      try:
        sql = "SELECT nickname FROM users where nickname = %s"
        values = nickname
        return execute_query_fetchone(sql, values)
      
      except Exception as e:
        raise ValueError("Error al consultar usuario:", e)

    def obtener_usuarios(self):
        try:
            sql = "SELECT * FROM users"
            return execute_query_fetchall(sql)
        except Exception as e:
          raise ValueError("Error al consultar usuario:", e)
    
    def obtener_usuario_por_id(self, user_id):
      sql = "SELECT * FROM users where id = %s"
      values = user_id
      result = execute_query_fetchone(sql, values)
      
      if result is None:
        raise ValueError("No se encontro usuario con ese id")
      
      user = UsuarioModel(result[0], result[1], result[2], result[4], result[3], result[5], result[6], result[7], result[8])
      return user
    
    def update(self, email, nickname, cellphone, user):
      try:
        sql = "UPDATE users SET email = %s, nickname = %s, cellphone = %s where id = %s"
        values = (email, nickname, cellphone, user["user_id"])
        execute_query(sql, values)
        user = self.obtener_usuario_por_id(user["user_id"])
        return user
      except Exception as e:
        raise ValueError("Error al actualizar usuario:", e)
      
