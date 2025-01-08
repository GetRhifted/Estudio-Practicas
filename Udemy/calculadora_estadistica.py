from collections import Counter

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

def calcular_moda(lista_numeros):
    # Utilizamos Counter para contar la frecuencia de los elementos en la lista
    conteo = Counter(lista_numeros)
    
    # Encuentra la frecuencia máxima
    max_frecuencia = max(conteo.values())
    
    # Obtiene todos los números que tienen la frecuencia máxima
    moda = [num for num, frecuencia in conteo.items() if frecuencia == max_frecuencia]
    
    return moda

def user_choice():
    desicion_usuario = input("¿Deseas realizar más calculos? Responde con Si o No: ").capitalize().strip()
    if desicion_usuario not in ["Si", "No"]:
        print("Por favor, elige una opción válida (Si o No).")
    elif desicion_usuario == "No":
        print("Gracias por preferirnos.")
    return desicion_usuario


def menu():
    desision_usuario = "Si"
    while desision_usuario == "Si":
        try:
            print("Bienvenido a la calculadora estadistica \n Acontinuación encontraras las opciones: \n 1 - Calcular Promedio, 2 - Calcular Mediana, 3 - Calcular Moda, 4 - Calcular Todos, 5 - Salir ")
            selección = int(input("Ingresa tu elección, ej: 1, 2, 3, 4 o 5: "))
            if selección not in[1,2,3,4,5]:
                raise ValueError("Asegurate de usar una opción valida.")
            
            elif selección == 1:
                cantidad_numeros = validador_cantidad()
                lista_numeros = generar_lista(cantidad_numeros)
                promedio = promediador(lista_numeros)
                print(f"El promedio para los numeros ingresados es de: {promedio} ")
                desision_usuario = user_choice()

            elif selección == 2:
                cantidad_numeros = validador_cantidad()
                lista_numeros = generar_lista(cantidad_numeros)
                mediana = calculadora_mediana(lista_numeros)
                print(f"La mediana para los numeros ingresados es de {mediana}")
                desision_usuario = user_choice()
            
            elif selección == 3:
                cantidad_numeros = validador_cantidad()
                lista_numeros = generar_lista(cantidad_numeros)
                moda = calcular_moda(lista_numeros)
                print(f"La moda para los numeros ingresados es de {moda}")
                desision_usuario = user_choice()
            
            elif selección == 4:
                cantidad_numeros = validador_cantidad()
                lista_numeros = generar_lista(cantidad_numeros)
                promedio = promediador(lista_numeros)
                mediana = calculadora_mediana(lista_numeros)
                moda = calcular_moda(lista_numeros)
                print(f"El promedio para los numeros ingresados es de: {promedio}, la mediana es de {mediana} y, la moda es de: {moda}")
                desision_usuario = user_choice()

            elif selección == 5:
                print("Gracias por preferirnos, regresa pronto.")
                break

            else:
                print("Opción invalida.")
        
        except ValueError as e:
            print(e)

menu()
