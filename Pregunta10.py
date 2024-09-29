 #Implementar un programa que pida al usuario una fecha, en orden mes-día-año, con formato como
 #8/9/1636 o Septiembre 8, 1636

def HayComa(x):
    max = len(x)
    i=0
    verdad=True
    es=0
    while i<max:
        if x[i]==',':
            es= es + 1
        i=i+1
    if es == 1:
        verdad = True
    else:
        verdad = False
    return verdad

def NombreMes(x):
   match x.lower():
        case "enero":
            return "01"
        case "febrero":
            return "02"
        case "marzo":
            return "03"
        case "abril":
            return "04"
        case "mayo":
            return "05"
        case "junio":
            return "06"
        case "julio":
            return "07"
        case "agosto":
            return "08"
        case "setiembre":
            return "09"
        case "septiembre":
            return "09"
        case "octubre":
            return "10"
        case "noviembre":
            return "11"
        case "diciembre":
            return "12"
        case _:
            return "Mes no válido"

def Fecha1(x): #9/8/1636
    i=0
    max = len(x)
    mes=''
    dia=''
    año=''
    while x[i] !='/':
        mes=mes + x[i]
        i=i+1
    i=i+1
    while x[i]!='/':
        dia=dia + x[i]
        i=i+1
    i=i+1
    while i<max:
        año=año+x[i]
        i=i+1
    return dia, mes, año

def Fecha2(x):
    i=0
    max = len(x)
    mes=''
    dia=''
    año=''
    while x[i] !=' ':
        mes=mes + x[i]
        i=i+1
    i=i+1
    while x[i]!=',':
        dia=dia + x[i]
        i=i+1
    i=i+1
    while i<max:
        año=año+x[i]
        i=i+1
    return dia, mes, año

cadena=input("Ingresar una fecha: ")
aux = HayComa(cadena)
if aux == True:
    d, mes, a = Fecha2(cadena)
    m = NombreMes(mes)
    fecha = a + '-' + m + '-' + d 
    print("La fecha es " + str(fecha))
else: 
    d, m, a = Fecha1(cadena)
    fecha = a + '-' + m + '-' + d
    print("La fecha es " + str(fecha))



