# Programa que le desde teclado y almacenar el número de 
# control, el nombre y 3 calificaciones para 3 alumnos 
# utilizando una lista de listas
# [ [num_control, nombre, calif1, calif2, calif3], 
# [num_control, nombre, calif1, calif2, calif3], 
# [num_control, nombre, calif1, calif2, calif3] ]
# Recorrer los elementos de las listas y calcular e imprimir: 
# Número de control, Nombre y Promedio
#
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386

if __name__ == "__main__":
    campos = ["Numero de control", "Nombre", "Calificación 1", "Calificación 2", "Calificación 3"]
    alumnos = 3
    lista_alumnos = []

    print("Ingrese los siguientes datos.")
    # Caputa de los datos
    for alumno in range(alumnos):
        print(f"\nPara el alumno {alumno + 1}.")
        lista_alumnos.append([])
        for campo in range(len(campos)):
            value = input(f"{campos[campo]}: ")
            if campo > 1:
                value = int(value)
            lista_alumnos[alumno].append(value)
    
    print("\nLos datos capturado son:")
    # Presentación de los datos
    for alumno in lista_alumnos:
        promedio = sum(alumno[2:])/len(alumno[2:])
        print(f"Número control: {alumno[0]} - Nombre: {alumno[1]} - Promedio: {promedio}")