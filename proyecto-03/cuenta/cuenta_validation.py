"""Cuenta validation"""

import random
from utils import valid_float, valid_int


def random_acount_number():
    """Random number account function"""
    minimo = 10 ** (12 - 1)
    maximo = 10**12 - 1
    return random.randint(minimo, maximo)


def valid_account():
    """Numero de cuenta function"""
    cuenta = valid_int(
        "\nNúmero de cuenta del usuario: ", "\nEl número de cuenta debe ser un entero"
    )

    return int(cuenta)


def saldo_inicial(input_text: str):
    """Saldo inicial function"""
    saldo = valid_float(input_text, "\nEl saldo inicial debe ser un número")

    return float(saldo)
