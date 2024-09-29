#Por medio de un bucle While genere un código que permita el ingreso de números por teclado. El
#ingreso de los números debe ser permitido hasta que el usuario decida ya no ingresar nuevos
#números.
#Con dichos números, su programa debe evaluar cada uno de estos números e indicar la cantidad de
#números pares e impares.

x = str(input("Desea ingresar un número? "))
i=0
lista = []
aux = 0
par = 0
impar = 0
while x.lower() == 'si':
    y = int(input("Ingrese un numero "))
    aux = y%2
    lista.append(y)
    x = str(input("Desea ingresar un número? "))
    i = i + 1
    if aux == 0:
        par = par + 1
    else:
        impar = impar + 1
print("Mostraremos la siguiente lista " + str(lista))
print("Hay " + str(par) + " numero pares y " + str(impar) + " numero impares")
        

