""" Proyecto 1, Listado de estudiantes """

estudiante = {
    "nombre": "test",
    "apellido": "test",
    "cedula": 1,
    "nota_1": 0,
    "nota_2": 0,
    "nota_3": 0,
    "promedio": 0,
}

estudiantes = [estudiante]

options = [
    {"accion": "Listado de estudiantes", "valor": "1"},
    {"accion": "Registrar estudiante", "valor": "2"},
    {"accion": "Actualizar estudiante", "valor": "3"},
    {"accion": "Eliminar estudiante", "valor": "4"},
    {"accion": "Salir", "valor": "5"},
]

is_not_exit = True

print()

while is_not_exit:
    print('---- Elija una opción ----')
    for option in options:
        print()
        print(f'Para {option['accion']}: {option["valor"]}')

    print()
    option_selected = input("Elija una de las opciones de arriba: ")
    print()

    valid_type = option_selected.isdigit()

    if valid_type:
        option_value = int(option_selected)

        if option_value in range(1,5):

            if option_value == 1:
                print('-------- Listado de estudiantes --------')

                if len(estudiantes) == 0:
                    print()
                    print('-------- Actualmente no hay estudiantes --------')
                    print()
                else:
                    for index, estudiante in enumerate(estudiantes):
                        print(f'''
--------------- Alumno {index + 1} ---------------
    Nombre:   {estudiante['nombre']}
    Apellido: {estudiante['apellido']}
    Cédula:   {estudiante['cedula']}
    Nota 1:   {estudiante['nota_1']}
    Nota 2:   {estudiante['nota_2']}
    Nota 3:   {estudiante['nota_3']}
    Promedio: {estudiante['promedio']}
                            ''')

                input('Presione enter para volver')
            elif option_value == 2:
                print('-------- Registrar estudiante --------')

                name_input = input('Ingrese el nombre del estudiante: ')

                while name_input.replace(',', '.').isdigit() or not name_input:
                    print("El nombre debe ser un nombre válido")
                    name_input = input('Ingrese el nombre del estudiante: ')

                lastname_input = input('Ingrese el apellido del estudiante: ')

                while lastname_input.replace(',', '.').isdigit() or not lastname_input:
                    print("El apellido debe ser un apellido válido")
                    name_input = input('Ingrese el apellido del estudiante: ')

                id_input = input('Ingrese la cédula del estudiante: ')

                while not id_input.isdigit() or int(id_input) < 0 or not id_input:
                    print("La cédula debe ser un número entero y mayor a 0")
                    id_input = input('Ingrese la cédula del estudiante: ')

                grade_1_input = input('Ingrese la nota 1 del estudiante: ').replace(',','.')

                grade_1 = 0

                if '.' in grade_1_input:
                    grade_1 = float(grade_1_input)
                else:
                    grade_1 = int(grade_1_input)

                while not grade_1_input.replace('.','').isdigit() or grade_1 < 0.0 or not grade_1_input:
                    print("La nota 1 debe ser un número y mayor a 0")
                    id_input = input('Ingrese la nota 1 del estudiante: ')

                grade_2_input = input('Ingrese la nota 2 del estudiante: ').replace(',','.')

                grade_2 = 0

                if '.' in grade_2_input:
                    grade_2 = float(grade_2_input)
                else:
                    grade_2 = int(grade_2_input)

                while not grade_2_input.replace('.','').isdigit() or grade_2 < 0.0 or not grade_2_input:
                    print("La nota 2 debe ser un número y mayor a 0")
                    id_input = input('Ingrese la nota 2 del estudiante: ')

                grade_3_input = input('Ingrese la nota 3 del estudiante: ').replace(',','.')

                grade_3 = 0

                if '.' in grade_3_input:
                    grade_3 = float(grade_3_input)
                else:
                    grade_3 = int(grade_3_input)

                while not grade_3_input.replace('.','').isdigit() or grade_3 < 0.0 or not grade_3_input:
                    print("La nota 3 debe ser un número y mayor a 0")
                    id_input = input('Ingrese la nota 3 del estudiante: ')

                average_grade = (grade_1 + grade_2 + grade_3) / 3

                new_estudiante = {
                        "nombre": name_input,
                        "apellido": lastname_input,
                        "cedula": int(id_input),
                        "nota_1": grade_1,
                        "nota_2": grade_2,
                        "nota_3": grade_3,
                        "promedio": round(average_grade, 2),
                }

                estudiantes.append(new_estudiante)

                input('Estudiante Añadido, presione enter para volver')

            elif option_value == 3:
                print('-------- Actualizar estudiante --------')
                print()

                id_estudiante = input('Ingrese la cédula del estudiante a actualizar: ')
                print()

                while not id_estudiante.isdigit() or int(id_estudiante) < 0 or not id_estudiante:
                    print("La cédula debe ser un número entero y mayor a 0")
                    id_estudiante = input('Ingrese la cédula del estudiante a actualizar: ')

                for index, estudiante in enumerate(estudiantes.copy()):
                    if int(id_estudiante) == estudiante['cedula']:

                        name_input = input('Ingrese el nombre del estudiante: ')

                        while name_input.replace(',', '.').isdigit() or not name_input:
                            print("El nombre debe ser un nombre válido")
                            name_input = input('Ingrese el nombre del estudiante: ')

                        lastname_input = input('Ingrese el apellido del estudiante: ')

                        while lastname_input.replace(',', '.').isdigit() or not lastname_input:
                            print("El apellido debe ser un apellido válido")
                            name_input = input('Ingrese el apellido del estudiante: ')

                        id_input = input('Ingrese la cédula del estudiante: ')

                        while not id_input.isdigit() or int(id_input) < 0 or not id_input:
                            print("La cédula debe ser un número entero y mayor a 0")
                            id_input = input('Ingrese la cédula del estudiante: ')

                        grade_1_input = input('Ingrese la nota 1 del estudiante: ').replace(',','.')

                        grade_1 = 0

                        if '.' in grade_1_input:
                            grade_1 = float(grade_1_input)
                        else:
                            grade_1 = int(grade_1_input)

                        while not grade_1_input.replace('.','').isdigit() or grade_1 < 0.0 or not grade_1_input:
                            print("La nota 1 debe ser un número y mayor a 0")
                            id_input = input('Ingrese la nota 1 del estudiante: ')

                        grade_2_input = input('Ingrese la nota 2 del estudiante: ').replace(',','.')

                        grade_2 = 0

                        if '.' in grade_2_input:
                            grade_2 = float(grade_2_input)
                        else:
                            grade_2 = int(grade_2_input)

                        while not grade_2_input.replace('.','').isdigit() or grade_2 < 0.0 or not grade_2_input:
                            print("La nota 2 debe ser un número y mayor a 0")
                            id_input = input('Ingrese la nota 2 del estudiante: ')

                        grade_3_input = input('Ingrese la nota 3 del estudiante: ').replace(',','.')

                        grade_3 = 0

                        if '.' in grade_3_input:
                            grade_3 = float(grade_3_input)
                        else:
                            grade_3 = int(grade_3_input)

                        while not grade_3_input.replace('.','').isdigit() or grade_3 < 0.0 or not grade_3_input:
                            print("La nota 3 debe ser un número y mayor a 0")
                            id_input = input('Ingrese la nota 3 del estudiante: ')

                        average_grade = (grade_1 + grade_2 + grade_3) / 3

                        estudiante_actualizado = {
                        "nombre": name_input,
                        "apellido": lastname_input,
                        "cedula": int(id_input),
                        "nota_1": grade_1,
                        "nota_2": grade_2,
                        "nota_3": grade_3,
                        "promedio": round(average_grade, 2),
                        }
                        estudiantes[index] = estudiante_actualizado
                        print()
                        print(f'-------- Estudiante {id_estudiante} actualizado --------')
                        print()
                    else:
                        print("------- La cédula ingresada no se encuentra en la lista de estudiantes -------")
                        print()

            elif option_value == 4:
                print('-------- Eliminar estudiante --------')
                print()

                id_estudiante = input('Ingrese la cédula del estudiante a borrar: ')
                print()

                while not id_estudiante.isdigit() or int(id_estudiante) < 0 or not id_estudiante:
                    print("La cédula debe ser un número entero y mayor a 0")
                    id_estudiante = input('Ingrese la cédula del estudiante a borrar: ')


                for estudiante in estudiantes.copy():
                    if int(id_estudiante) == estudiante['cedula']:
                        estudiantes.remove(estudiante)
                        print()
                        print(f'-------- Estudiante {id_estudiante} eliminado --------')
                        print()
                    else:
                        print("------- La cédula ingresada no se encuentra en la lista de estudiantes -------")
                        print()

        elif option_value == 5:
            is_not_exit = False
        else:
            print(f"------- {option_value} no es una opción -------")
            print()
    else:
        print("------- Debe escribir el número asignado a alguna de las opciones -------")
        print()
print('Terminado')
