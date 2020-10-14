# Programa que lee un código postal desde teclado, lo busca dentro
# de un archivo json y en caso de encontrarse el código imprime
# el estado y municipio al que pertenece el código. En caso de que no
# se encuentre imprime: "Código Postal NO encontrado".
# 
# Tecnológico Nacional de México Campus Colima
# Ingeniería en Sistemas Computacionales
# Lenguaje de programación Python
#
# José Andrés Ceballos Vadillo
# 17460386


# Importar libreria para trabajar con json
import json

# Método para solicitar código postal y validar formato
def get_postal_code():
    while True:
        code = input("Ingrese el código postal a buscar: ")
        if len(code) == 5:
            try:
                int(code)
                break
            except:
                print("Debe ingresar solo números!")
        else:
            print("El código postal se debe componer de 5 dígitos")
    return code

# Método para abrir json e iterar sus elementos en busqueda de código postal
def find_postal_code(code, json_file):
    with open(json_file, encoding="utf8") as file:
        data = json.load(file)
        for elem in data['data']:
            if code == elem['d_codigo']:
                return elem
        return False

if __name__ == "__main__":
    postal_code = get_postal_code()
    response = find_postal_code(postal_code, 'codigos_postales.json')
    if response == False:
        print("\nCódigo Postal NO encontrado")
    else:
        print(f"El código pertenece a... \nEstado: {response['d_estado']}\nEstado: {response['d_nmpio']} ")