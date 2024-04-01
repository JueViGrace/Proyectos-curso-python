""" 
    Proyecto 2: Tareas pendientes
"""

from datetime import datetime


def valid_int(input_text: str, error_text: str):
    """Number valiation"""
    value = input(input_text)

    while not value.isdigit():
        print(error_text)
        value = input(input_text)

    return value


def not_empty(input_text: str, error_text: str):
    """Not empty validation"""
    value = input(input_text)

    while value == "":
        print(error_text)
        value = input(input_text)

    return value


def valid_code(tasks: list, input_text: str):
    """Code validation function"""
    codigo = valid_int(input_text, "\nEl código debe ser un número entero")

    while len(list(filter(lambda task: task["codigo"] == codigo, tasks))) > 0:
        print("\nEl código introducido ya existe en la lista de tareas")
        codigo = valid_int(
            "\nCódigo de la tarea: ", "\nEl código debe ser un número entero"
        )

    return codigo


def valid_title(input_text: str):
    """Title validation function"""
    title = not_empty(input_text, "\nEl título no puede estar vacío")

    while len(title) > 20:
        print("\nEl título de la tarea puede tener como máximo 20 caracteres")
        title = not_empty(input_text, "\nEl título no puede estar vacío")

    while title.isdigit():
        print("\nEl título no debe contener solo números")
        title = not_empty(input_text, "\nEl título no puede estar vacío")

    return title


def valid_description(input_text: str):
    """Description validation function"""
    description = not_empty(input_text, "\nLa descripción no puede estar vacía")

    return description


def valid_status(input_text: str):
    """Status validation function"""
    status = not_empty(input_text, "\nEl status no puede estar vacío")

    while status.isdigit():
        print("\nEl status no debe ser un número")
        status = not_empty(input_text, "\nEl status no puede estar vacío")

    while status.lower() != "pendiente" and status.lower() != "completado":
        print("\nEl status de la tarea debe ser 'pendiente' o 'completado'")
        status = not_empty(input_text, "\nEl status no puede estar vacío")

    return status


def valid_date(input_text: str):
    """Date validation function"""
    created_at = not_empty(input_text, "\nLa fecha de creación no puede estar vacía")

    valid_date = False

    while not valid_date:
        try:
            datetime.strptime(created_at, "%d-%m-%Y")
            valid_date = True
        except ValueError:
            valid_date = False
            print("\nLa fecha de creación debe ser con el formato DD-MM-YYYY")
            created_at = not_empty(
                input_text, "\nLa fecha de creación no puede estar vacía"
            )

    return created_at


def find(input_value: str, field: str, tasks: list):
    """Find task by given field and value"""
    if len(tasks) == 0:
        print("\nNo hay tareas que mostrar")
    else:
        data = list(filter(lambda task: task[field] == input_value, tasks))
        if len(data) == 0:
            print("\nNo hay tareas que mostrar")
        else:
            draw_task(data)


def draw_task(data: list):
    """Print current tasks"""
    for task in data:
        print(
            f"""
--------------- Tareas ---------------
    Código: {task['codigo']}
    Título: {task['titulo']}
    Descripción: {task['description']}
    Status: {task['status']}
    Fecha de creación: {task['created_at']}
             """
        )


def get_task(tasks: list):
    """get tasks function"""
    menu_options = [
        {"accion": "Completadas", "valor": "1"},
        {"accion": "Pendientes", "valor": "2"},
        {"accion": "Atras", "valor": "3"},
    ]
    is_not_back = True

    while is_not_back:
        print("\nElija una opción\n")
        for option in menu_options:
            print(f'Para {option["accion"]}: {option["valor"]}\n')

        option_selected = validate_option(menu_options)

        if option_selected == 1:
            find("completado", "status", tasks)

        elif option_selected == 2:
            find("pendiente", "status", tasks)

        elif option_selected == 3:
            is_not_back = False


