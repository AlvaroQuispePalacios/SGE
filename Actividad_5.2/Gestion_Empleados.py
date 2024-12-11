empleados = []
seleccionar = -1
while(seleccionar != 4): 
    seleccionar = int(input("\n1. Agregar nuevo empleado\n2. Calcular promedio de los salarios\n3. Buscar empleado por una posicion especifica\n4. Salir\n"))

    if(seleccionar == 1):
        try:
            nombre = str(input("Dime el nombre del empleado: "))
            salario = int(input("Dime el salario: "))
            listaPosiciones =[]
            posiciones = ()
            seleccionarPosicion = -1
            while(seleccionarPosicion != 2):
                seleccionarPosicion = int(input("1. Agregar posicion\n2. Salir\n"))
                if(seleccionarPosicion == 1):
                    posicion = str(input("Dime la posicion: "))
                    listaPosiciones.append(posicion)
                
            posiciones = tuple(listaPosiciones)

            empleados.append({
                "nombre": nombre,
                "posiciones": posiciones,
                "salario": salario
            })
        except ValueError:
            print("Ha ocurrido un error creando un empleado")
            
    elif(seleccionar == 2):
        if(len(empleados) > 0):
            suma = 0
            for empleado in empleados:
                suma += empleado["salario"]
            promedio = suma/len(empleados)
            print(f"El promedio de los salarios es: {promedio}")
        else:
            print("No existen empleados")

    elif(seleccionar == 3):
        posicionEmpleado = str(input("Dime la posicion a buscar: "))
        posicionEncontrada = False
        for empleado in empleados:
            if(posicionEmpleado in empleado["posiciones"]):
                posicionEncontrada = True
                print("\n")
                for clave, valor in empleado.items():
                    print(f"{clave}:{valor}")
            else:
                posicionEncontrada= False
        
        if(posicionEncontrada == False):
            print("El rol buscado no existe")

        
print(empleados)

