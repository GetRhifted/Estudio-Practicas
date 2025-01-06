import random

def amount_options():
    while True:
        try:
            cantidad_opciones = int(input("Ingresa la cantidad de opciones con las que quieres trabajar (Se recomienda que este número no sea mayor a 10): "))
            if cantidad_opciones <= 0:
                raise ValueError("Asegúrate de ingresar un valor mayor a 0.")
            if cantidad_opciones > 10:
                print("Nota: Trabajar con más de 10 opciones puede no ser práctico.")
            return cantidad_opciones
        except ValueError as e:
            print(e)

def options(cantidad_opciones):
    opciones = []
    for i in range(cantidad_opciones):
        while True:
            try:
                opcion = input(f"Ingresa la opción número {i + 1}: ")
                if not opcion.strip():
                    raise ValueError("Asegúrate de no dejar campos en blanco.")
                opciones.append(opcion)
                break
            except ValueError as e:
                print(e)
    return opciones

def chooser():
    desicion_usuario = "Si"
    while desicion_usuario == "Si":
        cantidad_opciones = amount_options()
        opciones = options(cantidad_opciones)
        
        if not opciones:
            print("No se ingresaron opciones válidas. Intenta de nuevo.")
            return
        
        seleccion = random.choice(opciones)
        print(f"Nuestra opción recomendada es: {seleccion}")

        desicion_usuario = input("¿Deseas agregar nuevas opciones? Responde con Si o No: ").capitalize().strip()
        
        if desicion_usuario == "Si":
            continue
        elif desicion_usuario == "No":
            print("Gracias por preferirnos, regresa pronto.")
            break
        else:
            print("Por favor ingresa una opción valida. Ej: Si o No.")

# Ejecución del programa
chooser()




            



