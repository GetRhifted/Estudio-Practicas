try:
    numero = int(input('Ingresa un numero: '))

    if numero % 2 == 0:
        print(f"El numero {numero} es un numero PAR.")
    else:
        print(f"El numero {numero} es un numero IMPAR.")

except ValueError:
    print("Ingresa un valor valido.")