seleccionar = -1
contactos = []

while(seleccionar != 5):
    seleccionar = int(input("Que quieres hacer?\n1. Mostrar agenda\n2. Añadir contacto\n3. Borrar contacto\n4. Modificar contacto\n5. salir\n"))

    if(seleccionar == 1):
        if(len(contactos) == 0):
            print("No existen contactos")
        else:
            for contacto in contactos:
                print(f"Nombre: {contacto["nombre"]}\nTelefono: {contacto["telefono"]}\nEmail: {contacto["email"]}")

    elif(seleccionar == 2):
        nombre = str(input("Dime el nombre: "))
        telefono = str(input("Dime el telefono: "))
        email = str(input("Dime el email: "))

        contactos.append({
            "nombre": nombre,
            "telefono": telefono,
            "email": email
        })

    elif(seleccionar == 3):
        if(len(contactos) == 0): 
            print("No existe ningun contacto") 
        else:
            nombre = str(input("Dime el nombre del contacto a eliminar: "))
            encontrado = False
            for i in range(0, len(contactos)):
                if(contactos[i]["nombre"] == nombre):
                    del contactos[i]
                    encontrado = True
                    break

            if not encontrado:
                print("Contacto no encontrado")
    elif(seleccionar == 4):
        if(len(contactos) == 0): 
            print("No existe ningun contacto")
        else:
            nombre = str(input("Dime el nombre del contacto a modificar: "))
            seleccionar = -1
            encontrado = False

            for i in range(0, len(contactos)):
                if(contactos[i].get("nombre") == nombre):
                    encontrado = True
                    while(seleccionar != 3):
                        seleccionar = int(input("1. Modificar telefono\n2. Modificar email\n3. Salir\n"))
                        if(seleccionar == 1):
                            contactos[i]["telefono"] = str(input("Dime el nuevo telefono: "))
                        elif(seleccionar == 2):
                            contactos[i]["email"] = str(input("Dime el nuevo email: "))
                        elif(seleccionar == 3):
                            print("Contacto modificado correctamente")   

            if not encontrado:
                print("Contacto no encontrado")

