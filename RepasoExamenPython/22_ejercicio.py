contactos = {
    "Alvaro": 631956919,
    "Aldo": 95684875
}

seleccionar = -1
while(seleccionar != 2):
    seleccionar = int(input("1. Agregar Contacto\n2. Salir\n"))

    if(seleccionar == 1):
        contactoExiste = False
        nombre = input("Dime el nombre del contacto: ")

        for key in contactos.keys():
            if(nombre == key):
                contactoExiste = True
                break

        if(not(contactoExiste)):
            numero = int(input("Dime el numero de telefono: "))
            contactos[nombre] = numero
        else:
            print("El contacto ya existe")
            
        


print(contactos)