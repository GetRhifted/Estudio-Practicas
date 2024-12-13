decisión = 1

while decisión > 0:
    numero_1 = int(input("Ingresa el numero que quieres sumar: "))
    numero_2 = int(input("¿Cuanto deseas sumar? "))

    if numero_1 == 0 or numero_2 == 0:
        decisión = 0

    suma = numero_1 + numero_2

    print(f'La suma es de: {suma}')



