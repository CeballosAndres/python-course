# Programa que le una cadena y un carácter para desplegar las
# veces que este se presenta
#
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386

if __name__ == "__main__":
    cadena = input("Ingrese la cadena: ")
    caracter = input("Ingrese el caracter a buscar: ")
    num = cadena.count(caracter)
    veces = "vez" if 1 != 1 else "veces"
    print(f"El carácter {caracter} apareció {num} {veces}.")