def filter_task(tasks: list):
    """Filter task function"""
    menu_options = [
        {"accion": "Filtrar por código", "valor": "1"},
        {"accion": "Filtrar por título", "valor": "2"},
        {"accion": "Filtrar por fecha", "valor": "3"},
        {"accion": "Atras", "valor": "4"},
    ]
    is_not_back = True

    while is_not_back:
        print("\nElija una opción\n")
        for option in menu_options:
            print(f'Para {option["accion"]}: {option["valor"]}\n')

        option_selected = validate_option(menu_options)

        if option_selected == 1:
            codigo = valid_int(
                "\nCódigo de la tarea: ", "\nEl código debe ser un número entero"
            )
            find(codigo, "codigo", tasks)

        elif option_selected == 2:
            titulo = valid_title("\nTítulo de la tarea: ")
            find(titulo, "titulo", tasks)

        elif option_selected == 3:
            created_at = valid_date("\nFecha de creación de la tarea: ")
            find(created_at, "created_at", tasks)

        elif option_selected == 4:
            is_not_back = False


def create_task(tasks: list):
    """Create task function"""
    codigo = valid_code(tasks, "\nCódigo de la tarea: ")

    titulo = valid_title("\nTítulo de la tarea: ")

    description = valid_description("\nDescripción de la tarea: ")

    status = valid_status("\nStatus de la tarea: ")

    created_at = valid_date("\nFecha de creación de la tarea: ")

    task = {
        "codigo": codigo,
        "titulo": titulo,
        "description": description,
        "status": status,
        "created_at": created_at,
    }

    return [*tasks, task]


def update(task, tasks):
    """Update task if there are"""
    codigo = valid_int(
        "\nCódigo de la tarea a modificar: ",
        "\nEl código debe ser un número entero",
    )

    menu_options = [
        {"accion": "Actualizar código", "valor": "1"},
        {"accion": "Actualizar título", "valor": "2"},
        {"accion": "Actualizar descripción", "valor": "3"},
        {"accion": "Actualizar status", "valor": "4"},
        {"accion": "Actualizar fecha", "valor": "5"},
        {"accion": "Atras", "valor": "6"},
    ]

    is_not_back = True

    if task["codigo"] == codigo:
        while is_not_back:
            print("\nElija una opción\n")
            for option in menu_options:
                print(f'Para {option["accion"]}: {option["valor"]}\n')

            option_selected = validate_option(menu_options)

            if option_selected == 1:
                new_codigo = valid_code(
                    tasks,
                    "\nNuevo código de la tarea: ",
                )

                task["codigo"] = new_codigo

            elif option_selected == 2:
                titulo = valid_title("\nNuevo título de la tarea: ")
                task["titulo"] = titulo

            elif option_selected == 3:
                description = valid_description("\nNueva descripción de la tarea: ")
                task["description"] = description

            elif option_selected == 4:
                status = valid_status("\nNuevo status de la tarea: ")
                task["status"] = status

            elif option_selected == 5:
                created_at = valid_date("\nFecha de creación de la tarea: ")
                task["created_at"] = created_at

            elif option_selected == 6:
                is_not_back = False
    else:
        print("\nEl código elegido no existe")

    return task


def update_task(tasks: list):
    """Update task function"""

    if len(tasks) != 0:
        print("\nNo existen tareas")
        return []

    return list(map(update, tasks))


def delete_task():
    """Delete task function"""


def finish():
    """Finish function"""
    return print("Finalizado")


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


def main():
    """Main function"""
    tasks = []
    options = [
        {"accion": "Listado de tareas", "valor": "1"},
        {"accion": "Filtrar tareas", "valor": "2"},
        {"accion": "Añadir tarea", "valor": "3"},
        {"accion": "Actualizar tarea", "valor": "4"},
        {"accion": "Eliminar tarea", "valor": "5"},
        {"accion": "Salir", "valor": "6"},
    ]

    is_not_exit = True

    while is_not_exit:
        print("\nElija una opción\n")
        for option in options:
            print(f'Para {option["accion"]}: {option["valor"]}\n')

        option_selected = validate_option(options)

        if option_selected == 1:
            get_task(tasks)
        elif option_selected == 2:
            filter_task(tasks)
        elif option_selected == 3:
            tasks = create_task(tasks)
        elif option_selected == 4:
            tasks = update_task(tasks)
        elif option_selected == 5:
            delete_task()
        elif option_selected == 6:
            finish()
            break


main()
