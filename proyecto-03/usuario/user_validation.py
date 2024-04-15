"""Usuario validation"""

from utils import not_empty, valid_int
from usuario.Usuario import Usuario


def valid_nombre() -> str:
    """Nombre validation function"""
    nombre = not_empty("\nNombre: ")

    while nombre.isdigit():
        print("\nEl nombre no puede tener numeros")
        nombre = not_empty("\nNombre: ")

    return nombre


def valid_apellido() -> str:
    """Apellido validation function"""
    apellido = not_empty("\nApellido: ")

    while apellido.isdigit():
        print("\nEl apellido no puede tener numeros")
        apellido = not_empty("\nApellido: ")

    return apellido


def valid_cedula(input_text: str) -> str:
    """Cedula validation function"""
    cedula = valid_int(input_text, "\nLa cédula solo debe contener números")

    return int(cedula)


def valid_username() -> str:
    """Username validation function"""
    username = not_empty("\nNombre de usuario: ")

    while username.isdigit():
        print("\nEl nombre de usuario no puede tener solo números")
        username = not_empty("Nombre de usuario: ")

    return username


def valid_password() -> str:
    """Password validation function"""
    password = not_empty("\nContraseña: ")

    return password


def create_user() -> Usuario:
    """Create user function"""

    nombre = valid_nombre()

    apellido = valid_apellido()

    cedula = valid_cedula("\nCédula: ")

    username = valid_username()

    password = valid_password()

    return Usuario(nombre, apellido, cedula, username, password)


def sign_in(usuarios: list[Usuario]):
    """Sign in function"""
    username = valid_username()

    password = valid_password()

    valid_user = [
        usuario
        for usuario in usuarios
        if username == usuario.username and usuario.validate_password(password) is True
    ]

    return valid_user
