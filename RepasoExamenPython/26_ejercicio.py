biblioteca = [
    {
        "isbn": 1,
        "titulo": "Libro 1",
        "autor": "Alvaro",
        "generos": ("accion", "suspenso")
    }
]

seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Regisrar libro\n2. Consulta po ID\n3. Mostrar libros por genero\n4. salir\n"))

    if(seleccionar == 1):
        isbn = len(biblioteca) + 1
        titulo = input("Dime el titulo: ")
        autor = input("Dime el autor: ")
        generos = []

        seleccionarGeneros = -1
        while(seleccionarGeneros != 2):
            seleccionarGeneros = int(input("1. Agregar genero\n2. Salir\n"))

            if(seleccionarGeneros == 1):
                genero = input("Dime el nombre del genero: ")
                generos.append(genero)
            
        biblioteca.append(
            {
                "isbn": isbn,
                "titulo": titulo,
                "autor": autor,
                "generos": tuple(generos)
            }
        )
    
    elif(seleccionar == 2):
        buscarLibro = int(input("Dime el ISBN del libro: "))
        libroEncontrado = False

        for libro in biblioteca:
            if(buscarLibro == libro["isbn"]):
                libroEncontrado = True        
                for clave, valor in libro.items():
                    print(f"{clave}: {valor}")
                break

            if(not(libroEncontrado)):
                print("El libro no existe")
    
    elif(seleccionar == 3):
        buscarGenero = input("Dime el genero a buscar: ")
        
        for libro in biblioteca:
            generosLibro = libro["generos"]
            for generoLibro in generosLibro:
                if(buscarGenero == generoLibro):
                    print(libro)


print(biblioteca)