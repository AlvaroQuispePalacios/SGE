# Gestión de estudiantes y asignaturas
estudiantes = {
    "Alvaro": {
        "algebra": 5,
        "aritmetica": 7
    }
}

seleccionar = -1


while(seleccionar != 4):
    try:
        seleccionar = int(input("1. Agregar estudiante\n2. Consultar asignaturas y notas de un estudiante\n3. Calcular promedio de notas de un estudiante\n4. Salir\n"))
        
        if(seleccionar == 1):
            estudianteExiste = False
            nombre = input("Dime el nombre del estudiante: ")

            try:
                if(estudiantes[nombre]):
                    estudianteExiste = True
            except KeyError:
                print("Creando nuevo estudiante")

            if(not(estudianteExiste)):
                seleccionarAsigNota = -1
                while(seleccionarAsigNota != 2):
                    seleccionarAsigNota = int(input("1. Agregar asignatura\n2. Salir\n"))
                    if(seleccionarAsigNota == 1):
                        asignatura = input("Dime el nombre de la asignatura: ")
                        nota = int(input("Dime la nota: "))

                        estudiantes[nombre] = {
                            asignatura: nota
                        }
            else:
                print("El estudiante ya existe")

        elif(seleccionar == 2):
            nombre = input("Dime el nombre del estudiante: ")
            estudianteEncontrado = False
            try:
                if(estudiantes[nombre]):
                    estudianteEncontrado = True
            except KeyError:
                print("El estudiante no existe")

            if(estudianteEncontrado):
                print(f"Nombre: {nombre}")
                for asignatura, nota in estudiantes[nombre].items():
                    print(f"{asignatura}: {nota}")

            
        elif(seleccionar == 3):
            nombre = input("Dime el nombre del estudiante: ")
            estudianteEncontrado = False

            try:
                if(estudiantes[nombre]):
                    estudianteEncontrado = True
            except KeyError:
                print("El estudiante no existe")

            if(estudianteEncontrado):
                sumador = 0
                for nota in estudiantes[nombre].values():
                    sumador += nota
                
                print(f"El promedio de {nombre} es {sumador/len(estudiantes[nombre].values())}")

    except ValueError:
        print("Valor no valido")
