 import funcion_genrnd

 def sumgen():
    lista = genrnd(n)
    total = 0
    for i in range(0,len(lista)-1):
        for j in range(i + 1,len(lista)):
            total += lista[i] + lista[j]
    return total        
          
