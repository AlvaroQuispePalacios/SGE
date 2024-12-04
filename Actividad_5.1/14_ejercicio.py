meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre")

numero = int(input("Dime un numero: "))

if(numero >= 0 and numero < len(meses)):
    print(meses[numero])