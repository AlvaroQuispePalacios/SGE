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
    
    elif(seleccionar == 2):
        nombre = input("Dime el nombre del estudiante: ")

        if(estudiantes[nombre]):
            sumador = 0
            for item in estudiantes[nombre]:
                sumador += item[1]    
            print(f"El promedio de {nombre} es: {sumador/len(estudiantes[nombre])}")
        else:
            print("El estudiante no existe")

    elif(seleccionar == 3):
        mejorPromedio = None

        for clave, valor in estudiantes.items():
            sumador = 0
            for item in valor:
                sumador += item[1]
            
            promedio = sumador/len(valor)

            if(mejorPromedio == None):
                mejorPromedio = [clave, promedio]
            else:
                if(promedio > mejorPromedio[1]):
                    mejorPromedio = [clave, promedio]
        
        print(f"El mayor promedio es de {mejorPromedio[0]} con {mejorPromedio[1]}")



        



print(estudiantes)