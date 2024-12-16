def obtener_lista(cantidad):
    numeros = []
    for i in range(cantidad):
            while True:
                try:
                    numero = int(input(f"Ingresa el numero {i + 1}: "))
                    numeros.append(numero)
                    break
                except ValueError:
                    print("Recuerda ingresar valores numericos.")
    return numeros

def obtener_promedio(numeros):
    return sum(numeros) / len(numeros)

def obtener_suma(numeros): 
    return sum(numeros)

def obtener_producto(numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto

def obtener_resultados(numeros, operación, resultados):
    print(f"Los números ingresados fueron: {numeros}")
    print(f"El resultado de la operación: {operación} es: {resultados}")

def calculadora_de_listas():
    while True:
        try:
            cantidad = int(input("Bienvenido a la calculadora multifuncional, ingresa la cantidad de numeros con los que deseas trabajar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Intenta de nuevo.")
                continue

            numeros = obtener_lista(cantidad)
        
        except ValueError:
            print("Por favor ingresa un valor numerico, ej: 10.")
        
        selección = input("Ahora selecciona la operación: 1: Promedio, 2: Suma, 3: Multiplicación, 4: Salir. ")

        if selección == "1":
            resultados = obtener_promedio(numeros)
            operación = "Promedio"
            obtener_resultados(numeros, operación, resultados)
        elif selección == "2":
            resultados = obtener_suma(numeros)
            operación = "Suma"
            obtener_resultados(numeros, operación, resultados)
        elif selección == "3":
            resultados = obtener_producto(numeros)
            operación = "Multiplicación"
            obtener_resultados(numeros, operación, resultados)
        elif selección == "4":
            print("Gracias por usar la calculadora. ¡Hasta pronto!")
            return
        else:
            print("Selección inválida, regresando al inicio.")

calculadora_de_listas()


