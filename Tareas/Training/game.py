import random

def user_choice():
    while True:
        try:
            selección_usuario = int(input("Ingresa tu elección: 1: Piedra - 2 : Tijeras - 3: Papel - 4: Salir: "))
            if selección_usuario not in [1, 2, 3, 4]:
                raise ValueError("Opción no válida. Debes ingresar 1, 2, 3 o 4.")
            return selección_usuario
        except ValueError as e:
            print(e)


def cpu_choice():
    opciones = {1: "Piedra", 2: "Tijeras", 3: "Papel"}
    selección_cpu = random.choice(list(opciones.keys()))
    print(f"CPU eligió: {opciones[selección_cpu]}")
    return selección_cpu


def match_points():
    user_wins = 0
    cpu_wins = 0
    opciones = {1: "Piedra", 2: "Tijeras", 3: "Papel"}

    while user_wins < 3 and cpu_wins < 3:
        selección_usuario = user_choice()
        
        if selección_usuario == 4:
            print("Gracias por jugar, esperamos vuelvas pronto.")
            return

        selección_cpu = cpu_choice()

        print(f"Tú elegiste: {opciones[selección_usuario]}")
        
        # Comparación de resultados
        if selección_cpu == selección_usuario:
            print("Esta ronda es un empate.")
        elif (selección_cpu == 1 and selección_usuario == 2) or \
             (selección_cpu == 2 and selección_usuario == 3) or \
             (selección_cpu == 3 and selección_usuario == 1):
            print("CPU gana esta ronda.")
            cpu_wins += 1
        else:
            print("¡Ganaste esta ronda!")
            user_wins += 1

        print(f"Puntaje actual: Usuario {user_wins} - CPU {cpu_wins}")

    # Resultado final
    if user_wins == 3:
        print("¡Felicitaciones, ganaste la partida!")
    else:
        print("La CPU ganó esta partida.")

match_points()