inventario = [
    {
        "id": 1,
        "nombre": "Producto 1",
        "detalle": (4.8, 4)
    }
]

seleccionar = -1
idActual = 0

while(seleccionar != 4):
    seleccionar = int(input("1. Agregar producto al inventario\n2. Actualizar el stock de un producto usando id\n3. Mostrar productos con menos de 5 unidades en stock\n4. Salir\n"))
    if(seleccionar == 1):
        nombre = str(input("Dime el nombre del producto: "))
        precio = int(input("Dime el precio del producto: "))
        cantidad = int(input("Dime la cantidad del producto: "))

        for producto in inventario:
            idActual += 1
        
        inventario.append({
            "id": idActual + 1,
            "nombre": nombre,
            "detalle": (precio, cantidad)
        })
        
    elif(seleccionar == 2):
        idProductoValido = False
        while idProductoValido == False:
            try:
                idProducto = int(input("Dime la id del producto: "))
                idProductoValido = True
            except ValueError:
                print("El id no es valido")

        productoEncontrado = False
        for producto in inventario:
            if (producto["id"] == idProducto):
                productoEncontrado = True
                print("Producto encontrado")
                nuevaCantidad = int(input("Dime la cantidad: "))
                producto["detalle"] = (producto["detalle"][0], nuevaCantidad)
                break

            if(not(productoEncontrado)):
                print("El producto no se ha encontrado")

    elif(seleccionar == 3):
        for producto in inventario:
            if(producto["detalle"][1] < 5):
                print(producto)

print(inventario)