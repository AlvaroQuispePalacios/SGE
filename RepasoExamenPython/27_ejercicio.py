# Gestion empleados
empleados = [
    {
        "nombre": "Alvaro",
        "posiciones": ("administrador", "esclavo"),
        "salario": 1000
    }
]

seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Agregar empleado\n2. Calcular promedio de los salarios\n3. Buscar empleado por posicion\n"))

    if(seleccionar == 1):
        try:
            nombre = input("Dime el nombre del empleado: ")
            salario = int(input("Dime el salario: "))
            posiciones = []

            seleccionarPosicion = -1
            while(seleccionarPosicion != 2):
                seleccionarPosicion = int(input("1. Agregar posicion\n2. Salir\n"))

                if(seleccionarPosicion == 1):
                    posicion = input("Dime la posicion: ")
                    posiciones.append(posicion)

            empleados.append(
                {
                    "nombre": nombre,
                    "posiciones": tuple(posiciones),
                    "salario": salario
                }
            )
            
        except ValueError:
            print("El valor introducido no es valido")
    
    elif(seleccionar == 2):
        sumador = 0
        for empleado in empleados:
            sumador += empleado["salario"]
        
        print(f"El promedio es: {sumador/len(empleados)}")

    elif(seleccionar == 3):
        try:
            buscarPosicion = input("Dime la posicion a buscar: ")
            encontrarPosicion = False

            for empleado in empleados:
                for posicionesEmpleado in empleado["posiciones"]:
                    if(buscarPosicion == posicionesEmpleado):
                        encontrarPosicion = True
                        print(empleado)

            if(not(encontrarPosicion)):
                print("No se han encontrado la posicion buscada")
        except ValueError:
            print("El valor introducido no es valido")

print(empleados)