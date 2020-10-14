# Programa que lee 10 números y calcula el promedio
#
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386

# funcion que recibe una lista de números y devuelve su promedio
def average(numbers):
    sum = 0
    for num in numbers:
        sum += num
    return sum/len(numbers)

# función para pedir n cantidad de números (al menos 1)
def get_numbers(value = 1):
    numbers = []
    for val in range(value):
        try:
            while True:
                number = int(input(f"Ingresa el {val + 1} número: "))
                numbers.append(number)
                break
        except:
            print("Ingresó un carácter no valido.")
    return numbers

if __name__ == "__main__":
    numbers = get_numbers(10)
    print(f"El promedio es: {average(numbers)}")