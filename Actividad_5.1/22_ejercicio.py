seleccionar = -1
contactos = []
while(seleccionar != 2):
    seleccionar = int(input("Que quieres hacer?\n1. Crear Contacto\n2. Salir\n"))
    if(seleccionar == 1):
        contactoExiste = False
        nombre = str(input("Dime el nombre del contacto: "))
        telefono = str(input("Dime el numero de telefono: "))

        for contacto in contactos:
            if(contacto.get("nombre") == nombre):
                print("El contacto ya existe")
                contactoExiste = True
        
        if(contactoExiste == False):
            contactos.append({
                "nombre": nombre,
                "telefono": telefono
            })
            print("Contacto creado")


print(contactos)