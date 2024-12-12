estudiantes = {"Alvaro":[("matematicas", 2),("matematicas", 2),("matematicas", 2),]}

seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Agregar estudiante con materias y calificaciones\n2. Calcular promedio de un estudiante\n3. Encontrar al estudiante con mejor promedio\n4. Salir\n"))

    if(seleccionar == 1):
        nombre = str(input("Dime el nombre del estudiante: "))
        listaMateriasCalificaciones = []
        agregarMateriaCalificacion = -1

        while(agregarMateriaCalificacion != 2):
            try:
                agregarMateriaCalificacion = int(input("1. Agregar materia y calificacion\n2. Salir\n"))
            except ValueError:
                print("La opcion elegida no es valida")
                break
            if(agregarMateriaCalificacion == 1):
                materia = str(input("Dime la materia: "))
                try:
                    calificacion = int(input("Dime la calificación: "))
                except ValueError:
                    print("La calificacion no es valida")
                    break
                listaMateriasCalificaciones.append((materia, calificacion))
            estudiantes[nombre] = listaMateriasCalificaciones

    elif(seleccionar == 2):
        nombre = str(input("Dime el nombre del estudiante a calcular el promedio: "))
        sumador = 0
        cantidadMaterias = 0
        encontrado = False
        for clave, valor in estudiantes.items():
            if(clave == nombre):
                # Calcular promedio
                for tuplaMateriaCalificacion in valor:
                    sumador += tuplaMateriaCalificacion[1]
                    cantidadMaterias += 1

                if(cantidadMaterias != 0):
                    promedio = sumador/cantidadMaterias
                    print(f"El promedio es: {promedio}") 
            else:
                print("El usuario no existe")
                
    elif(seleccionar == 3):
        if(len(estudiantes) > 0):
            # Encontrar el mejor promedio
            listaPromedios = []
            for clave, valor in estudiantes.items():
                sumador = 0
                cantidadMaterias = 0
                for tuplaMateriaCalificacion in valor:
                    sumador += tuplaMateriaCalificacion[1]
                    cantidadMaterias += 1

                promedio = sumador/cantidadMaterias
                listaPromedios.append(promedio)

            mejorPromedio = max(listaPromedios)

            # Mostrar el estudiante con mejor promedio
            for clave, valor in estudiantes.items():
                for tuplaMateriaCalificacion in valor:
                    if(tuplaMateriaCalificacion[1] == mejorPromedio):
                        print(estudiantes[clave])
                        break


        else:
            print("No existen estudiantes")


print(estudiantes)