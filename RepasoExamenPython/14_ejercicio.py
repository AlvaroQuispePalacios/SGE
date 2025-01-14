meses = ("Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio", "Agosto", "Setiembre", "Octubre", "Noviembre", "Diciembre")

mes = int(input("Dime un numero: "))
if(mes >= 1 and mes <= len(meses)):
    print(meses[mes - 1])