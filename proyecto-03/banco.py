"""Sistema Bancario"""

from usuario import Usuario


class Banco:
    """Clase Sistema Bancario"""

    _sesion: Usuario = None

    def __init__(self, usuarios: list[Usuario] ) -> None:
        self.usuarios = usuarios

    def main(self):
        pass
        
    

    def iniciar_sesion(self, username: str, password: str):
        pass

    def menu_usuario(self, option):
        pass
