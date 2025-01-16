# Inventario de una tienda
productos = [
    {
        "id": 1,
        "nombre": "carbon",
        "detalle": ("22€", 4)
    }
]

seleccionar = -1
while(seleccionar != 4):
    seleccionar = int(input("1. Agregra producto\n2. Actualizar Stock\n3. Mostrar productos con menos de 5 unidades\n4. Salir\n"))

    if(seleccionar == 1):
        nombre = input("Dime el nombre del producto: ")
        precio = input("Dime el precio: ")
        stock = int(input("Dime la cantidad del producto: "))

        productos.append(
            {
                "id": len(productos) + 1,
                "nombre": nombre,
                "detalle": tuple([precio, stock])
            }
        )

    elif(seleccionar == 2):
        identificador = int(input("Dime el identificador del producto: "))

        for producto in productos:
            if(identificador == producto["id"]):
                nuevoStock = int(input("Dime el nuevo stock de producto: "))
                producto["detalle"] = tuple([producto["detalle"][0], nuevoStock])
                break
    
    elif(seleccionar == 3):
        for producto in productos:
            if(producto["detalle"][1] < 5):
                print(producto)

print(productos)