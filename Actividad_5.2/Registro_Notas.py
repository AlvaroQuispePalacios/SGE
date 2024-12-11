estudiantes = {"Alvaro":[("matematicas", 2),("matematicas", 2),("matematicas", 2),]}


seleccionar = -1
while(seleccionar != 0):
    seleccionar = int(input("1. Agregar estudiante con materias y calificaciones\n2. Calcular promedio de un estudiante\n3. Encontrar al estudiante con mejor promedio"))

    if(seleccionar == 1):
        nombre = str(input("Dime el nombre del estudiante: "))
        listaMateriasCalificaciones = []
        tuplaMateriasCalificaciones = ()
        agregarMateriaCalificacion = -1
        while(agregarMateriaCalificacion != 2):
            agregarMateriaCalificacion = int(input("1. Agregar materia y calificacion\n2. Salir\n"))
            materia = str(input("Dime la materia: "))
            calificacion = int(input("Dime la calificación: "))
            
            listaMateriasCalificaciones.append(materia, calificacion)
            
        
        estudiantes[nombre] = listaMateriasCalificaciones
        
