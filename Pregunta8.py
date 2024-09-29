# Escribe una función de Python para calcular el factorial de un número (un entero no negativo). La
#función acepta el número como argumento
def Factorial(x):
    i = 1
    Mult = 1
    while i < x + 1:
        Mult = Mult * i
        i = i + 1
    return Mult
Numero = int(input("Ingrese un numero: "))
Aux = Factorial(Numero)
print("El factorial del numero es " + str(Aux))