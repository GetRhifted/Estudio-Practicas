def solicitar_numeros(cantidad):
    numeros = []
    print(f"Por favor, ingresa una cantidad de {cantidad} numeros: ")
    for i in range(cantidad):
        while True:
            try:
                numero = int(input(f"Ingresa el numero {i + 1}: "))
                numeros.append(numero)
                break
            
            except ValueError:
                print("Asegurate de introducir valores numericos.")  
    return numeros

def calcular_promedio(numeros):
    return sum(numeros) / len(numeros)

def main():
    while True:
        try:

            cantidad = 10
            numeros = solicitar_numeros(cantidad)

            promedio = calcular_promedio(numeros)

            print(f"De acuerdo a los numeros ingresados: {numeros}.")
            print(f"El promedio total es de: {promedio:.2f}")

            selección = input("¿Desea realizar más calculos? (1 : Sí - 2 : No): ").strip()

            if selección == "2":
                print("Esperamos regreses pronto.")
                break
            
            elif selección != "1":
                print("Selección invalida, regresando al inicio.")

        except Exception as e:
            print(f"Error inesperado: {e}")


main()

