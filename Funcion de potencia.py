#Funcion_de_potencia
#Funcion de Potencia ,retorna la potencia del primero elevado al segundo parametr

import math
base = int(input("Que base? "))
potencia = int(input("¡Que potencia de " +str(base)+" ? "))
print(str(base) + " elevado a la potencia "+ str(potencia)+" es "+str(int(math.pow(base,potencia))))
