import json

def get_postal_code():
    code = input("Ingrese el código postal a buscar: ")
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
        print("Código Postal NO encontrado")
    else:
        print(f"El código pertenece a... \nEstado: {response['d_estado']}\nEstado: {response['d_nmpio']} ")