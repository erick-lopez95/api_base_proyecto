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
        usuarios = usuario_controller.obtener_usuarios(payload)
        return jsonify({'pokemon': usuarios})
    else:
        return jsonify({'error': 'Token inválido o expirado.'}), 401