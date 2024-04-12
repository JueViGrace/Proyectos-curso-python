"""Persona"""

class Persona:
    """Clase persona"""
    def __init__(self, nombre: str, apellido: str, cedula: str) -> None:
        self.nombre = nombre
        self.apellido = apellido
        self.cedula = cedula

    def set_nombre(self, new_nombre: str):
        """Set nombre"""
        self.nombre = new_nombre

    def set_apellido(self, new_apellido: str):
        """Set apellido"""
        self.apellido = new_apellido

    def set_cedula(self, new_cedula: str):
        """Set cedula"""
        self.cedula = new_cedula

