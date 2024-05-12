import jwt

# Clave secreta para firmar y verificar los tokens JWT
SECRET_KEY = 'tu_secreto'

def generar_token(payload):
    """
    Genera un token JWT con el payload proporcionado.
    # Crear un payload con la información del usuario
      payload = {'user_id': 123, 'role': 'admin'}
    """
    return jwt.encode(payload, SECRET_KEY, algorithm='HS256')

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