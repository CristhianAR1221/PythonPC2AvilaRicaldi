#Al enviar mensajes de texto o twittear, no es raro acortar las palabras para ahorrar tiempo o espacio,
#por ejemplo, omitiendo las vocales.
#Implemente un programa que solicite al usuario una cadena de texto y luego retorne ese mismo
#texto pero con todas las vocales (A, E, I, O y U) omitidas, ya sea que se ingresen en mayúsculas o
#minúsculas.
def EsVocal(x):
    Verdad=True
    if x=='a' or x=='e' or x=='i' or x=='o' or x=='u':
        Verdad=True
    else:
        Verdad=False
    return Verdad
cad=input("Mencionar una frase: ")
longitud = len(cad)
i=0
cadnueva=''
aux=True
while i < longitud:
    aux=EsVocal(cad[i])
    if aux == False:
        cadnueva=cadnueva + cad[i]
    i=i+1
print("La nueva cadena es: ")
print(cadnueva)
