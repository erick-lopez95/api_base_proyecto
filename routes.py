from flask import Flask, jsonify, request
from jwt_utils import generar_token, verificar_token
from controllers.usuarios_controllers import UsuarioController
import pdb

app = Flask(__name__)
usuario_controller = UsuarioController()

@app.route('/login', methods=['POST'])
def login():
    # Supongamos que aquí tienes lógica para autenticar al usuario
    # y obtener su información (por ejemplo, user_id y role)
    user_id = 123
    # pdb.set_trace() punto de interrupcion usando la libreria pdb
    role = 'admin'

    # Generar un token JWT con la información del usuario
    token = generar_token({'user_id': user_id, 'role': role})

    return jsonify({'token': token})

@app.route('/protected', methods=['GET'])
def protected_route():
    # Obtener el token de la solicitud
    token = request.headers.get('Authorization')

    # Verificar el token
    payload = verificar_token(token)

    if payload:
        # El token es válido, puedes acceder a la información del payload
        user_id = payload['user_id']
        role = payload['role']
        return jsonify({'message': f'Acceso concedido para el usuario {user_id} con rol {role}.'})
    else:
        return jsonify({'error': 'Token inválido o expirado.'}), 401

@app.route('/crear_usuario', methods=['POST'])
def create_user():
  try:
    response_json = usuario_controller.create_user(request.json)
    return jsonify(response_json)
  except ValueError as ve:
    return jsonify(ve.args[0]), ve.args[0]['status']


@app.route('/user/consultar_usuario', methods=['GET'])
def obtener_usuarios():
    # Obtener el token de la solicitud
    token = request.headers.get('Authorization')

    # Verificar el token
    payload = verificar_token(token)

    if payload:
        # El token es válido, puedes acceder a la información del payload
        usuarios = usuario_controller.obtener_usuarios()
        return jsonify({'pokemon': usuarios})
    else:
        return jsonify({'error': 'Token inválido o expirado.'}), 401