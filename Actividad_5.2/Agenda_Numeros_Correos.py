agenda = {
    "Alvaro": {
            "datos": [(631956919, "movil"), (631956919, "trabajo")],
            "correos": ["alonsol1569@gmail.com"]
        }
}
seleccionar = -1

while(seleccionar != 4):
    seleccionar = int(input("1. Añadir contacto\n2. Modificar los numeros o correos electronicos de un contacto\n3. Buscar contactos por tipo de numero\n4. Salir\n"))
  
    if(seleccionar == 1):
        nombre = ""
        datos = []
        correos = []
        nombreValido = False

        while(nombreValido == False):
            try:
                nombre = str(input("Dime el nombre del contacto: "))
                if(agenda.get(nombre) != None): 
                    raise ValueError
                nombreValido = True
            except ValueError:
                print("El contacto ya existe")
        

        seleccionarAgregarNumero = -1
        while(seleccionarAgregarNumero != 2):
            seleccionarAgregarNumero = int(input("1. Agregar nuevo telefono\n2. Salir\n"))
            if(seleccionarAgregarNumero == 1):
                numero = int(input("Dime el numero de telefono: "))
                categoria = ""
                seleccionarCategoria = -1
                while(seleccionarCategoria != 3):
                    seleccionarCategoria = int(input("Seleccione la categoria:\n1. móvil\n2. trabajo\n3. Salir\n"))
                    if(seleccionarCategoria == 1):
                        categoria = "móvil"
                    elif(seleccionarCategoria == 2):
                        categoria = "trabajo"
                    break
                datos.append((numero, categoria))

        
        seleccionarAgregarCorreo = -1
        while(seleccionarAgregarCorreo != 2):
            seleccionarAgregarCorreo = int(input("1. Agregar Correo\n2. Salir\n"))
            if(seleccionarAgregarCorreo == 1):
                correo = str(input("Dime el correo: "))
                correos.append(correo)

        agenda[nombre] = {
            "datos": datos,
            "correos": correos
        }

    elif(seleccionar == 2):
        nombre = str(input("Dime el nombre del contacto: "))
        contactoExiste = False
        if(agenda.get(nombre) != None):
            seleccionarModificar = -1
            while(seleccionarModificar != 3):
                seleccionarModificar = int(input("1. Modificar Correo\n2. Modificar numero telefono\n3. Salir\n"))
                if(seleccionarModificar == 1):
                    for numeros in agenda.get(nombre)["datos"]:
                        

        


        

        # for clave in agenda.keys():
        #     if(clave == nombre):
        #         contactoExiste = True
        #         seleccionarModificar = -1
        #         while(seleccionarModificar != 3):
        #             seleccionarModificar = int(input("1. Modificar Correo\n2. Modificar numero telefono"))

        #         break


            
     



print(agenda)


