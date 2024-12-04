import time
segundos = int(input("Dime los segundo a esperar: "))

for i in range(segundos, 0 , -1):
    time.sleep(1)
    print(i)