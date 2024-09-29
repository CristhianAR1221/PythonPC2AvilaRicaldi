#Escribe un programa que encuentre todos los números perfectos menores que 1000. Un número
#perfecto es un número entero positivo que es igual a la suma de sus divisores propios positivos
#(excluyendo el propio número).
print("Prueba")
def NumeroPerfecto(a):
    i = 1
    SumaPerfecta = 0
    Es = True
    while i < a:
        aux = a%i #6/1
        if aux == 0:
            #Es un divisor
            SumaPerfecta = SumaPerfecta + i
            i = i + 1
        else:
            i = i + 1    
    if SumaPerfecta == a:
        Es = True
    else:
        Es = False
    return Es

print("Los numers perfectos por debajo del 1000 son: ")
j = 2
numero = 1000
Serie = []
while j < 1000:
    aux = NumeroPerfecto(j)
    if aux == True:
        Serie.append(j)
        j = j + 1
    else:
        j = j +1
print("La lista es")
print(str(Serie))



