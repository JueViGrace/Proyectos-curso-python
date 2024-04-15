"""Utility functions"""


def not_empty(input_text: str):
    """Not empty validation"""
    value = input(input_text)

    while value.strip() == "" or value == "":
        print("\nEl valor no puede estar vacío")
        value = input(input_text)

    return value


def valid_int(input_text: str, error_text: str):
    """Number valiation"""
    value = not_empty(input_text)

    while not value.isdigit():
        print(error_text)
        value = not_empty(input_text)

    return value


def valid_float(input_text: str, error_text: str):
    """Number valiation"""
    value = not_empty(input_text).replace(",", ".")

    while not value.replace(".", "").isdigit():
        print(error_text)
        value = not_empty(input_text)

    while float(value) < 0.0:
        print("\nEl saldo inicial debe ser mayor a 0")
        value = not_empty(input_text)

    return format(float(value), ".2f")


def finish():
    """Finish function"""
    return print("\nFinalizado")


def draw_menu(options: list):
    """Print menu items"""

    options = [(f'Para {option["accion"]}: {option["valor"]}\n') for option in options]

    for option in options:
        print(option)


def validate_option(options: list):
    """Options validation function"""
    option_selected = valid_int(
        "\n¿Qué acción desea realizar?: ", "\nLa opción seleccionada debe ser un número"
    )

    while (
        len([option for option in options if option["valor"] == option_selected]) == 0
    ):
        print("\nLa opción seleccionada no se encuentra en las opciones disponibles")
        option_selected = valid_int(
            "\n¿Qué acción desea realizar?: ",
            "\nLa opción seleccionada debe ser un número",
        )
    return int(option_selected)
