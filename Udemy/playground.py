def get_range():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de numeros con la que deseas trabajar: "))
            if cantidad < 0:
                raise ValueError("Por favor introduce un valor positivo")
            return cantidad
        except ValueError as e:
            print(e)

def generar_lista(cantidad):
    lista_numeros = []
    while len(lista_numeros) < cantidad:
        try:
            numero = int(input(f"Por favor, ingresa el numero {len(lista_numeros) + 1}:  "))
            lista_numeros.append(numero)
        except ValueError:
            print("Por favor ingresa valores validos.")
    return lista_numeros

def mediana(lista_numeros):
    lista_numeros = sorted(lista_numeros)
    numeros = len(lista_numeros)
    if numeros % 2 == 1:
        return lista_numeros[numeros // 2]
    else:
        medio1 = lista_numeros[numeros // 2]
        medio2 = lista_numeros[numeros // 2 - 1]
        return (medio1 + medio2) / 2


def main():
    cantidad = get_range()
    lista_numeros = generar_lista(cantidad)
    resultado = mediana(lista_numeros)
    print(f"La mediana de los numeros ingresados es de: \n {resultado}. ")

def reversed_word():
    while True:
        try:
            cadena = input("Ingresa la palabra que deseas invertir: ")
            if len(cadena) == 0:
                raise ValueError("Debes ingresar al menos una palabra.")
            print(cadena[::-1])
            break
        except ValueError as e:
            print(e)

reversed_word()