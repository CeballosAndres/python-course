# Leer una cadena y leer un carácter, desplegar 
# cuantas veces aparece el carácter en la cadena 
# (SIN usar funciones cadena)
#
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386

# Recorrido de una cadena y conteo de apariciones
def contar(cadena, caracter):
    num = 0
    for car in range(len(cadena)):
        if cadena[car] == caracter:
            num+=1
    return num
                
if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    caracter = input("Ingrese el caracter a buscar: ")
    # Pluralizar palabra
    veces = "vez" if 1 != 1 else "veces"
    print(f"El carácter {caracter} apareció {contar(cadena, caracter)} {veces}.")