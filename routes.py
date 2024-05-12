from flask import Flask, jsonify
from controllers.usuarios_controllers import UsuarioController

app = Flask(__name__)
usuario_controller = UsuarioController()

@app.route('/pokemon', methods=['GET'])
def obtener_usuarios():
    usuarios = usuario_controller.obtener_usuarios()
    return jsonify({'pokemon': usuarios})