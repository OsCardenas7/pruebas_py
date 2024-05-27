import time
from random import randint

#radnint() numero randnom integer
#uniform() numero random decimal
#random() numero aleatorio entre 0 y 1

print("BIENVENIDO")
print("Sección de sorteos")


flag = False
while(flag == False):
    n1 = int(input("Digite el primer número del rango para el sorteo: "))
    n2 = int(input("Digite el segundo número del rango para el sorteo: "))
    if(n1<n2):
        flag = True
    else:
        print("no se puede realizar la acción, digitar primero el número menor y luego el mayor")



a = randint(n1, n2)

print("Cargando número...")
time.sleep(3)

print("El número seleccionado es... ")
time.sleep(5)

print(str(a))
