productos = {
    "producto1" : {
        "precio": 22,
        "stock": 2
    }
}

provedores = {
    "provedor1": {
        "telefono": 631956919,
        "productos_suministrados": ["cosa1", "cosa2"]
    }
}

seleccionar = -1
while(seleccionar != 5):
    seleccionar = int(input("1. Registrar producto\n2. Registrar provedor\n3. Mostrar productos\n4. Mostrar provedores\n5. Salir\n"))

    if(seleccionar == 1):
        nombre = input("Dime el nombre del producto: ")
        precio = input("Dime el precio: ")
        stock = int(input("Dime el stock: "))

        productos[nombre] = {
            "precio": precio,
            "stock": stock
        }
    
    elif(seleccionar == 2):
        nombre = input("Dime el nombre del proveedor: ")
        telefono = int(input("Dime el numero del proveedor: "))
        productosP = []

        seleccionarProducto = -1
        while(seleccionarProducto != 2):
            seleccionarProducto = int(input("1. Agregar producto del proveedor\n2. Salir\n"))

            if(seleccionarProducto == 1):
                nombreProducto = input("Dime el nombre del producto: ")
                productosP.append(nombreProducto)
            
        provedores[nombre] = {
            "telefono": telefono,
            "productos_suministrados": productosP
        }

    elif(seleccionar == 3):
        print("\n")
        for clave, valor in productos.items():
            print(f"Nombre producto: {clave}")
            for claveV, valorV in valor.items():
                print(f"{claveV}: {valorV}")

    
    elif(seleccionar == 4):
        for clave, valor in provedores.items():
            print(f"Nombre proveedor: {clave}")
            for claveV, valorV in valor.items():
                print(f"{claveV}: {valorV}")
