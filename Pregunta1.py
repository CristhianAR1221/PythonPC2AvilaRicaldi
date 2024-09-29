#Escribe un programa en Python para encontrar los números que son divisibles por 7 y múltiplos de 5,
#en el rango de 1500 y 2700 (ambos incluidos).

print("Contabilizaremos los numeros que son multiplos de 5 y divisibles de 7")
i = 1500
x = 0
while i<2700:
    a = i%35
    if a == 0:
        x = x + 1
        i = i+1
    else:
        i = i + 1 

print("Los numeros divisibles por 7 y multiplos de 5 que estan en el intervalo mostrado es" + str(x))