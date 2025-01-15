# Registro de notas por asignatura
estudiantes = {
    "Alvaro": [("matematicas", 4), ("filosofia", 2)]
}


seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Agregar estudiante\n2. Calcular promedio de un estudiante\n3. Encontrar estudiante con mejor promedio\n4. Salir\n"))

    if(seleccionar == 1):
        try:
            nombre = input("Dime el nombre del estudiante: ")
            calificaciones = []

            seleccionarCalificacion = -1 
            while(seleccionarCalificacion != 2):
                seleccionarCalificacion = int(input("1. Agregar materia\n2. Salir\n"))

                if(seleccionarCalificacion == 1):
                    nombreMateria = input("Dime el nombre de la materia: ")
                    calificacionMateria = int(input("Dime la calificacion de la materia: "))

                    calificaciones.append(tuple([nombreMateria, calificacionMateria]))

            estudiantes[nombre] = calificaciones
        except ValueError:
            print("El valor introducido no es valido")

print(estudiantes)