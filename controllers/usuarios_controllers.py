from models.usuarios_models import UsuarioModel

class UsuarioController:
    def __init__(self):
        self.usuario_model = UsuarioModel()

    def obtener_usuarios(self):
        return self.usuario_model.obtener_usuarios()