libros = []
seleccionar = -1
idActual = 0
 
while(seleccionar != 4):
    seleccionar = int(input("\n1. Registrar nuevos libros\n2. Consultar información de libro por ID\n3. Mostrar Todos los libros de un genero especifico\n4. Salir\n"))

    if(seleccionar == 1):
        titulo = str(input("Dime el titulo: "))
        autor = str(input("Dime el autor: "))
        listaGeneros = []
        generos = ()
        seleccionarOpcionTupla = -1
        while(seleccionarOpcionTupla != 2):
            seleccionarOpcionTupla = int(input("1. Agregar Género\n2. Salir\n"))
            if(seleccionarOpcionTupla == 1):
                genero = str(input("Dime el género: "))
                listaGeneros.append(genero)
        
        generos = tuple(listaGeneros)

        for libro in libros:
            idActual += 1
     
        libros.append(
            {
                "id": idActual + 1,
                "titulo": titulo,
                "autor": autor,
                "generos": generos
            }
        )

    elif(seleccionar == 2):
        idBuscar = int(input("Dime el ID del libro a buscar: "))
        for libro in libros:
            if(libro["id"] == idBuscar):
                for clave, valor in libro.items():
                    print(f"\n{clave}: {valor}")
       
                break
            else:
                print("No existe un libro con ese ID")

    elif(seleccionar == 3):
        libroGenero = str(input("Dime el genero del libro a buscar: "))
        for libro in libros:
            if(libroGenero in libro["generos"]):
                for clave, valor in libro.items():
                    print(f"\n{clave}: {valor}")

    


