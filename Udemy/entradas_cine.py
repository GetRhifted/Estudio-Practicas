def cantidad_entradas():
    while True:
        try:
            entradas = int(input("Ingresa la cantidad de entradas que deseas facturar: "))
            if entradas <= 0:
                raise ValueError("Recuerda ingresar al menos una (1) entrada y valores positivos.")
            return entradas
        except ValueError as e:
            print(e)

def calcular_edades(entradas):
    edades = []
    for entrada in range(entradas):
        while True:
            try:
                edad = int(input(f"Ingresa la edad de la persona número {entrada + 1}: "))
                if edad < 0:
                    raise ValueError("No puedes ingresar valores negativos.")
                edades.append(edad)
                break
            except ValueError as e:
                print(e)
    return edades

def calcular_precios(edades):
    precio = 0
    for edad in edades:
        if edad <= 12:
            precio += 5
        elif 13 <= edad <= 64:
            precio += 10
        elif edad >= 65:
            precio += 7
    return precio

def main():
    print("Bienvenidos a la registradora de precios.\nPor favor, ingresa la siguiente información:")
    entradas = cantidad_entradas()
    edades = calcular_edades(entradas)
    precio = calcular_precios(edades)
    print(f"El precio total a pagar para las entradas registradas es de: {precio} pesos.")

main()

