"""Cuenta"""


class Cuenta:
    """Clase Cuenta"""

    def __init__(self, account_id: int, saldo: float) -> None:
        self.account_id = account_id
        self.saldo = saldo

    def depositar(self, value: float):
        """Depositar dinero"""
        self.saldo += value

    def retirar(self, value: float):
        """Retirar dinero"""
        self.saldo -= value
