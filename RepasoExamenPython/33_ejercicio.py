def contador_llamadas(func):
    contador = 0  # Variable interna para contar llamadas
    
    def envoltura(*args, **kwargs):
        nonlocal contador  # Permite modificar la variable dentro de la función anidada
        contador += 1
        print(f"La función '{func.__name__}' ha sido llamada {contador} veces.")
        return func(*args, **kwargs)
    
    return envoltura

@contador_llamadas
def saludar(nombre):
    print(f"¡Hola, {nombre}!")

# Llamadas a la función con nombres diferentes
saludar("Ana")
saludar("Carlos")
saludar("María")

