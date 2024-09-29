#Escribe un programa que encuentre la suma de todos los números primos menores que 100.

#Comenzaremos evaluando si un numero es primo o no, recordemos que esto sucede cuando el numero tiene dos divisores
def EsPrimo(a):
    j = 1
    Factores = 0
    PRIMO = True
    while j < a: 
        aux = a%j #10/1 => resto = 0
        if aux == 0: 
            Factores = Factores + 1
        j = j +1
    if Factores == 1:
        #Es numero primo
        Primo = True
    else:
        Primo = False

    return Primo

SumaPrimos = 0
i = 2
ListaPrimos = []
print("SUMA DE PRIMOS MENORES DE " + str(100))
while i < 100:
    if EsPrimo(i) == True:
        SumaPrimos = SumaPrimos + i
        ListaPrimos.append(i)
        i = i+1
    else:
        i = i+1

print("Los primos son " + str(ListaPrimos))
print("La suma es " + str(SumaPrimos))


       




