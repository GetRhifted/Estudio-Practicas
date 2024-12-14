def obtener_lista(cantidad):
    while True:
        try:
            numeros = []

            for i in range(cantidad):
                numero = int(input(f"Ingresa el numero {i + 1}: "))
                numeros.append(numero)
            return numeros
        
        except ValueError:
            print("Recuerda ingresar valores numericos.")

def obtener_promedio(numeros):
    return sum(numeros) / len(numeros)

def obtener_suma(numeros): 
    return sum(numeros)

def obtener_producto(numeros):
    producto = 1
    for numero in numeros:
        producto *= numero
    return producto
    

def calculadora_de_listas():
    while True:
        try:
            cantidad = int(input("Ingresa la cantidad de numeros con los que deseas trabajar: "))
            if cantidad <= 0:
                print("La cantidad debe ser mayor a 0. Intenta de nuevo.")
                continue

            numeros = obtener_lista(cantidad)
        
        except ValueError:
            print("Por favor ingresa un valor numerico, ej: 10.")
        
        try:
            selección = input("Bienvenido, por favor selecciona el numero de operación que deseas realizar: 1 : Promedio, 2 : Suma, 3 : Producto, 4 : Salir. ")

            if selección == "1":
                promedio = obtener_promedio(numeros)
                print(f"Los numeros ingresados fueron: {numeros}")
                print(f"El promedio total para los numeros indicados es de: {promedio:.2f}")
            
            elif selección == "2":
                suma = obtener_suma(numeros)
                print(f"Los numeros ingresados fueron: {numeros}")
                print(f"La suma total para los numeros indicados es de: {suma}")
            
            elif selección == "3":
                producto = obtener_producto(numeros)
                print(f"Los numeros ingresados fueron: {numeros}")
                print(f"El producto total para los numeros indicados es de: {producto}")

            elif selección == "4":
                print("Gracias por usar la calculadora. ¡Hasta pronto!")
                return
            
            else:
                print("Selección invalida, regresando al inicio.")
        
        except Exception as e:
            print(f"Error inesperado: {e}")

calculadora_de_listas()


