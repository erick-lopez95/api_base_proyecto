import jwt
from models.usuarios_models import UsuarioModel
import pdb
from utils.bcrypt_utils import check_password

# Clave secreta para firmar y verificar los tokens JWT
SECRET_KEY = 'P0r3#ct0F1n@lM@3sTr1@'

def generar_token(payload):
    
    usuario_model = UsuarioModel()
    user = usuario_model.consultar_usuario_por_email(payload["email"])
    
    if user is None:
      return {'response': {"message":"No se existe usuario con ese correo", "json": None}, "status": 400}
    
    if not check_password(payload["password"], user.encrypted_password.encode('utf-8')):
      return {'response': {"message":"La contraseña es incorrecta", "json": None}, "status": 422}
    
    token_content = {"user_id": user.id, "email": user.email, "nickname": user.nickname, "cellphone": user.cellphone, "encrypted_password": user.encrypted_password}
    token = jwt.encode(token_content, SECRET_KEY, algorithm='HS256')
    
    return {'response': {"message":"token generado", "json": token}, "status": 200}

def verificar_token(token):
    """
    Verifica y decodifica un token JWT.
    Retorna el payload si el token es válido.
    Retorna None si el token es inválido.
    
    # Verificar el token y decodificar el payload
    payload = jwt.decode(token, 'tu_secreto', algorithms=['HS256'])
    
    # El token es válido, puedes acceder a la información del payload
    user_id = payload['user_id']
    role = payload['role']
    """
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
        return payload
    except jwt.ExpiredSignatureError:
        # El token ha expirado
        # Manejar el error...
        return None
    except jwt.InvalidTokenError:
        # El token es inválido (puede ser porque ha sido alterado)
        # Manejar el error...
        return None