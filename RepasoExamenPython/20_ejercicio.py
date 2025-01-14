estudiantes = [
    {
        "nombre": "Alvaro",
        "edad": 23,
        "calificaciones": (2, 4, 5)
    }
]

seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Crear esudiante\n2. Mostrar estudiantes\n3. Ver promedio\n4. Salir\n"))

    if(seleccionar == 1):
        nombre = input("Dime el nombre: ")
        edad = input("Dime la edad: ")
        calificaciones = []

        seleccionarC = -1
        while(seleccionarC != 2):
            seleccionarC = int(input("1. Agregar calificacion\n2.Salir\n"))

            if(seleccionarC == 1):
                calificacion = int(input("Dime la calificacion: "))
                calificaciones.append(calificacion)
            

        estudiantes.append(
            {
                "nombre": nombre,
                "edad": edad,
                "calificaciones": tuple(calificaciones)
            }
        )
    elif(seleccionar == 2):
        for estudiante in estudiantes:
            for clave, valor in estudiante.items():
                print(f"{clave}: {valor}")
        print("\n")
    
    elif(seleccionar == 3):
        for estudiante in estudiantes:
            sumador = 0
            nombre = estudiante["nombre"]
            calificacionesEstudiante = estudiante["calificaciones"]
            for i in calificacionesEstudiante:
                sumador += i
            print(f"El promedio de {nombre} es {sumador/len(calificacionesEstudiante)}")
        