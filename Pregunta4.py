#Imaginemos que lo han contratado para un colegio donde se desea realizar un sistema por el cual se
#pueda generar un listado de “n” alumnos y 3 calificaciones que corresponden a alguna de sus
#materias.
#Puede usar el siguiente esquema a manera de ejemplo
#{
#Alumno: Juan,
#Notas: [10, 12, 15]
#}
#Una vez completado el ingreso de los datos, su programa debe mostrar en pantalla el listado
#completo de los alumnos.
def ingresar_datos():
    alumnos = {}  # Diccionario para almacenar los datos de los alumnos
    n = int(input("¿Cuántos alumnos desea ingresar? "))  # Cantidad de alumnos

    for i in range(n):
        nombre = input(f"Ingrese el nombre del alumno {i + 1}: ")
        
        # Lista para almacenar las tres notas del alumno
        notas = []
        
        for j in range(3):
            nota = float(input(f"Ingrese la nota {j + 1} para {nombre}: "))
            notas.append(nota)
        
        # Guardar las notas en el diccionario con el nombre del alumno como clave
        alumnos[nombre] = notas
    
    return alumnos

def mostrar_listado(alumnos):
    print("\nListado de Alumnos y sus Notas:")
    for nombre, notas in alumnos.items():
        print(f"Alumno: {nombre}, Notas: {notas}")

# Programa principal
alumnos = ingresar_datos()  # Ingresar datos de los alumnos
mostrar_listado(alumnos)  # Mostrar el listado completo
