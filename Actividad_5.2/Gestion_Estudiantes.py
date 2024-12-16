estudiantes = {
    "Alvaro": {
        "matematicas": 2,
        "filosofia": 3
    }
}


seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Agregar estudiante con asigmaturas y notas\n2. Consultar las asignaturas y notas de un estudiante\n3. Calcular el promedio de notas de un estudiante\n4. Salir\n"))

    if(seleccionar == 1):
        nombreValido = False
        while(nombreValido == False):
            try:
                nombre = str(input("Dime el nombre del estudiante: "))
                if(estudiantes.get(nombre) != None): 
                    raise ValueError
                nombreValido = True
            except ValueError:
                print("El alumno ya existe")
                
        asignatura = str(input("Dime la asignatura: "))
        nota = 0

        notaValida = False
        while(notaValida == False):
            try:
                nota = int(input("Dime la nota: "))
                notaValida = True
            except ValueError:
                print("La nota no es valida")
        
        estudiantes[nombre] = {
            asignatura: nota
        }

    elif(seleccionar == 2):
        nombre = str(input("Dime el nombre del estudiante: "))
        estudianteExiste = False
        if(estudiantes.get(nombre) != None):
            estudianteExiste = True
            for estudiante in estudiantes:
                print(estudiantes)        
        
        if(estudianteExiste == False):
            print("El estudiante no existe")
            
    elif(seleccionar == 3):
        nombre = str(input("Dime el nombre del estudiante: "))
        estudianteExiste = False

        if(estudiantes.get(nombre) != None):
            sumador = 0
            numeroAsignaturas = 0
            estudianteExiste = True

            for notas in estudiantes.get(nombre).values():
                sumador += notas
                numeroAsignaturas += 1

            print(sumador/numeroAsignaturas)
          
        if(estudianteExiste == False):
            print("El estudiante no existe")


