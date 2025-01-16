inventario = {
    "categoria1": {
        "producto1": {
            "cantidad_disponible": 3,
            "precio_unitario": 5
        }
    }
}

seleccionar = -1
while(seleccionar != 4):
    try:
        seleccionar = int(input("1. Mostrar inventario Actual\n2. Añadir nuevo producto\n3. Modificar cantidad y precio\n4. Salir\n"))

        if(seleccionar == 1):
            # 
            for categoria, productos in inventario.items():
                print(f"{categoria}")
                for clave, valor in productos.items():
                    print(f"\tNombre producto: {clave}\n\t\t {valor}")
                    # for cantidad, precio in valor.items():


        elif(seleccionar == 2):
            categoria = input("Dime la categoria si la categoria no existe se creara una: ")
            categoriaExiste = False

            #  En este bucle buscamos si la categoria escrita por el usuario existe en el inventario
            for key in inventario.keys():
                # Agregar un producto a una categoria existente
                if(categoria == key):
                    categoriaExiste = True
                    nombreProducto = input("Dime el nombre del producto: ")
                    productoExiste = False
                    # Verificamos que el producto exista, si el producto existe le decimos al usuario que el producto ya existe, si no existe creamos el producto
                    for keyProducto in inventario[categoria].keys():
                        if(nombreProducto == keyProducto):
                            productoExiste = True

                    # Si el producto no existe podemos agregarlo a la categoria especificada
                    if(not(productoExiste)):
                        cantidad = int(input("Dime la cantidad del producto: "))
                        precio = int(input("Dime el precio del producto: "))
                        
                        inventario[categoria][nombreProducto] = {
                            "cantidad_disponible": cantidad,
                            "precio_unitario": precio
                        }
                    else:
                        print("El producto ya existe")
 
            # Aqui creamos la categoria y añadimos el producto
            if(not(categoriaExiste)):
                nombreProducto = input("Dime el nombre del producto: ")
                cantidad = int(input("Dime la cantidad del producto: "))
                precio = int(input("Dime el precio del producto: "))

                # Primero creamos la categoria con un diccionario vacio
                inventario[categoria] = {}

                # Añdimos el producto a categoria recien creada
                inventario[categoria][nombreProducto] = {
                    "cantidad_disponible": cantidad,
                    "precio_unitario": precio
                }
        

        elif(seleccionar == 3):
            nombreProducto = input("Dime el nombre del producto: ")
            productoExiste = False
            # Busca el producto en todas las categorias
            # El el primer bucle obtenemos el nombre de la categoria para despues poder acceder al producto que se encuentra en ella
            for categoria, productos in inventario.items():
                # En este segundo bucle obtenemos el nombre de los productos de la categoria y si alguno coincide con el nombre del producto que el usuario ingreso procedemos a preguntarle al usuario por la nueva cantidad y nuevo precio
                for clave, valor in productos.items():
                    if(nombreProducto == clave):
                        productoExiste = True
                        nuevaCantidad = int(input("Dime la nueva cantidad del producto: "))
                        nuevoPrecio = int(input("Dime el nuevo precio: "))

                        inventario[categoria][nombreProducto] = {
                            "cantidad_disponible": nuevaCantidad,
                            "precio_unitario": nuevoPrecio
                        }
                        break

            if(not(productoExiste)):
                print("El producto buscado no existe")

    except ValueError:
        print("Valor no valido")