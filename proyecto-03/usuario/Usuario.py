"""Usuario"""

from persona import Persona
from cuenta.Cuenta import Cuenta


class Usuario(Persona):
    """Clase Usuario"""

    _password: str = None

    def __init__(
        self,
        nombre: str,
        apellido: str,
        cedula: int,
        username: str,
        password: str,
        cuentas: list[Cuenta] = None,
    ) -> None:
        super().__init__(nombre, apellido, cedula)
        self.username = username
        self._password = password
        self.cuentas = cuentas

    def set_username(self, new_username: str):
        """Set username"""
        self.username = new_username

    def set_password(self, new_password: str):
        """Set password"""
        self._password = new_password

    def set_cuentas(self, new_cuentas: list[Cuenta]):
        """Set cuentas"""
        self.cuentas = new_cuentas

    def validate_password(self, password: str):
        """Validate password"""
        return self._password == password
