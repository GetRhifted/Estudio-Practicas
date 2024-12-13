import math

# Versión Inicial:

pi = 3.14
radio = float(input("Ingresa el radio del circulo a calcular: "))

try:
    area = pi * (radio * radio)
    print(f"El area para el circulo con un radio de: {radio} es de: {area:.2f}")

except ValueError:
    print("Ingresa valores validos por favor.")


# Versión Mejorada:

try:
    # Solicitar entrada y convertir a flotante
    radio = float(input("Ingresa el radio del círculo a calcular: "))

    # Validar que el radio sea positivo
    if radio < 0:
        print("El radio no puede ser negativo. Por favor, ingresa un valor válido.")
    else:
        # Calcular el área
        area = math.pi * (radio ** 2)
        print(f"El área para el círculo con un radio de {radio} es: {area:.2f}")

except ValueError:
    print("Ingresa un valor numérico válido por favor.")