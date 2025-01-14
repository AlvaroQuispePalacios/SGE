contactos = [ 
    {
        "nombre": "Alvaro",
        "telefono": 631956919,
        "email": "alonsol1569@gmail.com"
    }
]

seleccionar = -1
while(seleccionar != 5):
    seleccionar = int(input("1. Mostrar Agenda\n2. Añadir Contacto\n3. Borrar Contacto\n4. Modificar Contacto\n5. Salir\n"))

    if(seleccionar == 1):
        for contacto in contactos:
            for clave, valor in contacto.items():
                print(f"{clave}: {valor}")
            
            print("\n")

    elif(seleccionar == 2):
        nombre = input("Dime el nombre: ")
        telefono = int(input("Dime el numero de telefono: "))
        email = input("Dime el correo: ")

        contactos.append(
            {
                "nombre": nombre,
                "telefono": telefono,
                "email": email
            }
        )

    elif(seleccionar == 3):
        contactoExiste = False
        nombre = input("Dime el nombre del contacto: ")

        for contacto in contactos:
            if(nombre == contacto["nombre"]):
                contactoExiste = True
                index = contactos.index(contacto)
                # NO funciona el remove aqui porque es cuando es igual por ejemplo: animales =["perro", "gato"]
                # animales.remove("perro")
                # Elimina a "perro" de la lista de animales
                # En cambio del funciiona con el index
                del contactos[index]
                break
    
        if(not(contactoExiste)):
            print("El contacto no existe")
            
    elif(seleccionar == 4):
        contactoExiste = False
        nombre = input("Dime el nombre del contacto: ")
        index = 1

        for contacto in contactos:
            if(nombre == contacto["nombre"]):
                contactoExiste = True
                index = contactos.index(contacto)
                break
        
        if(contactoExiste):
            seleccionarModificar = -1
            while(seleccionarModificar != 3):
                seleccionarModificar = int(input("1. Modificar telefono\n2. Modificar email\n3. Salir\n"))

                if(seleccionarModificar == 1):
                    nuevoTelefono = int(input("Dime el nuevo numero de telefono: "))
                    contactos[index].update(
                        {
                            "telefono": nuevoTelefono
                        }
                    )
                
                elif(seleccionarModificar == 2):
                    nuevoEmail = input("Dime el email: ")
                    contactos[index]["email"] = nuevoEmail

        else:
            print("El contacto no existe")
