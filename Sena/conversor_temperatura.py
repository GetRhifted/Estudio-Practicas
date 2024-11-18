def conversor(celcius):
    fahrenheit = (celcius * 9/5) + 32
    print(f'De acuerdo a los datos ingresados, {celcius} Celsius equivalen a {fahrenheit} Fahrenheit.') 

dato = float(input('Ingresa la cantidad de celcius a convertir: '))

try:

    dato = float(input("Ingresa la cantidad de grados Celsius a convertir: "))
    conversor(celsius = dato)

except ValueError:
    
    print("Por favor, ingresa un número válido.")