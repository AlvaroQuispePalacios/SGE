inventario = [
    {
        "id": 1,
        "nombre": "Producto 1",
        "detalle": (4.8, 4)
    }
]

seleccionar = -1
idActual = 0

while(seleccionar != 0):
    seleccionar = int(input("1. Agregar producto al inventario\n2. Actualizar el stock de un producto usando id\n3. Mostrar productos con menos de 5 unidades en stock\n"))
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
        
