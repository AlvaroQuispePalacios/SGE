libros = []
seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("\n1. Registrar nuevos libros\n2. Consultar información de libro por ID\n3. Mostrar Todos los libros de un genero especifico\n4. Salir\n"))

    if(seleccionar == 1):
        titulo = str(input("Dime el titulo: "))
        autor = str(input("Dime el autor: "))
        generos
        seleccionarOpcionTupla = -1
        while(seleccionarOpcionTupla != 2):
            seleccionarOpcionTupla = int(input("1. Agregar Género\n2. Salir\n"))
            if(seleccionarOpcionTupla == 1):
                genero = str(input("Dime el género: "))
                tupla = (genero)
                generos = generos + tupla

        libros.append(
            {
                "id": 1,
                "titulo": titulo,
                "autor": autor,
                "generos": generos
            }
        )
print(libros)
