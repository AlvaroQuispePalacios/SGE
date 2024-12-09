productos = {
    "platano": {
        "precio": 22,
        "stock": 3
    }
}
provedores = {}

seleccionar = -1
while(seleccionar != 5):
    seleccionar = int(input("1. Registrar nuevo producto\n2. Registrar nuevo provedor\n3. Mostrar todos los productos\n4. Mostrar todos los provedores\n5. Salir\n"))

    if(seleccionar == 1):
        nombreProducto = str(input("Dime el nombre del producto: "))
        precio = str(input("Precio del producto: "))
        stock = int(input("Cantidad del producto: "))

        productos[nombreProducto] = {
            "precio": precio,
            "stock": stock
        }

    elif(seleccionar == 2):
        nombreProvedor = str(input("Dime el nombre del proveedor: "))
        telefono = int(input("Telefono : "))
        lista = []

        seleccionarOpcionLista = -1
        while(seleccionarOpcionLista != 2):
            seleccionarOpcionLista = int(input("1. Agregar producto\n2. Salir\n"))
            if(seleccionarOpcionLista == 1):
                productoLista = str(input("Dime el producto a agregar a la lista: "))
                lista.append(productoLista)

        provedores[nombreProvedor] = {
            "telefono": telefono,
            "lista": lista
        }

    elif(seleccionar == 3):
        for clave, valor in productos.items():
            print(f"\nProducto {clave}\nPrecio: {valor["precio"]}\nCantidad: {valor["stock"]}\n")
    elif(seleccionar == 4):
        for clave, valor in provedores.items():
            print(f"\nNombre contacto: {clave}\nTelefono: {valor["telefono"]}\nLista de productos suministrados: {valor["lista"]}\n")