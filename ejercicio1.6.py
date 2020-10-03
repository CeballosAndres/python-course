import json

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