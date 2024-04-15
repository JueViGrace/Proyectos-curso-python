"""Sistema Bancario"""

from usuario.Usuario import Usuario
from usuario.user_validation import create_user, sign_in, valid_cedula
from utils import draw_menu, finish, validate_option
from cuenta.cuenta_validation import random_acount_number, saldo_inicial, valid_account
from cuenta.Cuenta import Cuenta


class Banco:
    """Clase Sistema Bancario"""

    def __init__(self, usuarios: list[Usuario], sesion: Usuario = None) -> None:
        self.usuarios = usuarios
        self.sesion = sesion

    def main(self):
        """Main function"""
        options = [
            {"accion": "Crea tu usuario", "valor": "1"},
            {"accion": "Iniciar sesión", "valor": "2"},
            {"accion": "Finalizar", "valor": "3"},
        ]

        is_not_exit = True

        while is_not_exit:
            print("\nElija una opción\n")
            draw_menu(options)

            option_selected = validate_option(options)

            if option_selected == 1:
                new_user = create_user()

                existing_user = [
                    usuario
                    for usuario in self.usuarios
                    if new_user.username == usuario.username
                    or new_user.cedula == usuario.cedula
                ]

                if len(existing_user) > 0:
                    print("\nEste usuario ya existe")
                else:
                    self.usuarios.append(new_user)
            elif option_selected == 2:
                self.iniciar_sesion()

                if self.sesion is not None:
                    self.menu_usuario()

            elif option_selected == 3:
                finish()
                break

    def iniciar_sesion(self):
        """Sign in funtion"""
        user = sign_in(self.usuarios)

        if len(user) == 0:
            print("\nInvalid credentials")
        else:
            self.sesion = user[0]

    def menu_usuario(self):
        """Menu de usuario"""
        options = [
            {"accion": "Crear cuenta bancaria", "valor": "1"},
            {"accion": "Depositar", "valor": "2"},
            {"accion": "Retirar", "valor": "3"},
            {"accion": "Transferir", "valor": "4"},
            {"accion": "Cerrar sesión", "valor": "5"},
        ]

        is_not_back = True

        while is_not_back:
            print("\nElija una opción\n")
            draw_menu(options)

            option_selected = validate_option(options)

            if option_selected == 1:
                self.crear_cuenta()
            elif option_selected == 2:
                self.depositar()
            elif option_selected == 3:
                self.retirar()
            elif option_selected == 4:
                self.transferir()
            elif option_selected == 5:
                is_not_back = self.cerrar_sesion()

    def crear_cuenta(self):
        """Crear cuenta bancaria function"""
        usuario = self.sesion

        if usuario.cuentas is not None:
            print("\nUsted ya posee una cuenta bancaria")
        else:
            numero_de_cuenta = random_acount_number()

            saldo = saldo_inicial("\nSaldo inicial de la cuenta: ")

            usuario.cuentas = [Cuenta(numero_de_cuenta, saldo)]

            print(f"\nSu nuevo número de cuenta: {numero_de_cuenta}")
            print(f"\nSaldo de la cuenta: {saldo}$")

    def depositar(self):
        """Depositar function"""
        usuario = self.sesion

        if usuario.cuentas is None:
            print("\nUsted no posee una cuenta bancaria")
        else:
            saldo = saldo_inicial("\nSaldo a depositar: ")

            usuario.cuentas[0].depositar(saldo)
            print("\nDeposito realizado con exito")
            print(f"\nSaldo: {usuario.cuentas[0].saldo}$")

    def retirar(self):
        """Retirar function"""
        usuario = self.sesion

        if usuario.cuentas is None:
            print("\nUsted no posee una cuenta bancaria")
        else:
            print(f"\nSaldo Actual: {usuario.cuentas[0].saldo}$")

            saldo = saldo_inicial("\nSaldo a retirar: ")

            if saldo > usuario.cuentas[0].saldo:
                print("\nFondos insuficientes")
            else:
                usuario.cuentas[0].retirar(saldo)
                print("\nRetiro realizado con exito")
                print(f"\nSaldo Restante: {usuario.cuentas[0].saldo}$")

    def transferir(self):
        """Transferir function"""
        usuario = self.sesion

        if usuario.cuentas is None:
            print("\nUsted no posee una cuenta bancaria")
        else:
            cedula = valid_cedula("\nCédula de la persona a transferir: ")

            while (
                len([usuario for usuario in self.usuarios if usuario.cedula == cedula])
                == 0
            ):
                print(
                    "\nLa cédula proporcionada no pertenece a ningún usuario. Intente con otra cédula"
                )
                cedula = valid_cedula("\nCédula de la persona a transferir: ")

            user_to_transfer = [
                usuario for usuario in self.usuarios if usuario.cedula == cedula
            ]

            print(f"\nDatos del usuario con cédula: {cedula}")
            print(f"\nNúmero de cuenta: {user_to_transfer[0].cuentas[0].account_id}")

            numero_de_cuenta = valid_account()

            if numero_de_cuenta != user_to_transfer[0].cuentas[0].account_id:
                print("\nNúmero de cuenta incorrecto")
            else:
                print(f"\nSaldo Actual: {usuario.cuentas[0].saldo}$")

                saldo = saldo_inicial("\nSaldo a transferir: ")

                if saldo > usuario.cuentas[0].saldo:
                    print("\nFondos insuficientes")
                else:
                    user_to_transfer[0].cuentas[0].depositar(saldo)
                    usuario.cuentas[0].retirar(saldo)
                    print("\nTransferencia realizada con exito")
                    print(f"\nSaldo transferido: {saldo}")
                    print(f"\nSaldo Restante: {usuario.cuentas[0].saldo}$")

    def cerrar_sesion(self):
        """Cerrar sesión function"""
        self.sesion = None
        return False
