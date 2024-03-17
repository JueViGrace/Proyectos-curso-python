# Estudiante Daniel Zabala

Proyecto 01: Programa para gestionar estudiantes universitarios.

```$
# Se declara el diccionario que contendrá los datos de un estudiante.
estudiante = {
    "nombre": "test",
    "apellido": "test",
    "cedula": 1,
    "nota_1": 0,
    "nota_2": 0,
    "nota_3": 0,
    "promedio": 0,
}

# Se establece la lista que contendra a todos los estudiantes.
estudiantes = [estudiante]

# Por ultimo una lista de opciones que el usuario pueda seleccionar.
options = [
    {"accion": "Listado de estudiantes", "valor": "1"},
    {"accion": "Registrar estudiante", "valor": "2"},
    {"accion": "Actualizar estudiante", "valor": "3"},
    {"accion": "Eliminar estudiante", "valor": "4"},
    {"accion": "Salir", "valor": "5"},
]
```

## Listado de estudiantes

Al marcar el número uno (1) se imprimirán los estudiantes que existen actualmente.

```$
# Se imprimen los datos de los estudiantes en consola.

--------------- Alumno {index + 1} ---------------
    Nombre:   {estudiante['nombre']}
    Apellido: {estudiante['apellido']}
    Cédula:   {estudiante['cedula']}
    Nota 1:   {estudiante['nota_1']}
    Nota 2:   {estudiante['nota_2']}
    Nota 3:   {estudiante['nota_3']}
    Promedio: {estudiante['promedio']}

```

## Registro de estudiantes

Al marcar el número dos (2) se le pedirá al usuario los datos del nuevo estudiante.

```$
# Se declaran variables que contendrán los datos del nuevo estudiante.

name_input = input('Ingrese el nombre del estudiante: ')
...

# Luego se crea un nuevo estudiante y se añade a la lista.

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

```

## Actualización de estudiante

Al marcar el número tres (3) se le pedirá al usuario la cédula del estudiante que quiera actualizar.

```$
# Antes de realizar cualquier operación en la lista se crea una copia y se valida si la cédula ingresada existe en alguno de los estudiantes actuales.

id_estudiante = input('Ingrese la cédula del estudiante a actualizar: ')
print()

while not id_estudiante.isdigit() or int(id_estudiante) < 0 or not id_estudiante:
    print("La cédula debe ser un número entero y mayor a 0")
    id_estudiante = input('Ingrese la cédula del estudiante a actualizar: ')

for index, estudiante in enumerate(estudiantes.copy()):
    if int(id_estudiante) == estudiante['cedula']:
    ...

# Se declaran variables que contendrán los datos actualizados del estudiante.

name_input = input('Ingrese el nombre del estudiante: ')
...

# Luego se crea un nuevo diccionario y se sobreescribe el valor en la posición donde se encuentra el estudiante.

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
```

## Eliminación de estudiante

Al marcar el número cuatro (4) se le pedirá al usuario la cédula del estudiante que quiera eliminar.

```$

id_estudiante = input('Ingrese la cédula del estudiante a borrar: ')
print()

while not id_estudiante.isdigit() or int(id_estudiante) < 0 or not id_estudiante:
    print("La cédula debe ser un número entero y mayor a 0")
    id_estudiante = input('Ingrese la cédula del estudiante a borrar: ')


for estudiante in estudiantes.copy():
    if int(id_estudiante) == estudiante['cedula']:
        estudiantes.remove(estudiante)
```

## Salir

Si el usuario no desea realizar ninguna acción marcando el número cinco (5) se terminará el programa
