import random

def definir_rango():
    while True:
        try:
            rango = int(input("Por favor ingresa el numero maximo a tener en cuenta: "))
            if rango < 0:
                raise ValueError("Asegurate de indicar un numero positivo.")
            return rango
        except ValueError as e:
            print(e)

def cpu_choice(rango):
    opciones = []
    for numero in range(rango):
        opciones.append(numero)
    opcion = random.choice(opciones)
    return opcion

def main():
    decision_usuario = "Si"
    counter = 0
    rango = definir_rango()
    cpu_option = cpu_choice(rango)
    while decision_usuario == "Si":
        try:
            user_option = int(input(f"Ingresa el numero que crees que fue seleccionado en un rango de 0 a {rango}: "))
            if user_option < 0 or user_option > rango:
                raise ValueError(f"Asegurate de no introducir ni opciones negativas ni mayores a {rango}.")
            elif user_option < cpu_option:
                print("Tu respuesta es menor al numero correcto.")
                counter += 1
            elif user_option > cpu_option:
                print("Tu respuesta es mayor al numero correcto.")
                counter += 1
            elif user_option == cpu_option:
                print(f"Felicitaciones, {user_option} es el numero correcto. Usaste un total de {counter} intentos.")
                break
            else:
                print("Opción invalida.")
        except ValueError as e:
            print(e)
        
main()





