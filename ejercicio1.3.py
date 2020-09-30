# Implementación de sentencia "break" para romper un ciclo 
# infinito (while True:) y aplíquelo en un ciclo infinito 
# que lea números enteros y se detenga cuando el número leído sea -1.
# Despliegue cuantos números se leyeron, cuantos fueron 
# menores que 10 y cuantos igual o mayores que 10.
#
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386

if __name__ == "__main__":
    print("Ingrese tantos números desee saber si son mayores o menores a 10.")
    print("Para salir ingrese -1")
    consecutivo = 0
    num = 0
    menores = 0
    mayores = 0
    while True:
        while True:
            try:
                num = int(input(f"Ingresa el {consecutivo+1} número: "))
                consecutivo+=1
                # Rompe el ciclo while interno
                break
            except:
                print("No ingreso un número. Intente de nuevo.")
        if num == -1:
            # Rompe el ciclo while externo
            break
        elif num < 10:
            menores+=1
        else:
            mayores+=1
    print(f"Se ingresaron {consecutivo-1} números.")
    print(f"{menores} menores a 10")
    print(f"{mayores} mayores o iguales a 10")
            
    