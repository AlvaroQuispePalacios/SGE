agenda = {
    "Alvaro": {
            "datos": [(631956919, "movil"), (631956919, "trabajo")],
            "correos": ["alonsol1569@gmail.com"]
        }
}
seleccionar = -1

while(seleccionar != 4):
    seleccionar = int(input("1. Añadir contacto\n2. Modificar los numeros o correos electronicos de un contacto\n3. Buscar contactos por tipo de numero\n4. Salir"))

    if(seleccionar == 1):
        nombreValido = False
        while(nombreValido == False):
            try:
                nombre = str(input("Dime el nombre del estudiante: "))
                if(agenda.get(nombre) != None): 
                    raise ValueError
                nombreValido = True
            except ValueError:
                print("El alumno ya existe")
        
        