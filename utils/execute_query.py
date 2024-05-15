import pymysql
from config import DATABASE_CONFIG
import pdb

def execute_query_fetchone(sql, values=None):
  try:
    connection = pymysql.connect(**DATABASE_CONFIG)
    with connection.cursor() as cursor:
      result = None
      if values is not None:
        cursor.execute(sql,values)
      else:
       cursor.execute(sql)
      result = cursor.fetchone()
      connection.commit()
      return result
  finally:
    connection.close()
    
def execute_query_fetchall(sql, values=None):
  try:
    connection = pymysql.connect(**DATABASE_CONFIG)
    with connection.cursor() as cursor:
      result = None
      if values is not None:
        cursor.execute(sql,values)
      else:
       cursor.execute(sql)
      result = cursor.fetchall()
      connection.commit()
      return result
  finally:
    connection.close()
    
def execute_query(sql, values=None):
  try:
    connection = pymysql.connect(**DATABASE_CONFIG)
    with connection.cursor() as cursor:
      result = None
      if values is not None:
        result = cursor.execute(sql,values)
      else:
       result = cursor.execute(sql)
      connection.commit()
      return result
  finally:
    connection.close()