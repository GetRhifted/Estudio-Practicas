def validador_cantidad():
    while True:
        try:
            cantidad_numeros = int(input("Ingresa la cantidad de numeros con los que quieres trabajar: "))
            if cantidad_numeros < 0:
                raise ValueError("Recuerda elegir una cantidad positiva.")
            return cantidad_numeros
        except ValueError as e:
            print(e)

def generar_lista(cantidad_numeros):
    lista_numeros = []
    while len(lista_numeros) < cantidad_numeros:
        try:
            numero = int(input(f"Ingresa el numero numero {len(lista_numeros) + 1}: "))
            lista_numeros.append(numero)
        except ValueError:
            print("Por favor, ingresa un numero valido.")
    return lista_numeros
    
        
def promediador(lista_numeros):
    return sum(lista_numeros) / len(lista_numeros)

def calculadora_mediana(lista_numeros):
    lista_numeros = sorted(lista_numeros)
    numeros = len(lista_numeros)
    if numeros % 2 == 1:  # Aquí corregimos el error
        return lista_numeros[numeros // 2]
    else:
        # Si es par, la mediana es el promedio de los dos valores centrales
        medio1 = lista_numeros[numeros // 2 - 1]
        medio2 = lista_numeros[numeros // 2]
        return (medio1 + medio2) / 2


def main():
    cantidad_numeros = validador_cantidad()
    lista_numeros = generar_lista(cantidad_numeros)
    promedio = promediador(lista_numeros)
    mediana = calculadora_mediana(lista_numeros)
    print(f"El promedio para los numeros ingresados es de: {promedio} ")
    print(f"La mediana para los numeros ingresados es de {mediana}")

main()