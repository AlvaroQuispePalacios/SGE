import time

def decorador(func):
    def envoltura():
        tiempo_inicio = time.time()

        func()
        tiempo_fin = time.time()

        print(round(tiempo_fin - tiempo_inicio))
        
        
    return envoltura

@decorador
def sumar_numeros_consecutivos():
    sumador = 0
    for i in range(1, 100000000):
        sumador += i

    print(sumador)

@decorador
def sumar_numeros_pares():
    sumador = 0
    for i in range(1, 20000000):
        if(i % 2 == 0):
            sumador += i

    print(sumador)


sumar_numeros_consecutivos()
sumar_numeros_pares()