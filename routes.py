from flask import Flask, jsonify, request
from jwt_utils import generar_token, verificar_token
from controllers.usuarios_controllers import UsuarioController
import pdb

app = Flask(__name__)
usuario_controller = UsuarioController()

@app.route('/login', methods=['POST'])
def login():
    # pdb.set_trace() punto de interrupcion usando la libreria pdb

    # Generar un token JWT con la información del usuario
    response_json = generar_token(request.json)
    return jsonify(response_json), response_json['status']

@app.route('/protected', methods=['GET'])
def protected_route():
    # Obtener el token de la solicitud
    token = request.headers.get('Authorization')

    # Verificar el token
    payload = verificar_token(token)

    if payload:
        # El token es válido, puedes acceder a la información del payload
        role = payload['role']
        return jsonify({'message': f'Acceso concedido para el usuario {payload['email']} con rol {role}.'})
    else:
        return jsonify({'error': 'Token inválido o expirado.'}), 401

@app.route('/crear_usuario', methods=['POST'])
def create_user():
  # try:
    response_json = usuario_controller.create_user(request.json)
    return jsonify(response_json), response_json['status']
  # except ValueError as ve:
  #   return jsonify(ve.args[0]), ve.args[0]['status']


@app.route('/user/consultar_usuario', methods=['GET'])
def obtener_usuarios():
    # Obtener el token de la solicitud
    token = request.headers.get('Authorization')

    # Verificar el token
    payload = verificar_token(token)

    if payload:
        # El token es válido, puedes acceder a la información del payload
        response_json = usuario_controller.obtener_usuarios(payload)
        return jsonify(response_json), response_json['status']
    else:
        return jsonify({'error': 'Token inválido o expirado.'}), 401
      
@app.route('/user/update', methods=['POST'])
def update_user():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  
  if payload:
    response_json = usuario_controller.update_user(payload, request.json)
    return jsonify(response_json), response_json['status']
  else:
    return jsonify({'error': 'Token inválido o expirado.'}), 401
  
@app.route('/user/get_by_email', methods=['GET'])
def get_by_email():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  email = request.args.get('email')
  
  if not email:
    return jsonify({'error': 'Falta el parámetro email'}), 400
  
  if payload:
    response_json = usuario_controller.consultar_usuario(email)
    return jsonify(response_json), response_json["status"]
  else:
    return jsonify({'error': 'Token invalido o expirado'}), 401
  
@app.route('/user/delete_by_id', methods=['DELETE'])
def eliminar_usuario():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  user_id = request.args.get('user_id')
  
  if not user_id:
    return jsonify({'error': 'Falta el parámetro user_id'}), 400
  
  if payload:
    response_json = usuario_controller.eliminar_usuario(user_id)
    return jsonify(response_json), response_json["status"]
  else:
    return jsonify({'error': 'Token inválido o expirado.'}), 400

@app.route('/user/update_password', methods=['POST'])
def update_password():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  
  if payload:
    response_json = usuario_controller.actualizar_contra(request.json, payload)
    return jsonify(response_json), response_json["status"]
  else:
    return jsonify({'error': 'Token inválido o expirado.'}), 400

@app.route('/sms/send', methods=['POST'])
def send_sms():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  
  if payload:
    response_json = usuario_controller.enviar_sms(request.json)
    return jsonify(response_json), response_json["status"]
  else:
    return jsonify({'error': 'Token inválido o expirado.'}), 400
  
@app.route('/recovery_password_token', methods=['POST'])
def recovery_password_token():
  token = request.headers.get('Authorization')
  payload = verificar_token(token)
  
  if payload:
    response_json = usuario_controller.enviar_token_recuperacion(request.json)
    return jsonify(response_json), response_json["status"]
  else:
    return jsonify({'error': 'Token inválido o expirado.'}), 400
