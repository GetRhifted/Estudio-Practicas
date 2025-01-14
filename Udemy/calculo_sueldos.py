def ingreso_horas():
    while True:
        try:
            horas = int(input("Ingresa por favor el numero de horas que has trabajado: "))
            if horas < 0:
                raise ValueError("Asegurate de ingresar numeros posivitos u horas por encima de 0.")
            return horas
        except ValueError as e:
            print(e)

def calcular_sueldos(horas):
    valor_hora = 1000
    valor_hora_extra = 1500

    if horas <= 40:  # Si trabaja 40 horas o menos
        sueldo = horas * valor_hora
    else:  # Si trabaja más de 40 horas
        horas_extras = horas - 40
        sueldo = (40 * valor_hora) + (horas_extras * valor_hora_extra)

    return sueldo

def main():
    while True:
        horas = ingreso_horas()
        if horas == 0:  # Permitir que el usuario termine el programa ingresando 0
            print("¡Gracias por usar el programa!")
            break
        sueldo = calcular_sueldos(horas)
        print(f"El sueldo a pagar teniendo en cuenta el total de horas trabajadas es de ${sueldo}.")

main()




