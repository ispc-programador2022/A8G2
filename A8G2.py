# Buenas, dejaré documentada algunas partes para hacer más comprensible el código.

# Cualquier duda no duden en comunicarse por el grupo

# Presentación mediante print
print("Bienvenido/a al primer proyecto grupal del ISPC. La función de esta app es realizar cálculos mediante funciones llamadas por el usuario")


# La siguiente funcion cumple lo solicitado en el punto, se encarga de recibir tres parametros, dos de ellos son los números solicitados debajo y el tercero es el validador para la operación a realizar.
def ing2i(valor1, valor2, operacion):
    valor1 = valor1
    valor2 = valor2

    if operacion == 1:
        resultado = valor1 + valor2
        print("Elegiste Suma, el resultado es: " + str(resultado))
    elif operacion == 2:
        resultado = valor1 - valor2
        print("Elegiste Resta, el resultado es: " + str(resultado))
    elif operacion == 3:
        resultado = valor1 * valor2
        print("Elegiste Producto, el resultado es: " + str(resultado))
    elif operacion == 4:
        resultado = valor1 % valor2
        print("Elegiste cociente, el resultado es: " + str(resultado))
    elif operacion == 5:
        resultado = valor1 * valor2
        print("Elegiste módulo, el resultado es: " + str(resultado))



# La siguiente variable se utiliza para uno de los puntos requeridos en el trabajo, que se acepten valores strings. Queda por terminar y ver esta parte
validacionStringOrInt = int(input("¿Desea trabajar solo con INT? Escriba 1 para Yes, 0 para Not "))

# Validación y de lo anteriormente dicho. Se encarga de llevarle a la función los parametros necesarios para su funcionamiento
if validacionStringOrInt == 1:
    print("Escriba dos números:")
    ing2i(int(input("Número 1: ")), int(input("Número 2: ")), (int(input(
        "¿Qué operación desea realizar? \n Escriba 1 para suma \n Escriba 2 para resta \n Escriba 3 para producto \n Escriba 4 para cociente \n Escriba 5 para módulo \n"))))
elif validacionStringOrInt != 1:
    print("Esta parte todavía no está programada ")

# El código tiene mucho que mejorar y mucho por terminar, recuerden no trabajar en la main para evitar problemas.
