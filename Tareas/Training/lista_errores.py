while True:

    try:

        numeros = []

        print("Ingresa una total de 7 numeros, uno a la vez: ")
        for n in range(7):
            numero = int(input(f"Ingresa el numero {n + 1}: "))

            if type(numero) != int:
                raise ValueError("Recuerda que necesitas ingresas valores numericos.")
            
            numeros.append(numero)

            if len(numeros) <= 0:
                print("Parece que no has ingresado ningún numero.")
        
        promedio = sum(numeros) / len(numeros)

        print(f"Dados los numeros ingresados: {numeros}. La medida total es de: {promedio:.2f}. ")
        print('¿Deseas realizar nuevos calculos?')
        selcción = int(input("1 : Sí - 2 : No: "))

        if selcción == 2:
            print("Esperamos que regreses pronto.")
            break


    except ValueError as e:
        print(f"Error: {e}")


